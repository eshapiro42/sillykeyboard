import sys
import mido
import time
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QSlider, QHBoxLayout, QVBoxLayout

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        self.stop_threads = threading.Event()

        self.input_combobox = QComboBox(self)
        self.input_combobox.addItems(mido.get_input_names())

        self.output_combobox = QComboBox(self)
        self.output_combobox.addItems(mido.get_output_names())

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)

        self.delay_slider = QSlider(Qt.Horizontal)
        self.delay_slider.setMinimum(0)
        self.delay_slider.setMaximum(10000)
        self.delay_slider.setValue(0)
        self.delay_slider.valueChanged.connect(self.delayChange)

        self.delay_label = QLabel(self)
        self.delay_label.setText("0 ms")

        self.interval_slider = QSlider(Qt.Horizontal)
        self.interval_slider.setMinimum(-12)
        self.interval_slider.setMaximum(12)
        self.interval_slider.setValue(0)
        self.interval_slider.valueChanged.connect(self.intervalChange)

        self.interval_label = QLabel(self)
        self.interval_label.setText("0 half steps")

        self.devices_hbox = QHBoxLayout()
        self.devices_hbox.addWidget(self.input_combobox)
        self.devices_hbox.addWidget(self.output_combobox)
        self.devices_hbox.addStretch(1)

        self.controls_hbox = QHBoxLayout()
        self.controls_hbox.addStretch(1)
        self.controls_hbox.addWidget(self.delay_label)
        self.controls_hbox.addStretch(1)
        self.controls_hbox.addWidget(self.delay_slider)
        self.controls_hbox.addWidget(self.interval_label)
        self.controls_hbox.addStretch(1)
        self.controls_hbox.addWidget(self.interval_slider)
        self.controls_hbox.addWidget(self.start_button)
        self.controls_hbox.addWidget(self.stop_button)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.devices_hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.controls_hbox)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def delayChange(self):
        self.delay_label.setText(str(self.delay_slider.value()) + " ms")

    def intervalChange(self):
        self.interval_label.setText(str(self.interval_slider.value()) + " half steps")

    def start(self):
        self.stop_threads.set()
        time.sleep(.1)
        self.stop_threads.clear()
        outport = mido.open_output(self.input_combobox.currentText())
        inport = mido.open_input(self.output_combobox.currentText())
        delay = float(self.delay_slider.value())
        interval = int(self.interval_slider.value())
        buffer = []
        def callback():
            while not self.stop_threads.is_set():
                # Look for ripe MIDI messages
                for msg, added_time in buffer:
                    if added_time + (delay / float(1000)) < time.time():
                        if msg.type in ["note_on", "note_off"]:
                            msg.note += interval
                        outport.send(msg)
                        buffer.remove((msg, added_time))
                # Look for new MIDI messages
                for msg in inport.iter_pending():
                    buffer.append((msg, time.time()))
        t = threading.Thread(target=callback)
        t.start()

    def stop(self):
        self.stop_threads.set()

    def closeEvent(self, event):
        self.stop_threads.set()
        event.accept()

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
