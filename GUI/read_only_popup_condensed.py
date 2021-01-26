# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_only.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from StyleSheet import *
from crc8_D81 import *
class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(325, 339)
        
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # instruction error
        self.lineEdit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit.setStyleSheet(LedGreen if self.TDC_inst.instruction_error[0]=='0' else LedRed)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        #CRC
        self.lineEdit_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.lineEdit_2.setText(format(int(self.TDC_inst.CRC[0], 2), '08X'))
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        #CRC_cal
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_8.setText(crc_cal(self.TDC_inst))
        # self.label_8.setText('FFFFFFFF')
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        #ePll lock
        self.lineEdit_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_3, 6, 2, 1, 1)
        self.lineEdit_3.setStyleSheet(LedGreen if self.TDC_inst.ePll_lock[0]=='1' else LedRed)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)

        #chnl fifo overflow
        self.lineEdit_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_4, 7, 2, 1, 1)
        self.lineEdit_4.setText(format(int(self.TDC_inst.chnl_fifo_overflow[0], 2), '06X'))
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)

        #read status labels
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)

        # bottom button stuff
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 280, 281, 41))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        # Apply button
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.apply_button)

        # OK button
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.OK_button)
        self.pushButton_2.clicked.connect(Dialog.reject)

        # Cancel button
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Read Only"))
        self.label.setText(_translate("Dialog", "read status 0"))
        self.label_2.setText(_translate("Dialog", "read status 1"))
        self.label_3.setText(_translate("Dialog", "instruction_error: "))
        self.label_4.setText(_translate("Dialog", "CRC_JTAG: "))
        self.label_5.setText(_translate("Dialog", "ePll_lock: "))
        self.label_6.setText(_translate("Dialog", "chnl_fifo_overflow: "))
        self.label_7.setText(_translate("Dialog", "CRC_cal: "))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    def apply_button(self):
        self.TDC_inst.read_status_0()
        self.TDC_inst.read_status_1()
        self.show_value()

    def OK_button(self):
        self.TDC_inst.read_status_0()
        self.TDC_inst.read_status_1()
        self.show_value()

    def show_value(self):
        self.label_8.setText(crc_cal(self.TDC_inst))
        self.lineEdit.setStyleSheet(LedGreen if self.TDC_inst.instruction_error[0]=='0' else LedRed)
        self.lineEdit_2.setText(format(int(self.TDC_inst.CRC[0], 2), '08X'))
        self.lineEdit_3.setStyleSheet(LedGreen if self.TDC_inst.ePll_lock[0]=='1' else LedRed)
        self.lineEdit_4.setText(format(int(self.TDC_inst.chnl_fifo_overflow[0], 2), '06X'))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())