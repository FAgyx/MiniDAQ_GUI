from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from LpGBT_functions__two_change_setup import *


class Ui_Dialog(object):
    plop = 3

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 761)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 560, 611))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.clocks = 4
        row = 0
        column = 0

        for i in range(self.clocks):
            if column == 6:
                column = 0
                row += 9

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setText("PS%i" % i)
            self.gridLayout.addWidget(self.label, row, column, 1, 1)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setText("Frequency")
            self.gridLayout.addWidget(self.label_5, row + 1, column, 1, 1)

            self.combobox = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox.addItem("disabled")
            self.combobox.addItem("40")
            self.combobox.addItem("80")
            self.combobox.addItem("160")
            self.combobox.addItem("320")
            self.combobox.addItem("640")
            self.combobox.addItem("1280")
            self.gridLayout.addWidget(self.combobox, row + 1, column + 1, 1, 1)

            self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_3.setText("Fine Tune")
            self.gridLayout.addWidget(self.label_3, row + 2, column, 1, 1)

            self.checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.gridLayout.addWidget(self.checkbox, row + 2, column + 1, 1, 1)

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setText("Delay")
            self.gridLayout.addWidget(self.label_2, row + 3, column, 1, 1)

            self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
            self.lineEdit.setText('00000000')
            self.gridLayout.addWidget(self.lineEdit, row + 3, column + 1, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setText("Drive Strength")
            self.gridLayout.addWidget(self.label_4, row + 4, column, 1, 1)

            self.combobox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox_2.addItem("0")
            self.combobox_2.addItem("1.0")
            self.combobox_2.addItem("1.5")
            self.combobox_2.addItem("2.0")
            self.combobox_2.addItem("2.5")
            self.combobox_2.addItem("3.0")
            self.combobox_2.addItem("3.5")
            self.combobox_2.addItem("4.0")
            self.gridLayout.addWidget(self.combobox_2, row + 4, column + 1, 1, 1)

            self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_6.setText("PE Strength")
            self.gridLayout.addWidget(self.label_6, row + 5, column, 1, 1)

            self.combobox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox_3.addItem("0")
            self.combobox_3.addItem("1.0")
            self.combobox_3.addItem("1.5")
            self.combobox_3.addItem("2.0")
            self.combobox_3.addItem("2.5")
            self.combobox_3.addItem("3.0")
            self.combobox_3.addItem("3.5")
            self.combobox_3.addItem("4.0")
            self.gridLayout.addWidget(self.combobox_3, row + 5, column + 1, 1, 1)

            self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_7.setText("PE Mode")
            self.gridLayout.addWidget(self.label_7, row + 6, column, 1, 1)

            self.combobox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox_4.addItem("disabled")
            self.combobox_4.addItem("disabled")
            self.combobox_4.addItem("self timed")
            self.combobox_4.addItem("clock timed")
            self.gridLayout.addWidget(self.combobox_4, row + 6, column + 1, 1, 1)

            self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_8.setText("PE Width")
            self.gridLayout.addWidget(self.label_8, row + 7, column, 1, 1)

            self.combobox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox_5.addItem("120")
            self.combobox_5.addItem("240")
            self.combobox_5.addItem("360")
            self.combobox_5.addItem("480")
            self.combobox_5.addItem("600")
            self.combobox_5.addItem("720")
            self.combobox_5.addItem("840")
            self.combobox_5.addItem("960")
            self.gridLayout.addWidget(self.combobox_5, row + 7, column + 1, 1, 1)

            self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_9.setText("  ")
            self.gridLayout.addWidget(self.label_9, row + 8, column, 1, 1)

            self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_10.setText("    ")
            self.gridLayout.addWidget(self.label_10, row + 6, column + 2, 1, 1)

            column += 3

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 660, 521, 80))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Apply
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setText("Apply")
        self.horizontalLayout.addWidget(self.pushButton)

        #OK
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setText("OK")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)

        #Cancel
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setText("Cancel")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

    def save(self):
        self.PSCLK = 5
        self.clocks = 4
        row = 0
        column = 0

        delay_val = 0
        fine_tune_val = 1
        DS_val = 2
        freq_val = 3
        PE_strength_val = 4
        PE_mode_val = 5
        PE_width_val = 6

        self.freq_data = []
        self.fine_tune_data = []
        self.delay_data = []
        self.DS_data = []
        self.PE_strength_data = []
        self.PE_mode_data = []
        self.PE_width_data = []

        for i in range(self.clocks):
            if column == 6:
                column = 0
                row += 9

            freq_box = self.gridLayout.itemAtPosition(row + 1, column + 1).widget()
            self.freq_data.append([self.PSCLK, i, freq_val, freq_box.currentIndex()])

            fine_tune_box = self.gridLayout.itemAtPosition(row + 2, column + 1).widget()
            if fine_tune_box.isChecked():
                self.fine_tune_data.append([self.PSCLK, i, fine_tune_val, '1'])
            else:
                self.fine_tune_data.append([self.PSCLK, i, fine_tune_val, '0'])

            delay_box = self.gridLayout.itemAtPosition(row + 3, column + 1).widget()
            self.delay_data.append([self.PSCLK, i, delay_val, delay_box.text()])

            drive_strength_box = self.gridLayout.itemAtPosition(row + 4, column + 1).widget()
            self.DS_data.append([self.PSCLK, i, DS_val, drive_strength_box.currentIndex()])

            PE_strength_box = self.gridLayout.itemAtPosition(row + 5, column + 1).widget()
            self.PE_strength_data.append([self.PSCLK, i, PE_strength_val, PE_strength_box.currentIndex()])

            PE_mode_box = self.gridLayout.itemAtPosition(row + 6 , column + 1).widget()
            self.PE_mode_data.append([self.PSCLK, i, PE_mode_val, PE_mode_box.currentIndex()])

            PE_width_box = self.gridLayout.itemAtPosition(row + 7, column + 1).widget()
            self.PE_width_data.append([self.PSCLK, i, PE_width_val, PE_width_box.currentIndex()])

            column += 3

        for freq, fine_tune, delay, DS, PE_S, PE_m, PE_w in zip(self.freq_data, self.fine_tune_data, self.delay_data,
                                                                self.DS_data, self.PE_strength_data, self.PE_mode_data,
                                                                self.PE_width_data):
            function(delay[0], delay[1], delay[2], delay[3])
            function(fine_tune[0], fine_tune[1], fine_tune[2], fine_tune[3])
            function(DS[0], DS[1], DS[2], DS[3])
            function(freq[0], freq[1], freq[2], freq[3])

            function(PE_S[0], PE_S[1], PE_S[2], PE_S[3])
            function(PE_m[0], PE_m[1], PE_m[2], PE_m[3])
            function(PE_w[0], PE_w[1], PE_w[2], PE_w[3])
            print("clock done")

        # print(add_and_reg)
        # print(sorted(add_and_reg, key=itemgetter(0)))
        post_function()


    #     ############# xml file loading ####################
    #     # Fine Tune
    #     PS_FineTune_List = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]
    #     i = 0
    #     for PS_FineTune in PS_FineTune_List:
    #         if root[5][i][0].text == '0x1':
    #             PS_FineTune.setChecked(True)
    #         else:
    #             PS_FineTune.setChecked(False)
    #         i += 1
    #
    #     # Frequency
    #     PS_Freq_list = [self.comboBox, self.comboBox_6, self.comboBox_11, self.comboBox_16]
    #     i = 0
    #     for PS_Freq in PS_Freq_list:
    #         if root[5][i][1].text == '0x0':
    #             PS_Freq.setCurrentIndex(0)
    #         if root[5][i][1].text == '0x1':
    #             PS_Freq.setCurrentIndex(1)
    #         if root[5][i][1].text == '0x2':
    #             PS_Freq.setCurrentIndex(2)
    #         if root[5][i][1].text == '0x3':
    #             PS_Freq.setCurrentIndex(3)
    #         if root[5][i][1].text == '0x4':
    #             PS_Freq.setCurrentIndex(4)
    #         if root[5][i][1].text == '0x5':
    #             PS_Freq.setCurrentIndex(5)
    #         if root[5][i][1].text == '0x6':
    #             PS_Freq.setCurrentIndex(6)
    #         i += 1
    #
    #     # Delay (come back to!)
    #     ### This is the one where ther are issues
    #     ##with figuiring out how to fill with a text box thing
    #     self.lineEdit.setText(root[5][0][2].text)
    #     self.lineEdit_2.setText(root[5][1][2].text)
    #     self.lineEdit_3.setText(root[5][2][2].text)
    #     self.lineEdit_4.setText(root[5][3][2].text)
    #
    #     # PE Strength
    #     PE_strength_list = [self.comboBox_2, self.comboBox_7, self.comboBox_12, self.comboBox_17]
    #     i = 0
    #     for PE_strength in PE_strength_list:
    #         if root[5][i][3].text == '0x0':
    #             PE_strength.setCurrentIndex(0)
    #         if root[5][i][3].text == '0x1':
    #             PE_strength.setCurrentIndex(1)
    #         if root[5][i][3].text == '0x2':
    #             PE_strength.setCurrentIndex(2)
    #         if root[5][i][3].text == '0x3':
    #             PE_strength.setCurrentIndex(3)
    #         if root[5][i][3].text == '0x4':
    #             PE_strength.setCurrentIndex(4)
    #         if root[5][i][3].text == '0x5':
    #             PE_strength.setCurrentIndex(5)
    #         if root[5][i][3].text == '0x6':
    #             PE_strength.setCurrentIndex(6)
    #         if root[5][i][3].text == '0x7':
    #             PE_strength.setCurrentIndex(7)
    #         i += 1
    #
    #     # PE Mode
    #     PE_Mode_list = [self.comboBox_3, self.comboBox_8, self.comboBox_13, self.comboBox_18]
    #     i = 0
    #     for PE_Mode in PE_Mode_list:
    #         if root[5][i][4].text == '0x0':
    #             PE_Mode.setCurrentIndex(0)
    #         if root[5][i][4].text == '0x2':
    #             PE_Mode.setCurrentIndex(1)
    #         if root[5][i][4].text == '0x3':
    #             PE_Mode.setCurrentIndex(2)
    #         i += 1
    #
    #     # PE_width
    #     PE_width_list = [self.comboBox_4, self.comboBox_9, self.comboBox_14, self.comboBox_19]
    #     i = 0
    #     for PE_width in PE_width_list:
    #         if root[5][i][5].text == '0x0':
    #             PE_width.setCurrentIndex(0)
    #         if root[5][i][5].text == '0x1':
    #             PE_width.setCurrentIndex(1)
    #         if root[5][i][5].text == '0x2':
    #             PE_width.setCurrentIndex(2)
    #         if root[5][i][5].text == '0x3':
    #             PE_width.setCurrentIndex(3)
    #         if root[5][i][5].text == '0x4':
    #             PE_width.setCurrentIndex(4)
    #         if root[5][i][5].text == '0x5':
    #             PE_width.setCurrentIndex(5)
    #         if root[5][i][5].text == '0x6':
    #             PE_width.setCurrentIndex(6)
    #         if root[5][i][5].text == '0x7':
    #             PE_width.setCurrentIndex(7)
    #         i += 1
    #
    #     # Drive strength
    #     Drive_strength_list = [self.comboBox_5, self.comboBox_10, self.comboBox_15, self.comboBox_20]
    #     i = 0
    #     for Drive_strength in Drive_strength_list:
    #         if root[5][i][6].text == '0x0':
    #             Drive_strength.setCurrentIndex(0)
    #         if root[5][i][6].text == '0x1':
    #             Drive_strength.setCurrentIndex(1)
    #         if root[5][i][6].text == '0x2':
    #             Drive_strength.setCurrentIndex(2)
    #         if root[5][i][6].text == '0x3':
    #             Drive_strength.setCurrentIndex(3)
    #         if root[5][i][6].text == '0x4':
    #             Drive_strength.setCurrentIndex(4)
    #         if root[5][i][6].text == '0x5':
    #             Drive_strength.setCurrentIndex(5)
    #         if root[5][i][6].text == '0x6':
    #             Drive_strength.setCurrentIndex(6)
    #         if root[5][i][6].text == '0x7':
    #             Drive_strength.setCurrentIndex(7)
    #         i += 1
    #
    #     ###################################################
    #
    #     self.retranslateUi(Dialog)
    #     QtCore.QMetaObject.connectSlotsByName(Dialog)
    #
    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    #     self.label.setText(_translate("Dialog", "PS0 "))
    #     self.label_4.setText(_translate("Dialog", "Delay"))
    #     self.label_3.setText(_translate("Dialog", "Frequency "))
    #     self.label_2.setText(_translate("Dialog", "Fine Tune"))
    #     self.label_5.setText(_translate("Dialog", "PE Strength"))
    #     self.label_6.setText(_translate("Dialog", "PE Mode"))
    #     self.comboBox.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox.setItemText(1, _translate("Dialog", "40"))
    #     self.comboBox.setItemText(2, _translate("Dialog", "80"))
    #     self.comboBox.setItemText(3, _translate("Dialog", "160"))
    #     self.comboBox.setItemText(4, _translate("Dialog", "320"))
    #     self.comboBox.setItemText(5, _translate("Dialog", "640"))
    #     self.comboBox.setItemText(6, _translate("Dialog", "1280"))
    #     self.label_7.setText(_translate("Dialog", "PE Width"))
    #     self.label_8.setText(_translate("Dialog", "Drive Strength"))
    #     self.comboBox_2.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_2.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_2.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_2.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_2.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_2.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_2.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_2.setItemText(7, _translate("Dialog", "4.0"))
    #     self.comboBox_3.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_3.setItemText(1, _translate("Dialog", "self timed"))
    #     self.comboBox_3.setItemText(2, _translate("Dialog", "clock timed"))
    #     self.comboBox_4.setItemText(0, _translate("Dialog", "120"))
    #     self.comboBox_4.setItemText(1, _translate("Dialog", "240"))
    #     self.comboBox_4.setItemText(2, _translate("Dialog", "360"))
    #     self.comboBox_4.setItemText(3, _translate("Dialog", "480"))
    #     self.comboBox_4.setItemText(4, _translate("Dialog", "600"))
    #     self.comboBox_4.setItemText(5, _translate("Dialog", "720"))
    #     self.comboBox_4.setItemText(6, _translate("Dialog", "840"))
    #     self.comboBox_4.setItemText(7, _translate("Dialog", "960"))
    #     self.comboBox_5.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_5.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_5.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_5.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_5.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_5.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_5.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_5.setItemText(7, _translate("Dialog", "4.0"))
    #     self.pushButton.setText(_translate("Dialog", "Apply"))
    #     self.pushButton_2.setText(_translate("Dialog", "OK"))
    #     self.pushButton_3.setText(_translate("Dialog", "Cancel"))
    #     self.label_9.setText(_translate("Dialog", "PS1"))
    #     self.label_10.setText(_translate("Dialog", "Delay"))
    #     self.label_11.setText(_translate("Dialog", "Frequency "))
    #     self.label_12.setText(_translate("Dialog", "Fine Tune"))
    #     self.label_13.setText(_translate("Dialog", "PE Strength"))
    #     self.label_14.setText(_translate("Dialog", "PE Mode"))
    #     self.comboBox_6.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_6.setItemText(1, _translate("Dialog", "40"))
    #     self.comboBox_6.setItemText(2, _translate("Dialog", "80"))
    #     self.comboBox_6.setItemText(3, _translate("Dialog", "160"))
    #     self.comboBox_6.setItemText(4, _translate("Dialog", "320"))
    #     self.comboBox_6.setItemText(5, _translate("Dialog", "640"))
    #     self.comboBox_6.setItemText(6, _translate("Dialog", "1280"))
    #     self.label_15.setText(_translate("Dialog", "PE Width"))
    #     self.label_16.setText(_translate("Dialog", "Drive Strength"))
    #     self.comboBox_7.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_7.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_7.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_7.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_7.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_7.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_7.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_7.setItemText(7, _translate("Dialog", "4.0"))
    #     self.comboBox_8.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_8.setItemText(1, _translate("Dialog", "self timed"))
    #     self.comboBox_8.setItemText(2, _translate("Dialog", "clock timed"))
    #     self.comboBox_9.setItemText(0, _translate("Dialog", "120"))
    #     self.comboBox_9.setItemText(1, _translate("Dialog", "240"))
    #     self.comboBox_9.setItemText(2, _translate("Dialog", "360"))
    #     self.comboBox_9.setItemText(3, _translate("Dialog", "480"))
    #     self.comboBox_9.setItemText(4, _translate("Dialog", "600"))
    #     self.comboBox_9.setItemText(5, _translate("Dialog", "720"))
    #     self.comboBox_9.setItemText(6, _translate("Dialog", "840"))
    #     self.comboBox_9.setItemText(7, _translate("Dialog", "960"))
    #     self.comboBox_10.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_10.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_10.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_10.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_10.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_10.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_10.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_10.setItemText(7, _translate("Dialog", "4.0"))
    #     self.label_17.setText(_translate("Dialog", "PS2"))
    #     self.label_18.setText(_translate("Dialog", "Delay"))
    #     self.label_19.setText(_translate("Dialog", "Frequency "))
    #     self.label_20.setText(_translate("Dialog", "Fine Tune"))
    #     self.label_21.setText(_translate("Dialog", "PE Strength"))
    #     self.label_22.setText(_translate("Dialog", "PE Mode"))
    #     self.comboBox_11.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_11.setItemText(1, _translate("Dialog", "40"))
    #     self.comboBox_11.setItemText(2, _translate("Dialog", "80"))
    #     self.comboBox_11.setItemText(3, _translate("Dialog", "160"))
    #     self.comboBox_11.setItemText(4, _translate("Dialog", "320"))
    #     self.comboBox_11.setItemText(5, _translate("Dialog", "640"))
    #     self.comboBox_11.setItemText(6, _translate("Dialog", "1280"))
    #     self.label_23.setText(_translate("Dialog", "PE Width"))
    #     self.label_24.setText(_translate("Dialog", "Drive Strength"))
    #     self.comboBox_12.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_12.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_12.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_12.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_12.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_12.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_12.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_12.setItemText(7, _translate("Dialog", "4.0"))
    #     self.comboBox_13.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_13.setItemText(1, _translate("Dialog", "self timed"))
    #     self.comboBox_13.setItemText(2, _translate("Dialog", "clock timed"))
    #     self.comboBox_14.setItemText(0, _translate("Dialog", "120"))
    #     self.comboBox_14.setItemText(1, _translate("Dialog", "240"))
    #     self.comboBox_14.setItemText(2, _translate("Dialog", "360"))
    #     self.comboBox_14.setItemText(3, _translate("Dialog", "480"))
    #     self.comboBox_14.setItemText(4, _translate("Dialog", "600"))
    #     self.comboBox_14.setItemText(5, _translate("Dialog", "720"))
    #     self.comboBox_14.setItemText(6, _translate("Dialog", "840"))
    #     self.comboBox_14.setItemText(7, _translate("Dialog", "960"))
    #     self.comboBox_15.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_15.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_15.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_15.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_15.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_15.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_15.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_15.setItemText(7, _translate("Dialog", "4.0"))
    #     self.label_25.setText(_translate("Dialog", "PS3"))
    #     self.label_26.setText(_translate("Dialog", "Delay"))
    #     self.label_27.setText(_translate("Dialog", "Frequency "))
    #     self.label_28.setText(_translate("Dialog", "Fine Tune"))
    #     self.label_29.setText(_translate("Dialog", "PE Strength"))
    #     self.label_30.setText(_translate("Dialog", "PE Mode"))
    #     self.comboBox_16.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_16.setItemText(1, _translate("Dialog", "40"))
    #     self.comboBox_16.setItemText(2, _translate("Dialog", "80"))
    #     self.comboBox_16.setItemText(3, _translate("Dialog", "160"))
    #     self.comboBox_16.setItemText(4, _translate("Dialog", "320"))
    #     self.comboBox_16.setItemText(5, _translate("Dialog", "640"))
    #     self.comboBox_16.setItemText(6, _translate("Dialog", "1280"))
    #     self.label_31.setText(_translate("Dialog", "PE Width"))
    #     self.label_32.setText(_translate("Dialog", "Drive Strength"))
    #     self.comboBox_17.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_17.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_17.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_17.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_17.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_17.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_17.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_17.setItemText(7, _translate("Dialog", "4.0"))
    #     self.comboBox_18.setItemText(0, _translate("Dialog", "disabled"))
    #     self.comboBox_18.setItemText(1, _translate("Dialog", "self timed"))
    #     self.comboBox_18.setItemText(2, _translate("Dialog", "clock timed"))
    #     self.comboBox_19.setItemText(0, _translate("Dialog", "120"))
    #     self.comboBox_19.setItemText(1, _translate("Dialog", "240"))
    #     self.comboBox_19.setItemText(2, _translate("Dialog", "360"))
    #     self.comboBox_19.setItemText(3, _translate("Dialog", "480"))
    #     self.comboBox_19.setItemText(4, _translate("Dialog", "600"))
    #     self.comboBox_19.setItemText(5, _translate("Dialog", "720"))
    #     self.comboBox_19.setItemText(6, _translate("Dialog", "840"))
    #     self.comboBox_19.setItemText(7, _translate("Dialog", "960"))
    #     self.comboBox_20.setItemText(0, _translate("Dialog", "0"))
    #     self.comboBox_20.setItemText(1, _translate("Dialog", "1.0"))
    #     self.comboBox_20.setItemText(2, _translate("Dialog", "1.5"))
    #     self.comboBox_20.setItemText(3, _translate("Dialog", "2.0"))
    #     self.comboBox_20.setItemText(4, _translate("Dialog", "2.5"))
    #     self.comboBox_20.setItemText(5, _translate("Dialog", "3.0"))
    #     self.comboBox_20.setItemText(6, _translate("Dialog", "3.5"))
    #     self.comboBox_20.setItemText(7, _translate("Dialog", "4.0"))
    #
    # def save(self):
    #     print("in progress")
    #     import xml.etree.ElementTree as ET
    #     # tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
    #     tree_ePortTX = ET.parse('LpGBT_transfer.xml')
    #     root = tree_ePortTX.getroot()
    #
    #     #Fine Tune
    #     PS_FineTune_List = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4]
    #     i = 0
    #     for PS_FineTune in PS_FineTune_List:
    #         if PS_FineTune.isChecked() == True:
    #             root[5][i][0].text = '0x1'
    #         else:
    #             root[5][i][0].text = '0x0'
    #         i += 1
    #
    #     #Frequency
    #     PS_Freq_list = [self.comboBox, self.comboBox_6, self.comboBox_11, self.comboBox_16]
    #     i = 0
    #     for PS_Freq in PS_Freq_list:
    #         #PS_Freq.setCurrentIndex(3)
    #         if PS_Freq.currentIndex() == 0:
    #             root[5][i][1].text = '0x0'
    #         if PS_Freq.currentIndex() == 1:
    #             root[5][i][1].text = '0x1'
    #         if PS_Freq.currentIndex() == 2:
    #             root[5][i][1].text = '0x2'
    #         if PS_Freq.currentIndex() == 3:
    #             root[5][i][1].text = '0x3'
    #         if PS_Freq.currentIndex() == 4:
    #             root[5][i][1].text = '0x4'
    #         if PS_Freq.currentIndex() == 5:
    #             root[5][i][1].text = '0x5'
    #         if PS_Freq.currentIndex() == 6:
    #             root[5][i][1].text = '0x6'
    #         i += 1
    #
    #     #Delay (come back to!)
    #     ### This is the one where ther are issues
    #     ##with figuiring out what's the thing that needs to fill this/what gets read into the function!
    #     root[5][0][2].text = self.lineEdit.text()
    #     root[5][1][2].text = self.lineEdit_2.text()
    #     root[5][2][2].text = self.lineEdit_3.text()
    #     root[5][3][2].text = self.lineEdit_4.text()
    #
    #     #PE Strength
    #     PE_strength_list = [self.comboBox_2, self.comboBox_7, self.comboBox_12, self.comboBox_17]
    #     i = 0
    #     for PE_strength in PE_strength_list:
    #         if PE_strength.currentIndex() == 0:
    #             root[5][i][3].text = '0x0'
    #         if PE_strength.currentIndex() == 1:
    #             root[5][i][3].text = '0x1'
    #         if PE_strength.currentIndex() == 2:
    #             root[5][i][3].text = '0x2'
    #         if PE_strength.currentIndex() == 3:
    #             root[5][i][3].text = '0x3'
    #         if PE_strength.currentIndex() == 4:
    #             root[5][i][3].text = '0x4'
    #         if PE_strength.currentIndex() == 5:
    #             root[5][i][3].text = '0x5'
    #         if PE_strength.currentIndex() == 6:
    #             root[5][i][3].text = '0x6'
    #         if PE_strength.currentIndex() == 7:
    #             root[5][i][3].text = '0x7'
    #         i += 1
    #
    #     #PE Mode
    #     PE_Mode_list = [self.comboBox_3, self.comboBox_8, self.comboBox_13, self.comboBox_18]
    #     i = 0
    #     for PE_Mode in PE_Mode_list:
    #         if PE_Mode.currentIndex() == 0:
    #             root[5][i][4].text = '0x0'
    #         if PE_Mode.currentIndex() == 1:
    #             root[5][i][4].text = '0x2'
    #         if PE_Mode.currentIndex() == 2:
    #             root[5][i][4].text = '0x3'
    #         i += 1
    #
    #     #PE_width
    #     PE_width_list = [self.comboBox_4, self.comboBox_9, self.comboBox_14, self.comboBox_19]
    #     i = 0
    #     for PE_width in PE_width_list:
    #         if PE_width.currentIndex() == 0:
    #             root[5][i][5].text = '0x0'
    #         if PE_width.currentIndex() == 1:
    #             root[5][i][5].text = '0x1'
    #         if PE_width.currentIndex() == 2:
    #             root[5][i][5].text = '0x2'
    #         if PE_width.currentIndex() == 3:
    #             root[5][i][5].text = '0x3'
    #         if PE_width.currentIndex() == 4:
    #             root[5][i][5].text = '0x4'
    #         if PE_width.currentIndex() == 5:
    #             root[5][i][5].text = '0x5'
    #         if PE_width.currentIndex() == 6:
    #             root[5][i][5].text = '0x6'
    #         if PE_width.currentIndex() == 7:
    #             root[5][i][5].text = '0x7'
    #         i += 1
    #
    #     #Drive strength
    #     Drive_strength_list = [self.comboBox_5, self.comboBox_10, self.comboBox_15, self.comboBox_20]
    #     i = 0
    #     for Drive_strength in Drive_strength_list:
    #         if Drive_strength.currentIndex() == 0:
    #             root[5][i][6].text = '0x0'
    #         if Drive_strength.currentIndex() == 1:
    #             root[5][i][6].text = '0x1'
    #         if Drive_strength.currentIndex() == 2:
    #             root[5][i][6].text = '0x2'
    #         if Drive_strength.currentIndex() == 3:
    #             root[5][i][6].text = '0x3'
    #         if Drive_strength.currentIndex() == 4:
    #             root[5][i][6].text = '0x4'
    #         if Drive_strength.currentIndex() == 5:
    #             root[5][i][6].text = '0x5'
    #         if Drive_strength.currentIndex() == 6:
    #             root[5][i][6].text = '0x6'
    #         if Drive_strength.currentIndex() == 7:
    #             root[5][i][6].text = '0x7'
    #         i += 1
    #
    #     tree_ePortTX.write('LpGBT_auto_saved.xml')
    #     tree_ePortTX.write('LpGBT_transfer.xml')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())