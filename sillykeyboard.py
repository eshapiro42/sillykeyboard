import sys
import mido
import time
import threading
import gui
import mido.backends.rtmidi
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(gui.Ui_MainWindow):
    def __init__(self):
        super(Window, self).setupUi(MainWindow)
        self.setup()
        self.actions()
        # self.loops()

    def setup(self):
        self.stopThreads = threading.Event()
        self.inputComboBox.addItems(mido.get_input_names())
        self.outputComboBox.addItems(mido.get_output_names())
        self.axisComboBox.addItems(self.notesList())
        self.axisComboBox.setCurrentIndex(self.notesList().index('C4'))
        self.positionComboBox.addItems(['Above', 'On', 'Below'])
        self.positionComboBox.setCurrentIndex(1)

    def actions(self):
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

    # def loops(self):
    #     def refreshDevices():
    #         originalInput = self.inputComboBox.currentText()
    #         self.inputComboBox.clear()
    #         self.inputComboBox.addItems(mido.get_input_names())
    #         self.inputComboBox.setCurrentIndex(mido.get_input_names().index(originalInput))
    #         originalOutput = self.outputComboBox.currentText()
    #         self.outputComboBox.clear()
    #         self.outputComboBox.addItems(mido.get_output_names())
    #         self.outputComboBox.setCurrentIndex(mido.get_output_names().index(originalOutput))
    #
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(refreshDevices)
    #     self.timer.start(2000)

    def start(self):
        self.stopThreads.set()
        time.sleep(.05)
        self.stopThreads.clear()
        outport = mido.open_output(self.outputComboBox.currentText())
        inport = mido.open_input(self.inputComboBox.currentText())
        delay = float(self.delaySpinBox.value())
        volume = float(self.volumeSpinBox.value())
        buffer = []
        # Check which tab is active
        if self.tabWidget.currentIndex() is 0:
            tab = 'transpose'
        if self.tabWidget.currentIndex() is 1:
            tab = 'mirror'

        def callback(tab):
            while not self.stopThreads.is_set():
                # Look for ripe MIDI messages
                for msg, addedTime in buffer:
                    if addedTime + (delay / float(1000)) < time.time():
                        if msg.type in ['note_on', 'note_off']:
                            if tab is 'transpose':
                                # Transpose
                                interval = int(self.intervalSpinBox.value())
                                # Skip notes below 0 or above 127
                                if msg.note + interval < 0 or msg.note + interval > 127:
                                    continue
                                msg.note += interval

                            if tab is 'mirror':
                                # Mirror
                                position = self.positionComboBox.currentText()
                                # All note indices are shifted down by 21 from their MIDI value
                                axis = self.notesList().index(self.axisComboBox.currentText()) + 21
                                # Skip notes below 0 or above 127
                                if msg.note - 2 * (msg.note - axis) < 0 or msg.note - 2 * (msg.note - axis) > 127:
                                    continue
                                msg.note -= 2 * (msg.note - axis)
                            msg.velocity = min(int(msg.velocity * volume / 100), 127)
                        outport.send(msg)
                        buffer.remove((msg, addedTime))
                # Look for new MIDI messages
                for msg in inport.iter_pending():
                    buffer.append((msg, time.time()))
                time.sleep(.005)
					
        t = threading.Thread(target=callback, args=[tab])
        t.start()

    def notesList(self):
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        notes = ['A0', 'A#0', 'B0']
        for octave in range(1, 8):
            for key in keys:
                notes.append(key + str(octave))
        notes.append('C8')
        return notes

    def stop(self):
        self.stopThreads.set()

    def close(self):
        self.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    MainWindow.show()
    ret = app.exec_()
    ui.close()
    sys.exit(ret)
