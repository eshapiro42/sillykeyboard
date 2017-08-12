# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 368)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deviceFrame = QtWidgets.QFrame(self.centralwidget)
        self.deviceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deviceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deviceFrame.setObjectName("deviceFrame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.deviceFrame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deviceWidget = QtWidgets.QWidget(self.deviceFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceWidget.sizePolicy().hasHeightForWidth())
        self.deviceWidget.setSizePolicy(sizePolicy)
        self.deviceWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.deviceWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.deviceWidget.setObjectName("deviceWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.deviceWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.deviceHorizontalLayout = QtWidgets.QHBoxLayout()
        self.deviceHorizontalLayout.setObjectName("deviceHorizontalLayout")
        self.inputVerticalLayout = QtWidgets.QVBoxLayout()
        self.inputVerticalLayout.setObjectName("inputVerticalLayout")
        self.inputLabel = QtWidgets.QLabel(self.deviceWidget)
        self.inputLabel.setObjectName("inputLabel")
        self.inputVerticalLayout.addWidget(self.inputLabel)
        self.inputComboBox = QtWidgets.QComboBox(self.deviceWidget)
        self.inputComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.inputComboBox.setObjectName("inputComboBox")
        self.inputVerticalLayout.addWidget(self.inputComboBox)
        self.deviceHorizontalLayout.addLayout(self.inputVerticalLayout)
        self.outputVerticalLayout = QtWidgets.QVBoxLayout()
        self.outputVerticalLayout.setObjectName("outputVerticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.deviceWidget)
        self.outputLabel.setObjectName("outputLabel")
        self.outputVerticalLayout.addWidget(self.outputLabel)
        self.outputComboBox = QtWidgets.QComboBox(self.deviceWidget)
        self.outputComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.outputComboBox.setObjectName("outputComboBox")
        self.outputVerticalLayout.addWidget(self.outputComboBox)
        self.deviceHorizontalLayout.addLayout(self.outputVerticalLayout)
        self.horizontalLayout_4.addLayout(self.deviceHorizontalLayout)
        self.verticalLayout_6.addWidget(self.deviceWidget)
        self.verticalLayout.addWidget(self.deviceFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.transposeTab = QtWidgets.QWidget()
        self.transposeTab.setObjectName("transposeTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.transposeTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.intervalSplitter = QtWidgets.QSplitter(self.transposeTab)
        self.intervalSplitter.setOrientation(QtCore.Qt.Vertical)
        self.intervalSplitter.setObjectName("intervalSplitter")
        self.intervalLabel = QtWidgets.QLabel(self.intervalSplitter)
        self.intervalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.intervalLabel.setObjectName("intervalLabel")
        self.intervalSpinBox = QtWidgets.QSpinBox(self.intervalSplitter)
        self.intervalSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.intervalSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.intervalSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.intervalSpinBox.setMinimum(-100)
        self.intervalSpinBox.setMaximum(100)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.verticalLayout_4.addWidget(self.intervalSplitter)
        self.tabWidget.addTab(self.transposeTab, "")
        self.mirrorTab = QtWidgets.QWidget()
        self.mirrorTab.setObjectName("mirrorTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mirrorTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.positionVerticalLayout = QtWidgets.QVBoxLayout()
        self.positionVerticalLayout.setObjectName("positionVerticalLayout")
        self.positionLabel = QtWidgets.QLabel(self.mirrorTab)
        self.positionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.positionLabel.setObjectName("positionLabel")
        self.positionVerticalLayout.addWidget(self.positionLabel)
        self.positionComboBox = QtWidgets.QComboBox(self.mirrorTab)
        self.positionComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.positionComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.positionComboBox.setObjectName("positionComboBox")
        self.positionVerticalLayout.addWidget(self.positionComboBox)
        self.horizontalLayout_3.addLayout(self.positionVerticalLayout)
        self.axisVerticalLayout = QtWidgets.QVBoxLayout()
        self.axisVerticalLayout.setObjectName("axisVerticalLayout")
        self.axisLabel = QtWidgets.QLabel(self.mirrorTab)
        self.axisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.axisLabel.setObjectName("axisLabel")
        self.axisVerticalLayout.addWidget(self.axisLabel)
        self.axisComboBox = QtWidgets.QComboBox(self.mirrorTab)
        self.axisComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.axisComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.axisComboBox.setObjectName("axisComboBox")
        self.axisVerticalLayout.addWidget(self.axisComboBox)
        self.horizontalLayout_3.addLayout(self.axisVerticalLayout)
        self.tabWidget.addTab(self.mirrorTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.controlFrame = QtWidgets.QFrame(self.centralwidget)
        self.controlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlFrame.setObjectName("controlFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controlFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlWidget = QtWidgets.QWidget(self.controlFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlWidget.sizePolicy().hasHeightForWidth())
        self.controlWidget.setSizePolicy(sizePolicy)
        self.controlWidget.setMinimumSize(QtCore.QSize(0, 80))
        self.controlWidget.setObjectName("controlWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.controlWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.volumeVerticalLayout = QtWidgets.QVBoxLayout()
        self.volumeVerticalLayout.setObjectName("volumeVerticalLayout")
        self.volumeLabel = QtWidgets.QLabel(self.controlWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.volumeVerticalLayout.addWidget(self.volumeLabel)
        self.volumeSpinBox = QtWidgets.QSpinBox(self.controlWidget)
        self.volumeSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.volumeSpinBox.setMaximum(200)
        self.volumeSpinBox.setProperty("value", 100)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.volumeVerticalLayout.addWidget(self.volumeSpinBox)
        self.horizontalLayout_2.addLayout(self.volumeVerticalLayout)
        self.delayVerticalLayout = QtWidgets.QVBoxLayout()
        self.delayVerticalLayout.setObjectName("delayVerticalLayout")
        self.delayLabel = QtWidgets.QLabel(self.controlWidget)
        self.delayLabel.setObjectName("delayLabel")
        self.delayVerticalLayout.addWidget(self.delayLabel)
        self.delaySpinBox = QtWidgets.QSpinBox(self.controlWidget)
        self.delaySpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.delaySpinBox.setMaximum(60000)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.delayVerticalLayout.addWidget(self.delaySpinBox)
        self.horizontalLayout_2.addLayout(self.delayVerticalLayout)
        self.emptyWidget = QtWidgets.QWidget(self.controlWidget)
        self.emptyWidget.setObjectName("emptyWidget")
        self.horizontalLayout_2.addWidget(self.emptyWidget)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.startEmptyLabel = QtWidgets.QLabel(self.controlWidget)
        self.startEmptyLabel.setText("")
        self.startEmptyLabel.setObjectName("startEmptyLabel")
        self.verticalLayout_9.addWidget(self.startEmptyLabel)
        self.startButton = QtWidgets.QPushButton(self.controlWidget)
        self.startButton.setMinimumSize(QtCore.QSize(0, 30))
        self.startButton.setObjectName("startButton")
        self.verticalLayout_9.addWidget(self.startButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stopEmptyLabel = QtWidgets.QLabel(self.controlWidget)
        self.stopEmptyLabel.setText("")
        self.stopEmptyLabel.setObjectName("stopEmptyLabel")
        self.verticalLayout_8.addWidget(self.stopEmptyLabel)
        self.stopButton = QtWidgets.QPushButton(self.controlWidget)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_8.addWidget(self.stopButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.horizontalLayout.addWidget(self.controlWidget)
        self.verticalLayout.addWidget(self.controlFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SillyKeyboard"))
        self.inputLabel.setText(_translate("MainWindow", "Input"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.intervalLabel.setText(_translate("MainWindow", "Interval (half steps)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transposeTab), _translate("MainWindow", "Transpose"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.axisLabel.setText(_translate("MainWindow", "Axis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mirrorTab), _translate("MainWindow", "Mirror"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume (%)"))
        self.delayLabel.setText(_translate("MainWindow", "Delay (ms)"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

