import sys
import mido
import time
import threading
import gui
import copy
import mido.backends.rtmidi
from PyQt5 import QtCore, QtGui, QtWidgets

class Effect():
    def __init__(self, tab):
        self.buffer = []
        self.notetimes = {i: 0 for i in range(128)}
        self.type = tab
        if self.type == 'transpose':
            self.interval = int(ui.intervalSpinBox.value())
        elif self.type == 'mirror':
            self.position = ui.positionComboBox.currentText()
            # All note indices are shifted down by 21 from their MIDI value
            self.axis = ui.notesList().index(ui.axisComboBox.currentText()) + 21
            self.axisName = ui.axisComboBox.currentText()
        elif self.type == 'repeat':
            repeat_time = int(ui.repeatSpinBox.value())
            self.repeat_time = repeat_time / float(1000)
            self.label = 'Repeat after {}ms'.format(repeat_time)
        delay = ui.delaySpinBox.value()
        volume = ui.volumeSpinBox.value()
        self.delay = delay / float(1000)
        self.volume = volume / float(100)
        self.label = self.createLabel()

    def createLabel(self):
        if self.type == 'transpose':
            direction = 'up' if self.interval >= 0 else 'down'
            label = 'Transpose {} {} half steps'.format(direction, abs(self.interval))
        elif self.type == 'mirror':
            label = 'Reflect {} {}'.format(self.position.lower(), self.axisName)
        elif self.type == 'repeat':
            repeat_time = int(self.repeat_time * 1000)
            label = 'Repeat after {}ms'.format(repeat_time)
        delay, volume = int(self.delay * 1000), int(self.volume * 100)
        delaychanged, volumechanged = delay is not 0, volume is not 100
        if delaychanged or volumechanged:
            label += ' -'
        if delaychanged:
            label += ' {}ms delay'.format(delay)
            if volumechanged:
                label += ' -'
        if volumechanged:
            label += ' {}% volume'.format(volume)
        return label

    def addToList(self):
        ui.currentEffects.append(self)
        ui.currentEffectsList.addItem(self.label)

    def run(self):
        return {'transpose': self.transpose,
                'mirror': self.mirror,
                'repeat': self.repeat
                }[self.type]

    def transpose(self, out_msg, addedTime):
        if out_msg.type in ['note_on', 'note_off']:
            # Do not play back an unchanged note
            if self.interval == 0 and self.delay == 0:
                return None
            # Skip notes below 0 or above 127
            if out_msg.note + self.interval < 0 or out_msg.note + self.interval > 127:
                return None
            out_msg.note += self.interval
            out_msg.velocity = min(int(out_msg.velocity * self.volume), 127)
        return out_msg

    def mirror(self, out_msg, addedTime):
        if out_msg.type in ['note_on', 'note_off']:
            mirrored_note = out_msg.note - 2 * (out_msg.note - self.axis)
            mirrored_note += {'On': 0, 'Above': 1, 'Below': -1}[self.position]
            # Do not play back an unchanged note
            if mirrored_note == out_msg.note and self.delay == 0:
                return None
            # Skip notes below 0 or above 127
            if mirrored_note < 0 or mirrored_note > 127:
                return None
            out_msg.note = mirrored_note
            out_msg.velocity = min(int(out_msg.velocity * self.volume), 127)
        return out_msg

    def repeat(self, out_msg, addedTime):
        if out_msg.type in ['note_on', 'note_off']:
            out_msg.velocity = min(int(out_msg.velocity * self.volume), 127)
            self.buffer.append((out_msg, addedTime + self.repeat_time))
            print(out_msg.note, self.notetimes[out_msg.note])
        if out_msg.type is 'note_on':
            self.notetimes[out_msg.note] += 1
        if out_msg.type is 'note_off':
            if self.notetimes[out_msg.note] > 0:
                self.notetimes[out_msg.note] -= 1
            if self.notetimes[out_msg.note] > 0:
                out_msg = None
        return out_msg

class Window(gui.Ui_MainWindow):
    def __init__(self):
        super(Window, self).setupUi(MainWindow)
        self.setup()
        self.actions()
        self.start()

    def setup(self):
        self.stopThreads = threading.Event()
        self.inputComboBox.addItems(mido.get_input_names())
        self.outputComboBox.addItems(mido.get_output_names())
        self.axisComboBox.addItems(self.notesList())
        self.axisComboBox.setCurrentIndex(self.notesList().index('C4'))
        self.positionComboBox.addItems(['Above', 'On', 'Below'])
        self.positionComboBox.setCurrentIndex(1)
        self.currentEffects = []

    def actions(self):
        self.addEffectButton.clicked.connect(self.addEffect)
        self.removeEffectButton.clicked.connect(self.removeEffect)
        self.deviceSelectButton.clicked.connect(self.selectDevice)
        self.deviceRefreshButton.clicked.connect(self.refreshDevices)

    def addEffect(self):
        # Check which tab is active
        tabindex = self.tabWidget.currentIndex()
        tab = {0: 'transpose', 1: 'mirror', 2: 'repeat'}[tabindex]
        effect = Effect(tab)
        # If an effect is active with the same label, do not add it again
        if any([existing.label == effect.label for existing in self.currentEffects]):
            del effect
        else:
            effect.addToList()

    def removeEffect(self):
        try:
            for effect in self.currentEffects:
                if effect.label == self.currentEffectsList.currentItem().text():
                    self.currentEffects.remove(effect)
                    del effect
            self.currentEffectsList.takeItem(self.currentEffectsList.currentRow())
        except:
            return

    def start(self):
        self.selectDevice()
        t = threading.Thread(target=self.main_thread)
        t.start()

    def inport_callback(self, msg):
        addedTime = time.time()
        for effect in self.currentEffects:
            effect.buffer.append((msg, addedTime))

    def main_thread(self):
        while not self.stopThreads.is_set():
            # Look for ripe MIDI messages
            for effect in self.currentEffects:
                for msg, addedTime in effect.buffer:
                    if addedTime + effect.delay < time.time():
                        out_msg = msg.copy()
                        out_msg = effect.run()(out_msg, addedTime)
                        if not out_msg:
                            continue
                        self.outport.send(out_msg)
                        effect.buffer.remove((msg, addedTime))
            time.sleep(0.0001)

    def notesList(self):
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        notes = ['A0', 'A#0', 'B0']
        for octave in range(1, 8):
            for key in keys:
                notes.append(key + str(octave))
        notes.append('C8')
        return notes

    def selectDevice(self):
        try:
            self.outport = mido.open_output(self.outputComboBox.currentText(), autoreset=True)
            self.inport = mido.open_input(self.inputComboBox.currentText(), autoreset=True, callback=self.inport_callback)
        except:
            return

    def refreshDevices(self):
        originalInput = self.inputComboBox.currentText()
        self.inputComboBox.clear()
        self.inputComboBox.addItems(mido.get_input_names())
        try:
            self.inputComboBox.setCurrentIndex(mido.get_input_names().index(originalInput))
        except:
            pass
        originalOutput = self.outputComboBox.currentText()
        self.outputComboBox.clear()
        self.outputComboBox.addItems(mido.get_output_names())
        try:
            self.outputComboBox.setCurrentIndex(mido.get_output_names().index(originalOutput))
        except:
            pass

    def stop(self):
        # Close the ports
        try:
            self.inport.close()
            self.outport.close()
        except:
            pass
        # Kill the thread
        self.stopThreads.set()
        time.sleep(.05)
        self.stopThreads.clear()

    def close(self):
        self.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('piano-icon.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    MainWindow.show()
    ret = app.exec_()
    ui.close()
    sys.exit(ret)
