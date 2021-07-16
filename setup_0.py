# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup0_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

##########   setup0 popup script ###########

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1138, 657)

        #getting the stuff from TDCreg for the larger bit variables
        self.rising_is_leading_list = list(self.TDC_inst.rising_is_leading[0])
        self.channel_enable_r_list = list(self.TDC_inst.channel_enable_r[0])
        self.channel_enable_f_list = list(self.TDC_inst.channel_enable_f[0])


        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 540, 1091, 101))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        #Apply button
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.apply_button)

        #OK button
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.OK_button)
        self.pushButton_2.clicked.connect(Dialog.reject)

        #Cancel button
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1071, 261))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        #enable_high_speed
        self.checkBox_95 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_high_speed[0] == '1':
            self.checkBox_95.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_95, 6, 1, 1, 1)

        #enable_legacy
        self.checkBox_96 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_legacy[0] == '1':
            self.checkBox_96.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_96, 0, 2, 1, 1)

        #enable_TDC_ID
        self.checkBox_89 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_TDC_ID[0] == '1':
            self.checkBox_89.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_89, 5, 2, 1, 1)

        #enable_8b10b
        self.checkBox_87 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_8b10b[0] == '1':
            self.checkBox_87.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_87, 2, 2, 1, 1)

        #channel_data_debug
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.channel_data_debug[0] == '1':
            self.checkBox_7.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_7, 1, 1, 1, 1)

        #enable_trigger
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_trigger[0] == '1':
            self.checkBox_6.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_6, 0, 1, 1, 1)


        #enable_direct_bunch_reset
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_direct_bunch_reset[0] == '1':
            self.checkBox_3.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)

        #enable_new_ttc
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_new_ttc[0] == '1':
            self.checkBox.setChecked(True)
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        #enable_insert
        self.checkBox_93 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_insert[0] == '1':
            self.checkBox_93.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_93, 3, 2, 1, 1)

        #enable_direct_trigger
        self.checkBox_92 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_direct_trigger[0] == '1':
            self.checkBox_92.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_92, 4, 0, 1, 1)

        #bypass_bcr_distribution
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.bypass_bcr_distribution[0] == '1':
            self.checkBox_5.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_5, 6, 0, 1, 1)

        #auto_roll_over
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.auto_roll_over[0] == '1':
            self.checkBox_4.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_4, 5, 0, 1, 1)

        #enable_trigger_timeout
        self.checkBox_94 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_trigger_timeout[0] == '1':
            self.checkBox_94.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_94, 5, 1, 1, 1)

        #enable_pair
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_pair[0] == '1':
            self.checkBox_9.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_9, 3, 1, 1, 1)

        #enable_leading
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_leading[0] == '1':
            self.checkBox_8.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_8, 2, 1, 1, 1)

        #enable_error_packet
        self.checkBox_88 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_error_packet[0] == '1':
            self.checkBox_88.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_88, 4, 2, 1, 1)

        #enable_fake_hit
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_fake_hit[0] == '1':
            self.checkBox_10.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_10, 4, 1, 1, 1)

        #enable_error_notify
        self.checkBox_90 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_error_notify[0] == '1':
            self.checkBox_90.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_90, 6, 2, 1, 1)

        #full_width_res
        self.checkBox_97 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.full_width_res[0] == '1':
            self.checkBox_97.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_97, 1, 2, 1, 1)

        #enable_direct_event_reset
        self.checkBox_91 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_direct_event_reset[0] == '1':
            self.checkBox_91.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_91, 3, 0, 1, 1)

        #enable_master_reset_code
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        if self.TDC_inst.enable_master_reset_code[0] == '1':
            self.checkBox_2.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)


        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 310, 1091, 141))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        #checkbox labels (0-23)
        for i in range(24):
            label_num = i + 3
            label = QtWidgets.QLabel(self.gridLayoutWidget_2)
            label.setObjectName("label_%d"%label_num)
            self.gridLayout_2.addWidget(label, 0, i+1, 1, 1)
            label.setText("%d"%i)

        #rising is leading checkboxes
        self.checkbox_list = []
        for i in range(24):
            checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
            self.gridLayout_2.addWidget(checkBox, 1, i+1, 1, 1)
            if self.rising_is_leading_list[i] == '1':
                checkBox.setChecked(True)
            self.checkbox_list.append(checkBox)

        #channel enable r checkboxes
        self.checkbox_list_2 = []
        for i in range(24):
            checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
            self.gridLayout_2.addWidget(checkBox_2, 2, i+1, 1, 1)
            if self.channel_enable_r_list[i] == '1':
                checkBox_2.setChecked(True)
            self.checkbox_list_2.append(checkBox_2)

        #channel enable f checkboxes
        self.checkbox_list_3 = []
        for i in range(24):
            checkbox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
            self.gridLayout_2.addWidget(checkbox_3, 3, i+1, 1, 1)
            if self.channel_enable_f_list[i] == '1':
                checkbox_3.setChecked(True)
            self.checkbox_list_3.append(checkbox_3)

        #channel_enable_r label
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        #rising_is_leading label
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_select = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_select.setObjectName("label_select")
        self.label_select.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.label_select, 0, 25, 1, 1)

        self.label_select_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_select_2.setObjectName("label_select_2")
        self.label_select_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.label_select_2, 0, 26, 1, 1)

        #select all - channel enable f
        self.registerButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_6, 3, 25, 1, 1)
        self.registerButton_6.clicked.connect(self.channel_enable_f_enable)

        #select all - channel enable r
        self.registerButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_7, 2, 25, 1, 1)
        self.registerButton_7.clicked.connect(self.channel_enable_r_enable)

        #select all - rising is leading
        self.registerButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_8, 1, 25, 1, 1)
        self.registerButton_8.clicked.connect(self.rising_is_leading_enable)

        #deselec all - rising is leading
        self.registerButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_9, 1, 26, 1, 1)
        self.registerButton_9.clicked.connect(self.rising_is_leading_disable)

        #deselect all - channel enable r
        self.registerButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_10, 2, 26, 1, 1)
        self.registerButton_10.clicked.connect(self.channel_enable_r_disable)

        #deselect all - channel enable f
        self.registerButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.gridLayout_2.addWidget(self.registerButton_11, 3, 26, 1, 1)
        self.registerButton_11.clicked.connect(self.channel_enable_f_disable)

        #Bottom line edit setup

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 470, 761, 80))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #TDC_ID label and line edit
        self.label_31 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout.addWidget(self.label_31)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setText(format(int(self.TDC_inst.TDC_ID[0], 2), '03X'))
        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(800, 470, 311, 80))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        #width select label and line edit
        self.label_32 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_2.addWidget(self.label_32)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setText(self.TDC_inst.width_select[0])
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setup0"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))
        self.checkBox_95.setText(_translate("Dialog", "enable_high_speed"))
        self.checkBox_96.setText(_translate("Dialog", "enable_legacy"))
        self.checkBox_89.setText(_translate("Dialog", "enable_TDC_ID"))
        self.checkBox_87.setText(_translate("Dialog", "enable_8b10b"))
        self.checkBox_7.setText(_translate("Dialog", "channel_data_debug"))
        self.checkBox_6.setText(_translate("Dialog", "enable_trigger"))
        self.checkBox_3.setText(_translate("Dialog", "enable_direct_bunch_reset"))
        self.checkBox.setText(_translate("Dialog", "enable_new_ttc"))
        self.checkBox_93.setText(_translate("Dialog", "enable_insert"))
        self.checkBox_92.setText(_translate("Dialog", "enable_direct_trigger"))
        self.checkBox_5.setText(_translate("Dialog", "bypass_bcr_distribution"))
        self.checkBox_4.setText(_translate("Dialog", "auto_roll_over"))
        self.checkBox_94.setText(_translate("Dialog", "enable_trigger_timeout"))
        self.checkBox_9.setText(_translate("Dialog", "enable_pair"))
        self.checkBox_8.setText(_translate("Dialog", "enable_leading"))
        self.checkBox_88.setText(_translate("Dialog", "enable_error_packet"))
        self.checkBox_10.setText(_translate("Dialog", "enable_fake_hit"))
        self.checkBox_90.setText(_translate("Dialog", "enable_error_notify"))
        self.checkBox_97.setText(_translate("Dialog", "full_width_res"))
        self.checkBox_91.setText(_translate("Dialog", "enable_direct_event_reset"))
        self.checkBox_2.setText(_translate("Dialog", "enable_master_reset_code"))
        self.label_29.setText(_translate("Dialog", "channel_enable_r:"))
        self.label_30.setText(_translate("Dialog", "channel_enable_f:"))
        self.label_31.setText(_translate("Dialog", "TDC_ID:"))
        self.label_32.setText(_translate("Dialog", "Width_select:"))
        self.label_2.setText(_translate("Dialog", "Channel Options: "))
        self.label.setText(_translate("Dialog", "rising_is_leading:"))
        self.registerButton_6.setText(_translate("Dialog", "enable f"))
        self.registerButton_7.setText(_translate("Dialog", "enable r"))
        self.registerButton_8.setText(_translate("Dialog", "rising is leading"))
        self.registerButton_9.setText(_translate("Dialog", "rising is leading"))
        self.registerButton_10.setText(_translate("Dialog", "enable r"))
        self.registerButton_11.setText(_translate("Dialog", "enable f"))
        self.label_select.setText(_translate("Dialog", "Select All:"))
        self.label_select_2.setText(_translate("Dialog", "Deselect All:"))

    #General function stuff - for viewing, not setting them officially

    #rising is leading
    #enable all
    def rising_is_leading_enable(self):
        for i in self.checkbox_list:
            i.setChecked(True)

    #disable all
    def rising_is_leading_disable(self):
        for i in self.checkbox_list:
            i.setChecked(False)

    #channel_enable_r
    #enable all
    def channel_enable_r_enable(self):
        for i in self.checkbox_list_2:
            i.setChecked(True)

    # disable all
    def channel_enable_r_disable(self):
        for i in self.checkbox_list_2:
            i.setChecked(False)

    #channel_enable_f
    #enable all
    def channel_enable_f_enable(self):
        for i in self.checkbox_list_3:
            i.setChecked(True)

    # disable all
    def channel_enable_f_disable(self):
        for i in self.checkbox_list_3:
            i.setChecked(False)

    #Functions for officially saving new setup
    #apply button
    def apply_button(self):
        self.save()

    #Ok button
    def OK_button(self):
        self.save()

    #save all changes
    def save(self):

        #enable_new_ttc
        if self.checkBox.isChecked() == True:
            self.TDC_inst.enable_new_ttc[0] = '1'
        else:
            self.TDC_inst.enable_new_ttc[0] = '0'
        self.enable_new_ttc_message = "enable_new_ttc: " + self.TDC_inst.enable_new_ttc[0] + " "

        #enable_master_reset_code
        if self.checkBox_2.isChecked() == True:
            self.TDC_inst.enable_master_reset_code[0] = '1'
        else:
            self.TDC_inst.enable_master_reset_code[0] = '0'

        #enable_direct_bunch_reset
        if self.checkBox_3.isChecked() == True:
            self.TDC_inst.enable_direct_bunch_reset[0] = '1'
        else:
            self.TDC_inst.enable_direct_bunch_reset[0] = '0'

        #enable_direct_event_reset
        if self.checkBox_91.isChecked() == True:
            self.TDC_inst.enable_direct_event_reset[0] = '1'
        else:
            self.TDC_inst.enable_direct_event_reset[0] = '0'

        #enable_direct_trigger
        if self.checkBox_92.isChecked() == True:
            self.TDC_inst.enable_direct_trigger[0] = '1'
        else:
            self.TDC_inst.enable_direct_trigger[0] = '0'

        #auto_roll_over
        if self.checkBox_4.isChecked() == True:
            self.TDC_inst.auto_roll_over[0] = '1'
        else:
            self.TDC_inst.auto_roll_over[0] = '0'
        self.auto_roll_over_message = "auto_roll_over: " + self.TDC_inst.auto_roll_over[0] + "  "

        #bypass_bcr_distribution
        if self.checkBox_5.isChecked() == True:
            self.TDC_inst.bypass_bcr_distribution[0] = '1'
        else:
            self.TDC_inst.bypass_bcr_distribution[0] = '0'

        #enable_trigger
        if self.checkBox_6.isChecked() == True:
            self.TDC_inst.enable_trigger[0] = '1'
        else:
            self.TDC_inst.enable_trigger[0] = '0'

        #channel_data_debug
        if self.checkBox_7.isChecked() == True:
            self.TDC_inst.channel_data_debug[0] = '1'
        else:
            self.TDC_inst.channel_data_debug[0] = '0'

        #enable_leading
        if self.checkBox_8.isChecked() == True:
            self.TDC_inst.enable_leading[0] = '1'
        else:
            self.TDC_inst.enable_leading[0] = '0'

        #enable_pair
        if self.checkBox_9.isChecked() == True:
            self.TDC_inst.enable_pair[0] = '1'
        else:
            self.TDC_inst.enable_pair[0] = '0'
        self.enable_pair_message = "enable_pair: " + self.TDC_inst.enable_pair[0] + "  "

        #enable_fake_hit
        if self.checkBox_10.isChecked() == True:
            self.TDC_inst.enable_fake_hit[0] = '1'
        else:
            self.TDC_inst.enable_fake_hit[0] = '0'

        #rising_is_leading
        #individual channel enable
        for i in self.checkbox_list:
            index = self.checkbox_list.index(i)
            if i.isChecked() == True:
                self.rising_is_leading_list[index] = '1'
            else:
                self.rising_is_leading_list[index] = '0'

        #saving the values to TDCreg
        self.TDC_inst.rising_is_leading[0] = ''.join(self.rising_is_leading_list)

        #channel_enable_r
        #individual channel enable
        for i in self.checkbox_list_2:
            index = self.checkbox_list_2.index(i)
            if i.isChecked() == True:
                self.channel_enable_r_list[index] = '1'
            else:
                self.channel_enable_r_list[index] = '0'

        self.TDC_inst.channel_enable_r[0] = ''.join(self.channel_enable_r_list)

        #channel_enable_f
        for i in self.checkbox_list_3:
            index = self.checkbox_list_3.index(i)
            if i.isChecked() == True:
                self.channel_enable_f_list[index] = '1'
            else:
                self.channel_enable_f_list[index] = '0'

        self.TDC_inst.channel_enable_f[0] = ''.join(self.channel_enable_f_list)

        #TDC_ID
        self.lineEdit_binary = format(int(self.lineEdit.text(), 16), '010b')
        self.TDC_inst.TDC_ID[0] = self.lineEdit_binary
        self.messages = self.lineEdit_binary

        #enable_trigger_timeout
        if self.checkBox_94.isChecked() == True:
            self.TDC_inst.enable_trigger_timeout[0] = '1'
        else:
            self.TDC_inst.enable_trigger_timeout[0] = '0'

        #enable_high_speed
        if self.checkBox_95.isChecked() == True:
            self.TDC_inst.enable_high_speed[0] = '1'
        else:
            self.TDC_inst.enable_high_speed[0] = '0'

        #enable_legacy
        if self.checkBox_96.isChecked() == True:
            self.TDC_inst.enable_legacy[0] = '1'
        else:
            self.TDC_inst.enable_legacy[0] = '0'

        #full_width_res
        if self.checkBox_97.isChecked() == True:
            self.TDC_inst.full_width_res[0] = '1'
        else:
            self.TDC_inst.full_width_res[0] = '0'

        #width_select
        self.TDC_inst.width_select[0] = self.lineEdit_2.text()

        #enable_8b10b
        if self.checkBox_87.isChecked() == True:
            self.TDC_inst.enable_8b10b[0] = '1'
        else:
            self.TDC_inst.enable_8b10b[0] = '0'

        #enable_insert
        if self.checkBox_93.isChecked() == True:
            self.TDC_inst.enable_insert[0] = '1'
        else:
            self.TDC_inst.enable_insert[0] = '0'

        #enable_error_packet
        if self.checkBox_88.isChecked() == True:
            self.TDC_inst.enable_error_packet[0] = '1'
        else:
            self.TDC_inst.enable_error_packet[0] = '0'

        #enable_TDC_ID
        if self.checkBox_89.isChecked() == True:
            self.TDC_inst.enable_TDC_ID[0] = '1'
        else:
            self.TDC_inst.enable_TDC_ID[0] = '0'

        #enable_error_notify
        if self.checkBox_90.isChecked() == True:
            self.TDC_inst.enable_error_notify[0] = '1'
        else:
            self.TDC_inst.enable_error_notify[0] = '0'

        # calling update_setup_0 function
        self.TDC_inst.update_setup_0()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
