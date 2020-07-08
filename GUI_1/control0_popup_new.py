# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control0_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
# test here

######## control0 popup script #########

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 311)

        #Main layout 
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 311, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #rst_ePLL checkbox
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox.clicked.connect(self.checked_box)

        #reset_jtag_in checkbox
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_2.clicked.connect(self.checked_box_2)

        #event_reset_jtag_in checkbox
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_3.clicked.connect(self.checked_box_3)

        #chnl_fifo_overflow_clear checkbox
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_4.clicked.connect(self.checked_box_4)

        #layout for debug_port_select 
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 180, 311, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #debug_port_select
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.changed_line1)

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        #Save button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 311, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.reject)

        #enabling the messages to print on the TDC tab 
        self.message_1 = ""
        self.message_2 = ""
        self.message_3 = ""
        self.message_4 = ""
        self.message_5 = ""

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Control0"))
        self.checkBox.setText(_translate("Dialog", "rst_ePLL"))
        self.checkBox_2.setText(_translate("Dialog", "reset_jtag_in"))
        self.checkBox_3.setText(_translate("Dialog", "event_reset_jtag_in"))
        self.checkBox_4.setText(_translate("Dialog", "chnl_fifo_overflow_clear"))
        self.label.setText(_translate("Dialog", "debug_port_select"))
        self.pushButton.setText(_translate("Dialog", "Run control0"))

    #Functions for the checkboxes 
    def checked_box(self): 
        if self.checkBox.isChecked() == True:
            self.message_1 = "rst_ePLL: set   "
        else:
            self.message_1 = ""

    def checked_box_2(self): 
        if self.checkBox_2.isChecked() == True: 
            self.message_2 = "reset_jtag_in: set   "
        else: 
            self.message_2 = ""

    def checked_box_3(self): 
        if self.checkBox_3.isChecked() == True: 
            self.message_3 = "event_reset_jtag_in: set   "
        else: 
            self.message_3 = ""

    def checked_box_4(self): 
        if self.checkBox_4.isChecked() == True: 
            self.message_4 = "chnl_fifo_overflow_clear: set   "
        else: 
            self.message_4 = ""


    #Function for the line edit 
    def changed_line1(self): 
        self.message_5 = "debug_port_select: " + self.lineEdit.text() + "    "



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
