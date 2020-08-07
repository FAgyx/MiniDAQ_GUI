# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASD_trying.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 567)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 611, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 9, 1, 1)
        self.pushButton.clicked.connect(self.all_channels_on)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 9, 1, 1)
        self.pushButton_2.clicked.connect(self.all_channels_off)

        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 8, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 1, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_0_mode[0] == '00':
            self.checkBox.setChecked(True)

        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_1_mode[0] == '00':
            self.checkBox_2.setChecked(True)

        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 3, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_2_mode[0] == '00':
            self.checkBox_3.setChecked(True)

        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 4, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_3_mode[0] == '00':
            self.checkBox_4.setChecked(True)

        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 5, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_4_mode[0] == '00':
            self.checkBox_5.setChecked(True)

        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 6, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_5_mode[0] == '00':
            self.checkBox_6.setChecked(True)

        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 2, 7, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_6_mode[0] == '00':
            self.checkBox_7.setChecked(True)

        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 2, 8, 1, 1)
        if self.TDC_inst.asd_mezz.ASD0.channel_7_mode[0] == '00':
            self.checkBox_8.setChecked(True)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 140, 191, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)

        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        if self.TDC_inst.asd_mezz.ASD0.chip_mode[0] == '0':
            self.comboBox.setCurrentIndex(0)
        if self.TDC_inst.asd_mezz.ASD0.chip_mode[0] == '1':
            self.comboBox.setCurrentIndex(1)

        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 210, 241, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 2, 0, 1, 1)
        self.spinbox_value = int(format(int(self.TDC_inst.asd_mezz.ASD0.main_thr[0], 2), '02d'))
        self.spinbox_value_true = int(255 - self.spinbox_value*2)
        self.spinBox.setValue(self.spinbox_value_true)

        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)
        #### tad confused about this here!!
        self.hyst_bin_rev = ''.join(reversed(str(self.TDC_inst.asd_mezz.ASD0.hyst[0])))
        self.hyst_index = int(format(int(self.hyst_bin_rev, 2), 'd'))
        self.comboBox_2.setCurrentIndex(self.hyst_index)

        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 1, 1, 1)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 310, 471, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_4, 1, 2, 1, 1)
        self.wilkthr_index = format(int(self.TDC_inst.asd_mezz.ASD0.wilk_thr[0], 2), '02d')
        self.comboBox_4.setCurrentIndex(int(self.wilkthr_index))

        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_6, 1, 4, 1, 1)
        self.deadtime_index = format(int(self.TDC_inst.asd_mezz.ASD0.deadtime[0], 2), '02d')
        self.comboBox_6.setCurrentIndex(int(self.deadtime_index))

        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.rundowncurr_index = format(int(self.TDC_inst.asd_mezz.ASD0.rundown_curr[0], 2), '02d')
        self.comboBox_5.setCurrentIndex(int(self.rundowncurr_index))

        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.intgate_index = format(int(self.TDC_inst.asd_mezz.ASD0.int_gate[0], 2), '02d')
        self.comboBox_3.setCurrentIndex(int(self.intgate_index))

        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 0, 4, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 440, 611, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #bottom buttons

        #save current ASD
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.save_single)
        self.pushButton_3.clicked.connect(Dialog.reject)

        #save all ASDs
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.save_all)
        self.pushButton_4.clicked.connect(Dialog.reject)

        #discard
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(Dialog.reject)

        self.checkBox_list = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4,
                              self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8]

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ASD0"))
        self.pushButton.setText(_translate("Dialog", "All Channels On"))
        self.label_2.setText(_translate("Dialog", "0"))
        self.pushButton_2.setText(_translate("Dialog", "All Channels Off"))
        self.label_9.setText(_translate("Dialog", "7"))
        self.label_3.setText(_translate("Dialog", "1"))
        self.label_4.setText(_translate("Dialog", "2"))
        self.label_6.setText(_translate("Dialog", "4"))
        self.label_7.setText(_translate("Dialog", "5"))
        self.label_8.setText(_translate("Dialog", "6"))
        self.label_5.setText(_translate("Dialog", "3"))
        self.label.setText(_translate("Dialog", "Channel:   "))
        self.label_10.setText(_translate("Dialog", "Chip Mode:"))
        self.comboBox.setItemText(0, _translate("Dialog", "ADC mode"))
        self.comboBox.setItemText(1, _translate("Dialog", "TOT mode"))
        self.label_11.setText(_translate("Dialog", "Main Thr (mV):"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "20"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "40"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "60"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "80"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "100"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "120"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "140"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "160"))
        self.comboBox_2.setItemText(9, _translate("Dialog", "180"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "200"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "220"))
        self.comboBox_2.setItemText(12, _translate("Dialog", "240"))
        self.comboBox_2.setItemText(13, _translate("Dialog", "260"))
        self.comboBox_2.setItemText(14, _translate("Dialog", "280"))
        self.comboBox_2.setItemText(15, _translate("Dialog", "300"))
        self.comboBox_2.setItemText(16, _translate("Dialog", "320"))
        self.label_12.setText(_translate("Dialog", "Disc1 Hyst (uA):"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "32   mV"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "64   mV"))
        self.comboBox_4.setItemText(2, _translate("Dialog", "96   mV"))
        self.comboBox_4.setItemText(3, _translate("Dialog", "128 mV"))
        self.comboBox_4.setItemText(4, _translate("Dialog", "160 mV"))
        self.comboBox_4.setItemText(5, _translate("Dialog", "192 mV"))
        self.comboBox_4.setItemText(6, _translate("Dialog", "224 mV"))
        self.comboBox_4.setItemText(7, _translate("Dialog", "256 mV"))
        self.comboBox_6.setItemText(0, _translate("Dialog", "40   ns"))
        self.comboBox_6.setItemText(1, _translate("Dialog", "150 ns"))
        self.comboBox_6.setItemText(2, _translate("Dialog", "260 ns"))
        self.comboBox_6.setItemText(3, _translate("Dialog", "370 ns"))
        self.comboBox_6.setItemText(4, _translate("Dialog", "480 ns"))
        self.comboBox_6.setItemText(5, _translate("Dialog", "590 ns"))
        self.comboBox_6.setItemText(6, _translate("Dialog", "700 ns"))
        self.comboBox_6.setItemText(7, _translate("Dialog", "810 ns"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "7.3 uA"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "6.6 uA"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "5.9 uA"))
        self.comboBox_5.setItemText(3, _translate("Dialog", "5.2 uA"))
        self.comboBox_5.setItemText(4, _translate("Dialog", "4.5 uA"))
        self.comboBox_5.setItemText(5, _translate("Dialog", "3.8 uA"))
        self.comboBox_5.setItemText(6, _translate("Dialog", "3.1 uA"))
        self.comboBox_5.setItemText(7, _translate("Dialog", "2.4 uA"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "8      ns"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "10.5 ns"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "13    ns"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "15.5 ns"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "18    ns"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "20.5 ns"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "23    ns"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "25.5 ns"))
        self.comboBox_3.setItemText(8, _translate("Dialog", "28    ns"))
        self.comboBox_3.setItemText(9, _translate("Dialog", "30.5 ns"))
        self.comboBox_3.setItemText(10, _translate("Dialog", "33    ns"))
        self.comboBox_3.setItemText(11, _translate("Dialog", "35.5 ns"))
        self.comboBox_3.setItemText(12, _translate("Dialog", "38    ns"))
        self.comboBox_3.setItemText(13, _translate("Dialog", "40.5 ns"))
        self.comboBox_3.setItemText(14, _translate("Dialog", "43    ns"))
        self.comboBox_3.setItemText(15, _translate("Dialog", "45.5 ns"))
        self.label_13.setText(_translate("Dialog", "Int. Gate:"))
        self.label_14.setText(_translate("Dialog", "Disc2 Thr:"))
        self.label_15.setText(_translate("Dialog", "Round. Curr:"))
        self.label_16.setText(_translate("Dialog", "Dead Time:"))
        self.pushButton_3.setText(_translate("Dialog", "Save Single ASD"))
        self.pushButton_4.setText(_translate("Dialog", "Save All ASDs "))
        self.pushButton_5.setText(_translate("Dialog", "Discard"))

    def all_channels_on(self):
        for box in self.checkBox_list:
            box.setChecked(True)

    def all_channels_off(self):
        for box in self.checkBox_list:
            box.setChecked(False)

    def save_single(self):

        # self.channel_list = [self.TDC_inst.asd_mezz.ASD0.channel_0_mode[0], self.TDC_inst.asd_mezz.ASD0.channel_1_mode[0],
        #                      self.TDC_inst.asd_mezz.ASD0.channel_2_mode[0], self.TDC_inst.asd_mezz.ASD0.channel_3_mode[0],
        #                      self.TDC_inst.asd_mezz.ASD0.channel_4_mode[0], self.TDC_inst.asd_mezz.ASD0.channel_5_mode[0],
        #                      self.TDC_inst.asd_mezz.ASD0.channel_6_mode[0], self.TDC_inst.asd_mezz.ASD0.channel_7_mode[0]]


        #channels
        if self.checkBox.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_0_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_0_mode[0] = '11'

        if self.checkBox_2.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_1_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_1_mode[0] = '11'

        if self.checkBox_3.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_2_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_2_mode[0] = '11'

        if self.checkBox_4.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_3_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_3_mode[0] = '11'

        if self.checkBox_5.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_4_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_4_mode[0] = '11'

        if self.checkBox_6.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_5_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_5_mode[0] = '11'

        if self.checkBox_7.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_6_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_6_mode[0] = '11'

        if self.checkBox_8.isChecked() == True:
            self.TDC_inst.asd_mezz.ASD0.channel_7_mode[0] = '00'
        else:
            self.TDC_inst.asd_mezz.ASD0.channel_7_mode[0] = '11'


        #chip_mode
        if self.comboBox.currentIndex() == 0:
            self.TDC_inst.asd_mezz.ASD0.chip_mode[0] = '0'
        else:
            self.TDC_inst.asd_mezz.ASD0.chip_mode[0] = '1'

        #hyst
        self.hyst_binary = format(self.comboBox_2.currentIndex(), '04b')
        self.hyst_binary_reversed = reversed(self.hyst_binary)
        self.hyst_binary_reversed_val = ''.join(self.hyst_binary_reversed)
        self.TDC_inst.asd_mezz.ASD0.hyst[0] = self.hyst_binary_reversed_val

        #int_gate
        self.int_gate_index = self.comboBox_3.currentIndex()
        self.int_gate_binary = format(self.int_gate_index, '04b')
        self.TDC_inst.asd_mezz.ASD0.int_gate[0] = self.int_gate_binary

        #Disc2 Thr - wilk thr
        self.wilk_thr_index = self.comboBox_4.currentIndex()
        self.wilk_thr_binary = format(self.wilk_thr_index, '03b')
        self.TDC_inst.asd_mezz.ASD0.wilk_thr[0] = self.wilk_thr_binary

        #Rund Curr
        self.round_curr_index = self.comboBox_5.currentIndex()
        self.round_curr_binary = format(self.round_curr_index, '03b')
        self.TDC_inst.asd_mezz.ASD0.rundown_curr[0] = self.round_curr_binary

        #deadtime
        self.dead_time_index = self.comboBox_6.currentIndex()
        self.dead_time_binary = format(self.dead_time_index, '03b')
        self.TDC_inst.asd_mezz.ASD0.deadtime[0] = self.dead_time_binary

        #main_thr
        self.main_thr_val = int((255 - self.spinBox.value())/2)
        self.main_thr_binary = format(self.main_thr_val, '08b')
        self.TDC_inst.asd_mezz.ASD0.main_thr[0] = self.main_thr_binary

        print('Settings saved to ASD0')

    def save_all(self):
        self.ASD_list = [self.TDC_inst.asd_mezz.ASD0, self.TDC_inst.asd_mezz.ASD1, self.TDC_inst.asd_mezz.ASD2]

        for ASD in self.ASD_list:
            if self.checkBox.isChecked() == True:
                ASD.channel_0_mode[0] = '00'
            else:
                ASD.channel_0_mode[0] = '11'

            if self.checkBox_2.isChecked() == True:
                ASD.channel_1_mode[0] = '00'
            else:
                ASD.channel_1_mode[0] = '11'

            if self.checkBox_3.isChecked() == True:
                ASD.channel_2_mode[0] = '00'
            else:
                ASD.channel_2_mode[0] = '11'

            if self.checkBox_4.isChecked() == True:
                ASD.channel_3_mode[0] = '00'
            else:
                ASD.channel_3_mode[0] = '11'

            if self.checkBox_5.isChecked() == True:
                ASD.channel_4_mode[0] = '00'
            else:
                ASD.channel_4_mode[0] = '11'

            if self.checkBox_6.isChecked() == True:
                ASD.channel_5_mode[0] = '00'
            else:
                ASD.channel_5_mode[0] = '11'

            if self.checkBox_7.isChecked() == True:
                ASD.channel_6_mode[0] = '00'
            else:
                ASD.channel_6_mode[0] = '11'

            if self.checkBox_8.isChecked() == True:
                ASD.channel_7_mode[0] = '00'
            else:
                ASD.channel_7_mode[0] = '11'

            #chip_mode
            if self.comboBox.currentIndex() == 0:
                ASD.chip_mode[0] = '0'
            else:
                ASD.chip_mode[0] = '1'

            # hyst
            self.hyst_binary = format(self.comboBox_2.currentIndex(), '04b')
            self.hyst_binary_reversed = reversed(self.hyst_binary)
            self.hyst_binary_reversed_val = ''.join(self.hyst_binary_reversed)
            ASD.hyst[0] = self.hyst_binary_reversed_val

            # int_gate
            self.int_gate_index = self.comboBox_3.currentIndex()
            self.int_gate_binary = format(self.int_gate_index, '04b')
            ASD.int_gate[0] = self.int_gate_binary

            # Disc2 Thr - wilk thr
            self.wilk_thr_index = self.comboBox_4.currentIndex()
            self.wilk_thr_binary = format(self.wilk_thr_index, '03b')
            ASD.wilk_thr[0] = self.wilk_thr_binary

            # Rund Curr
            self.round_curr_index = self.comboBox_5.currentIndex()
            self.round_curr_binary = format(self.round_curr_index, '03b')
            ASD.rundown_curr[0] = self.round_curr_binary

            # deadtime
            self.dead_time_index = self.comboBox_6.currentIndex()
            self.dead_time_binary = format(self.dead_time_index, '03b')
            ASD.deadtime[0] = self.dead_time_binary

            # main_thr
            self.main_thr_val = int((255 - self.spinBox.value()) / 2)
            self.main_thr_binary = format(self.main_thr_val, '08b')
            ASD.main_thr[0] = self.main_thr_binary

        print('Settings saved to all ASDs')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
