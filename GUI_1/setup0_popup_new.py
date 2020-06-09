# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup0_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


##########   setup0 popup script ########### 

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 698)

        #Main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 400, 491, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #Line edits setup 
        #channel_enable_r 
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit.textChanged.connect(self.changed_line1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        #channel_enable_f
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_2.textChanged.connect(self.changed_line2)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        #TDC_ID
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_3.textChanged.connect(self.changed_line3)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        #rising_is_leading
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_4.textChanged.connect(self.changed_line4)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        #width_select
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_5.textChanged.connect(self.changed_line5)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)


        #Run setup0 button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 491, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.reject)

        #Checkbox grid layout setup 
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 491, 361))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        ###################################################################################

        #bypass_bcr_distribution
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox.clicked.connect(self.checked_box)

        #enable_direct_event_reset
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_2.clicked.connect(self.checked_box_2)

        #enable_high_speed
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_3.clicked.connect(self.checked_box_3)

        #enable_leading
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 1, 1, 1, 1)
        self.checkBox_4.clicked.connect(self.checked_box_4)

        #enable_master_reset_code
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_5.clicked.connect(self.checked_box_5)

        #enable_pair
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_2.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.checkBox_6.clicked.connect(self.checked_box_6)

        #enable_trigger_timeout
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_2.addWidget(self.checkBox_7, 3, 0, 1, 1)
        self.checkBox_7.clicked.connect(self.checked_box_7)

        #full_width_res
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 3, 1, 1, 1)
        self.checkBox_8.clicked.connect(self.checked_box_8)

        #enable_TDC_ID
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 4, 0, 1, 1)
        self.checkBox_9.clicked.connect(self.checked_box_9)

        #enable_direct_bunch_reset
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 4, 1, 1, 1)
        self.checkBox_10.clicked.connect(self.checked_box_10)

        #auto_roll_over
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 5, 0, 1, 1)
        self.checkBox_11.clicked.connect(self.checked_box_11)

        #Channel_data_debug
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_2.addWidget(self.checkBox_12, 5, 1, 1, 1)
        self.checkBox_12.clicked.connect(self.checked_box_12)

        #enable_8b10b
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_2.addWidget(self.checkBox_13, 6, 0, 1, 1)
        self.checkBox_13.clicked.connect(self.checked_box_13)

        #enable_direct_trigger
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_2.addWidget(self.checkBox_14, 6, 1, 1, 1)
        self.checkBox_14.clicked.connect(self.checked_box_14)

        #enable_error_packet
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_2.addWidget(self.checkBox_15, 7, 0, 1, 1)
        self.checkBox_15.clicked.connect(self.checked_box_15)

        #enable_insert
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_2.addWidget(self.checkBox_16, 7, 1, 1, 1)
        self.checkBox_16.clicked.connect(self.checked_box_16)

        #enable_legacy
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_2.addWidget(self.checkBox_17, 8, 0, 1, 1)
        self.checkBox_17.clicked.connect(self.checked_box_17)

        #enable_new_ttc
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_2.addWidget(self.checkBox_18, 8, 1, 1, 1)
        self.checkBox_18.clicked.connect(self.checked_box_18)

        #enable_trigger
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_2.addWidget(self.checkBox_19, 9, 0, 1, 1)
        self.checkBox_19.clicked.connect(self.checked_box_19)

        #enable_fake_hit
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_2.addWidget(self.checkBox_20, 9, 1, 1, 1)
        self.checkBox_20.clicked.connect(self.checked_box_20)

        #enable_error_notify
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_2.addWidget(self.checkBox_21, 10, 0, 1, 1)
        self.checkBox_21.clicked.connect(self.checked_box_21)

        #enablinging the messages to print on the TDC tab 
        self.message_1 = ""
        self.message_2 = ""
        self.message_3 = ""
        self.message_4 = ""
        self.message_5 = ""
        self.message_6 = ""
        self.message_7 = ""
        self.message_8 = ""
        self.message_9 = ""
        self.message_10 = ""
        self.message_11 = ""
        self.message_12 = ""
        self.message_13 = ""
        self.message_14 = ""
        self.message_15 = ""
        self.message_16 = ""
        self.message_17 = ""
        self.message_18 = ""
        self.message_19 = ""
        self.message_20 = ""
        self.message_21 = ""
        self.message_22 = ""
        self.message_23 = ""
        self.message_24 = ""
        self.message_25 = ""
        self.message_26 = ""

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setup0"))
        self.label_5.setText(_translate("Dialog", "width_select"))
        self.label_3.setText(_translate("Dialog", "TDC_ID"))
        self.label.setText(_translate("Dialog", "channel_enable_r"))
        self.label_4.setText(_translate("Dialog", "rising_is_leading"))
        self.label_2.setText(_translate("Dialog", "channel_enable_f"))
        self.pushButton.setText(_translate("Dialog", "Run Setup0"))
        self.checkBox_12.setText(_translate("Dialog", "Channel_data_debug"))
        self.checkBox_18.setText(_translate("Dialog", "enable_new_ttc"))
        self.checkBox_8.setText(_translate("Dialog", "full_width_res"))
        self.checkBox_20.setText(_translate("Dialog", "enable_fake_hit"))
        self.checkBox_19.setText(_translate("Dialog", "enable_trigger"))
        self.checkBox_7.setText(_translate("Dialog", "enable_trigger_timeout"))
        self.checkBox_6.setText(_translate("Dialog", "enable_pair"))
        self.checkBox_9.setText(_translate("Dialog", "enable_TDC_ID"))
        self.checkBox_16.setText(_translate("Dialog", "enable_insert"))
        self.checkBox_13.setText(_translate("Dialog", "enable_8b10b"))
        self.checkBox_11.setText(_translate("Dialog", "auto_roll_over"))
        self.checkBox_14.setText(_translate("Dialog", "enable_direct_trigger"))
        self.checkBox_17.setText(_translate("Dialog", "enable_legacy"))
        self.checkBox_15.setText(_translate("Dialog", "enable_error_packet"))
        self.checkBox_5.setText(_translate("Dialog", "enable_master_reset_code"))
        self.checkBox_10.setText(_translate("Dialog", "enable_direct_bunch_reset"))
        self.checkBox_2.setText(_translate("Dialog", "enable_direct_event_reset"))
        self.checkBox_3.setText(_translate("Dialog", "enable_high_speed"))
        self.checkBox.setText(_translate("Dialog", "bypass_bcr_distribution"))
        self.checkBox_4.setText(_translate("Dialog", "enable_leading"))
        self.checkBox_21.setText(_translate("Dialog", "enable_error_notify"))

    #Functions for the checkboxes
    def checked_box(self): 
        if self.checkBox.isChecked() == True:
            self.message_1 = "bypass_bcr_distribution: set   "
        else:
            self.message_1 = ""

    def checked_box_2(self): 
        if self.checkBox_2.isChecked() == True:
            self.message_2 = "enable_direct_event_reset: set   "
        else:
            self.message_2 = ""

    def checked_box_3(self): 
        if self.checkBox_3.isChecked() == True:
            self.message_3 = "enable_high_speed: set   "
        else:
            self.message_3 = ""

    def checked_box_4(self): 
        if self.checkBox_4.isChecked() == True:
            self.message_4 = "enable_leading: set   "
        else:
            self.message_4 = ""

    def checked_box_5(self): 
        if self.checkBox_5.isChecked() == True:
            self.message_5 = "enable_master_reset_code: set   "
        else:
            self.message_5 = ""

    def checked_box_6(self): 
        if self.checkBox_6.isChecked() == True:
            self.message_6 = "enable_pair: set   "
        else:
            self.message_6 = ""

    def checked_box_7(self): 
        if self.checkBox_7.isChecked() == True:
            self.message_7 = "enable_trigger_timeout: set   "
        else:
            self.message_7 = ""

    def checked_box_8(self): 
        if self.checkBox_8.isChecked() == True:
            self.message_8 = "full_width_res: set   "
        else:
            self.message_8 = ""

    def checked_box_9(self): 
        if self.checkBox_9.isChecked() == True:
            self.message_9 = "enable_TDC_ID: set   "
        else:
            self.message_9 = ""

    def checked_box_10(self): 
        if self.checkBox_10.isChecked() == True:
            self.message_10 = "enable_direct_bunch_reset: set   "
        else:
            self.message_10 = ""

    def checked_box_11(self): 
        if self.checkBox_11.isChecked() == True:
            self.message_11 = "auto_roll_over: set   "
        else:
            self.message_11 = ""

    def checked_box_12(self): 
        if self.checkBox_12.isChecked() == True:
            self.message_12 = "Channel_data_debug: set   "
        else:
            self.message_12 = ""

    def checked_box_13(self): 
        if self.checkBox_13.isChecked() == True:
            self.message_13 = "enable_8b10b: set   "
        else:
            self.message_13 = ""

    def checked_box_14(self): 
        if self.checkBox_14.isChecked() == True:
            self.message_14 = "enable_direct_trigger: set   "
        else:
            self.message_14 = ""

    def checked_box_15(self): 
        if self.checkBox_15.isChecked() == True:
            self.message_15 = "enable_error_packet: set   "
        else:
            self.message_15 = ""

    def checked_box_16(self): 
        if self.checkBox_16.isChecked() == True:
            self.message_16 = "enable_insert: set   "
        else:
            self.message_16 = ""

    def checked_box_17(self): 
        if self.checkBox_17.isChecked() == True:
            self.message_17 = "enable_legacy: set   "
        else:
            self.message_17 = ""

    def checked_box_18(self): 
        if self.checkBox_18.isChecked() == True:
            self.message_18 = "enable_new_ttc: set   "
        else:
            self.message_18 = ""

    def checked_box_19(self): 
        if self.checkBox_19.isChecked() == True:
            self.message_19 = "enable_trigger: set   "
        else:
            self.message_19 = ""

    def checked_box_20(self): 
        if self.checkBox_20.isChecked() == True:
            self.message_20 = "enable_fake_hit: set   "
        else:
            self.message_20 = ""

    def checked_box_21(self): 
        if self.checkBox_21.isChecked() == True:
            self.message_21 = "enable_error_notify: set   "
        else:
            self.message_21 = ""


    #Functions for the line edits
    def changed_line1(self): 
        self.message_22 = "channel_enable_r: " + self.lineEdit.text() + "    "

    def changed_line2(self): 
        self.message_23 = "channel_enable_f: " + self.lineEdit_2.text() + "    "

    def changed_line3(self): 
        self.message_24 = "TDC_ID: " + self.lineEdit_3.text() + "    "

    def changed_line4(self): 
        self.message_25 = "rising_is_leading: " + self.lineEdit_4.text() + "    "

    def changed_line5(self): 
        self.message_26 = "width_select: " + self.lineEdit_5.text() + "    "



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
