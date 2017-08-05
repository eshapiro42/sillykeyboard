import sys
import mido
import time
import threading
import gui
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
    #         self.inputComboBox.clear()
    #         self.inputComboBox.addItems(mido.get_input_names())
    #         self.outputComboBox.clear()
    #         self.outputComboBox.addItems(mido.get_output_names())
    #
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(refreshDevices)
    #     self.timer.start(2000)

    def start(self):
        self.stopThreads.set()
        time.sleep(.05)
        self.stopThreads.clear()
        outport = mido.open_output(self.inputComboBox.currentText())
        inport = mido.open_input(self.outputComboBox.currentText())
        delay = float(self.delaySpinBox.value())
        volume = float(self.volumeSpinBox.value())
        buffer = []

        def transpose():
            interval = int(self.intervalSpinBox.value())
            while not self.stopThreads.is_set():
                # Look for ripe MIDI messages
                for msg, addedTime in buffer:
                    if addedTime + (delay / float(1000)) < time.time():
                        if msg.type in ["note_on", "note_off"]:
                            msg.note += interval
                            msg.velocity = min(int(msg.velocity * volume / 100), 126)
                        outport.send(msg)
                        buffer.remove((msg, addedTime))
                # Look for new MIDI messages
                for msg in inport.iter_pending():
                    buffer.append((msg, time.time()))

        def mirror():
            position = self.positionComboBox.currentText()
            # All note indices are shifted down by 21 from their MIDI value
            axis = self.notesList().index(self.axisComboBox.currentText()) + 21
            while not self.stopThreads.is_set():
                # Look for ripe MIDI messages
                for msg, addedTime in buffer:
                    if addedTime + (delay / float(1000)) < time.time():
                        if msg.type in ["note_on", "note_off"]:
                            msg.note -= 2 * (msg.note - axis)
                            msg.velocity = min(int(msg.velocity * volume / 100), 126)
                        outport.send(msg)
                        buffer.remove((msg, addedTime))
                # Look for new MIDI messages
                for msg in inport.iter_pending():
                    buffer.append((msg, time.time()))


        if self.tabWidget.currentIndex() is 0:
            callback = transpose
        if self.tabWidget.currentIndex() is 1:
            callback = mirror
        t = threading.Thread(target=callback)
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
        self.stopThreads.set()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    MainWindow.show()
    ret = app.exec_()
    ui.close()
    sys.exit(ret)
