import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from LpGBT_functions_two import *


class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst
        self.checkbox_list = []

    def setupUi(self, Dialog):

        Dialog.resize(1836, 910)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1800, 870))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # define parameters
        self.clocks = 29
        row = 0
        column = 0
        row_freq = 1
        column_two = 1
        EPCLK_label_width = 110
        EPCLK_label_height = 18

        for i in range(self.clocks):
            if column == 16:
                column = 0
                column_two = 1
                row += 7
                row_freq += 7

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setText("EPCLK %s" % i)
            self.label.setFont(QtGui.QFont("Calbri", 8))
            self.gridLayout.addWidget(self.label, row, column, 1, 1)

            self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_3.setText("Invert:")
            self.label_3.setFont(QtGui.QFont("Arial", 7))
            self.label_3.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_3, row_freq, column, 1, 1)

            self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.gridLayout.addWidget(self.checkBox, row_freq, column_two, 1, 1)
            # self.checkBox.stateChanged.connect(wr)
            self.checkbox_list.append(self.checkBox)

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setText("Frequency:")
            self.label_2.setFont(QtGui.QFont("Arial", 7))
            self.label_2.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_2, row_freq + 1, column, 1, 1)

            freq_box = QtWidgets.QComboBox(self.gridLayoutWidget)
            freq_box.addItem("off")
            freq_box.addItem("40")
            freq_box.addItem("80")
            freq_box.addItem("160")
            freq_box.addItem("320")
            freq_box.addItem("640")
            freq_box.addItem("1280")
            freq_box.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(freq_box, row_freq + 1, column_two, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setText("Drive Strength:")
            self.label_4.setFont(QtGui.QFont("Arial", 7))
            self.label_4.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_4, row_freq + 2, column, 1, 1)

            drive_strength = QtWidgets.QComboBox(self.gridLayoutWidget)
            drive_strength.addItem("0")
            drive_strength.addItem("1.0")
            drive_strength.addItem("1.5")
            drive_strength.addItem("2.0")
            drive_strength.addItem("2.5")
            drive_strength.addItem("3.0")
            drive_strength.addItem("3.5")
            drive_strength.addItem("4.0")
            drive_strength.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(drive_strength, row_freq + 2, column_two, 1, 1)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setText("PE strength:")
            self.label_5.setFont(QtGui.QFont("Arial", 7))
            self.label_5.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_5, row_freq + 3, column, 1, 1)

            PE_strength = QtWidgets.QComboBox(self.gridLayoutWidget)
            PE_strength.addItem("0")
            PE_strength.addItem("1.0")
            PE_strength.addItem("1.5")
            PE_strength.addItem("2.0")
            PE_strength.addItem("2.5")
            PE_strength.addItem("3.0")
            PE_strength.addItem("3.5")
            PE_strength.addItem("4.0")
            PE_strength.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(PE_strength, row_freq + 3, column_two, 1, 1)

            self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_6.setText("PE Mode:")
            self.label_6.setFont(QtGui.QFont("Arial", 7))
            self.label_6.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_6, row_freq + 4, column, 1, 1)

            PE_mode = QtWidgets.QComboBox(self.gridLayoutWidget)
            PE_mode.addItem("disabled")
            PE_mode.addItem("disabled")
            PE_mode.addItem("self timed")
            PE_mode.addItem("clock timed")
            PE_mode.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(PE_mode, row_freq + 4, column_two, 1, 1)

            self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_7.setText("PE Width:")
            self.label_7.setFont(QtGui.QFont("Arial", 7))
            self.label_7.setFixedSize(QtCore.QSize(EPCLK_label_width, EPCLK_label_height))
            self.gridLayout.addWidget(self.label_7, row_freq + 5, column, 1, 1)

            PE_width = QtWidgets.QComboBox(self.gridLayoutWidget)
            PE_width.addItem("120")
            PE_width.addItem("240")
            PE_width.addItem("360")
            PE_width.addItem("480")
            PE_width.addItem("600")
            PE_width.addItem("720")
            PE_width.addItem("840")
            PE_width.addItem("960")
            PE_width.setFont(QtGui.QFont("Arial", 7))
            self.gridLayout.addWidget(PE_width, row_freq + 5, column_two, 1, 1)

            column += 2
            column_two += 2

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1180, 700, 600, 160))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setText("Apply")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("OK")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("Cancel")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(Dialog.reject)

    def save(self):
        # define parameters
        self.clocks = 29
        self.EPCLK = 4
        invert_val = 0
        drive_strength_val = 1
        freq_val = 2
        PE_strength_val = 3
        PE_mode_val = 4
        PE_width_val = 5
        column = 0
        column_two = 1
        row_freq = 1

        # setup lists
        self.checkBox_data = []
        self.frequency_data = []
        self.drive_strength_data = []
        self.PE_strength_data = []
        self.PE_mode_data = []
        self.PE_width_data = []

        # loop over EPCLKs
        for i in range(self.clocks):
            if column == 16:
                column = 0
                column_two = 1
                row_freq += 7
            # Check Box saving
            # check_box = self.gridLayout.itemAtPosition(row_freq, column_two).widget()
            if self.checkbox_list[i].isChecked():
                self.checkBox_data.append([self.EPCLK, i, invert_val, '1'])
            else:
                self.checkBox_data.append([self.EPCLK, i, invert_val, '0'])

            # frequency saving
            freq_box = self.gridLayout.itemAtPosition(row_freq + 1, column_two).widget()
            self.frequency_data.append([self.EPCLK, i, freq_val, freq_box.currentIndex()])

            # drive strength saving
            drive_strength_box = self.gridLayout.itemAtPosition(row_freq + 2, column_two).widget()
            self.drive_strength_data.append([self.EPCLK, i, drive_strength_val, drive_strength_box.currentIndex()])

            # PE strength saving
            PE_strength_box = self.gridLayout.itemAtPosition(row_freq + 3, column_two).widget()
            self.PE_strength_data.append([self.EPCLK, i, PE_strength_val, PE_strength_box.currentIndex()])

            # PE mode saving
            PE_mode_box = self.gridLayout.itemAtPosition(row_freq + 4, column_two).widget()
            self.PE_mode_data.append([self.EPCLK, i, PE_mode_val, PE_mode_box.currentIndex()])

            # PE width saving
            PE_width_box = self.gridLayout.itemAtPosition(row_freq + 5, column_two).widget()
            self.PE_width_data.append([self.EPCLK, i, PE_width_val, PE_width_box.currentIndex()])

            column += 2
            column_two += 2

        # print("invert data: \n %s" % self.checkBox_data)
        # print("Frequency data \n %s" % self.frequency_data)
        # print("drive strength data: \n %s" % self.drive_strength_data)
        # print("PE strength data: \n %s" % self.PE_strength_data)
        # print("PE mode data: \n %s" % self.PE_mode_data)
        # print("PE width data: \n %s " % self.PE_width_data)

        for inv, freq, ds, PE_w, PE_m, PE_s in zip(self.checkBox_data, self.frequency_data, self.drive_strength_data,
                                             self.PE_width_data, self.PE_mode_data, self.PE_strength_data):
            # print(register_sub[1])
            function(inv[0], inv[1], inv[2], inv[3])
            function(ds[0], ds[1], ds[2], ds[3])
            function(freq[0], freq[1], freq[2], freq[3])

            function(PE_w[0], PE_w[1], PE_w[2], PE_w[3])
            function(PE_m[0], PE_m[1], PE_m[2], PE_m[3])
            function(PE_s[0], PE_s[1], PE_s[2], PE_s[3])

        print("EPCLK registers' addresses and values : \n %s " % add_and_reg)
        print(" END OF RUN ")
        post_function()


    # def values(self):
    #     # self.checkBox_transfer = self.checkBox_data
    #     self.ploppppp = 3
    #     print(self.ploppppp)

