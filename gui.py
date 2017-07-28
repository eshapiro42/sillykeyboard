import sys
import mido
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.input_combobox = QtGui.QComboBox(self)
        self.input_combobox.addItems(mido.get_input_names())

        self.output_combobox = QtGui.QComboBox(self)
        self.output_combobox.addItems(mido.get_output_names())

        self.start_button = QtGui.QPushButton("Start")
        self.stop_button = QtGui.QPushButton("Stop")

        self.delay_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.delay_slider.setMinimum(0)
        self.delay_slider.setMaximum(10000)
        self.delay_slider.setValue(0)
        self.delay_slider.valueChanged.connect(self.delayChange)

        self.delay_label = QtGui.QLabel(self)
        self.delay_label.setText("0 ms")

        self.devices_hbox = QtGui.QHBoxLayout()
        self.devices_hbox.addWidget(self.input_combobox)
        self.devices_hbox.addWidget(self.output_combobox)
        self.devices_hbox.addStretch(1)

        self.controls_hbox = QtGui.QHBoxLayout()
        self.controls_hbox.addStretch(1)
        self.controls_hbox.addWidget(self.delay_label)
        self.controls_hbox.addWidget(self.delay_slider)
        self.controls_hbox.addWidget(self.start_button)
        self.controls_hbox.addWidget(self.stop_button)

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addLayout(self.devices_hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.controls_hbox)

        self.setLayout(self.vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def delayChange(self):
        self.delay_label.setText(str(self.delay_slider.value()) + " ms")

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
