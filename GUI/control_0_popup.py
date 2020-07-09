# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control0_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

######## control0 popup script #########

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

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
        if self.TDC_inst.rst_ePLL[0] == '1':
            self.checkBox.setChecked(True)

        #reset_jtag_in checkbox
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        if self.TDC_inst.reset_jtag_in[0] == '1':
            self.checkBox_2.setChecked(True)

        #event_reset_jtag_in checkbox
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        if self.TDC_inst.event_reset_jtag_in[0] == '1':
            self.checkBox_3.setChecked(True)

        #chnl_fifo_overflow_clear checkbox
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        if self.TDC_inst.chnl_fifo_overflow_clear[0] == '1':
            self.checkBox_4.setChecked(True)

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
        self.lineEdit.setText(self.TDC_inst.debug_port_select[0])
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # bottom button stuff
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 250, 311, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        #Apply button
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.apply_button)
        #self.pushButton.clicked.connect(self.apply_button_mes)
        #self.pushButton.clicked.connect(Dialog.reject)

        #OK button
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.apply_button)
        #self.pushButton_2.clicked.connect(self.OK_button_mes)
        self.pushButton_2.clicked.connect(Dialog.reject)

        #Cancel button
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        #self.pushButton_3.clicked.connect(self.cancel_button_mes)
        self.pushButton_3.clicked.connect(Dialog.reject)

        # # #enabling the messages to print on the TDC tab
        # self.apply_button_message = ""
        # self.OK_button_message = ""
        # self.cancel_button_message = ""

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
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))


    # #Function for the line edit
    # def changed_line1(self):
    #     self.message_5 = "debug_port_select: " + self.lineEdit.text() + "    "


    #Function for the apply/OK buttons
    def apply_button(self):
        #rst_ePLL
        if self.checkBox.isChecked() == True:
            self.TDC_inst.rst_ePLL[0] = '1'
        else:
            self.TDC_inst.rst_ePLL[0] = '0'

        #reset_jtag_in
        if self.checkBox_2.isChecked() == True:
            self.TDC_inst.reset_jtag_in[0] = '1'
        else:
            self.TDC_inst.reset_jtag_in[0] = '0'

        #event_reset_jtag_in
        if self.checkBox_3.isChecked() == True:
            self.TDC_inst.event_reset_jtag_in[0] = '1'
        else:
            self.TDC_inst.event_reset_jtag_in[0] = '0'

        #chnl_fifo_overflow_clear
        if self.checkBox_4.isChecked() == True:
            self.TDC_inst.chnl_fifo_overflow_clear[0] = '1'
        else:
            self.TDC_inst.chnl_fifo_overflow_clear[0] = '0'

        #debug_port_select
        self.TDC_inst.debug_port_select[0] = self.lineEdit.text()

        #call update_control_0 function
        self.TDC_inst.update_control_0()

    # def apply_button_mes(self):
    #     self.apply_button_message = "control0: changes applied"
    #
    # def OK_button_mes(self):
    #     self.OK_button_message = "control0: changes saved"
    #     self.apply_button_message = ""
    #
    # def cancel_button_mes(self):
    #     self.cancel_button_message = "control0: changes canceled"
    #     self.apply_button_message = ""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
