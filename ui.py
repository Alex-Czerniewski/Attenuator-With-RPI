# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/pyApps/Attenuator/ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 207)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_set_attenuation = QtWidgets.QPushButton(self.groupBox)
        self.btn_set_attenuation.setObjectName("btn_set_attenuation")
        self.gridLayout_2.addWidget(self.btn_set_attenuation, 1, 0, 1, 4)
        self.dsbox_attenuation = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dsbox_attenuation.setPrefix("")
        self.dsbox_attenuation.setSuffix("")
        self.dsbox_attenuation.setMinimum(0.0)
        self.dsbox_attenuation.setMaximum(30.0)
        self.dsbox_attenuation.setProperty("value", 5.0)
        self.dsbox_attenuation.setObjectName("dsbox_attenuation")
        self.gridLayout_2.addWidget(self.dsbox_attenuation, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAtt = QtWidgets.QAction(MainWindow)
        self.actionAtt.setObjectName("actionAtt")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attenuator"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Attenuator"))
        self.btn_set_attenuation.setText(_translate("MainWindow", "Set Attenuation"))
        self.label.setText(_translate("MainWindow", "Attenuation ="))
        self.label_2.setText(_translate("MainWindow", " dB"))
        self.actionAtt.setText(_translate("MainWindow", "Att "))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh USB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
