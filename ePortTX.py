from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from LpGBT_functions__two_change_setup import *

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.resize(1340, 890)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1320, 600))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.clocks = 4
        row = 0
        column = 0

        for i in range(self.clocks):
            if column == 16:
                column = 0
                row += 10

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setText("G%i:" %i)
            self.gridLayout.addWidget(self.label, row, column, 1, 1)

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setText("DataRate:")
            self.gridLayout.addWidget(self.label_2, row + 1, column, 1, 2)

            self.combobox = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.combobox.addItem("disabled")
            self.combobox.addItem("80 Mbps")
            self.combobox.addItem("160 Mbps")
            self.combobox.addItem("320 Mbps")
            self.gridLayout.addWidget(self.combobox, row + 1, column + 3, 1, 2)

            self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_3.setText("MirrorEnable:")
            self.gridLayout.addWidget(self.label_3, row + 2, column, 1, 2)

            self.checkbox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.gridLayout.addWidget(self.checkbox, row + 2, column + 3, 1, 1)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setText("Enable")
            self.gridLayout.addWidget(self.label_4, row + 3, column + 1, 1, 1)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setText("Invert")
            self.gridLayout.addWidget(self.label_5, row + 3, column + 2, 1, 1)

            self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_6.setText("PE-Width")
            self.gridLayout.addWidget(self.label_6, row + 3, column + 3, 1, 1)

            self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_7.setText("PE-Strength")
            self.gridLayout.addWidget(self.label_7, row + 3, column + 4, 1, 1)

            self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_8.setText("PE-Mode")
            self.gridLayout.addWidget(self.label_8, row + 3, column + 5, 1, 1)

            self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_9.setText("Drive Strength")
            self.gridLayout.addWidget(self.label_9, row + 3, column + 6, 1, 1)

            self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_11.setText("  ")
            self.gridLayout.addWidget(self.label_11, row + 4, column + 7, 1, 1)

            self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_12. setText("  ")
            self.gridLayout.addWidget(self.label_12, row + 8, column + 4, 1, 1)

            for i in range(4):
                self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
                self.label_10.setText("CH%i:" % i)
                self.gridLayout.addWidget(self.label_10, row + 4 + i, column, 1, 1)

                #Enable
                self.checkbox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
                self.gridLayout.addWidget(self.checkbox_2, row + 4 + i, column + 1, 1, 1)

                #Invert
                self.checkbox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
                self.gridLayout.addWidget(self.checkbox_3, row + 4 + i, column + 2, 1, 1)

                #PE-Width
                self.combobox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.combobox_2.addItem("120")
                self.combobox_2.addItem("360")
                self.combobox_2.addItem("600")
                self.combobox_2.addItem("840")
                self.gridLayout.addWidget(self.combobox_2, row + 4 + i, column + 3, 1, 1)

                #PE-Strength
                self.combobox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.combobox_3.addItem("0")
                self.combobox_3.addItem("1.0")
                self.combobox_3.addItem("1.5")
                self.combobox_3.addItem("2.0")
                self.combobox_3.addItem("2.5")
                self.combobox_3.addItem("3.0")
                self.combobox_3.addItem("3.5")
                self.combobox_3.addItem("4.0")
                self.gridLayout.addWidget(self.combobox_3, row + 4 + i, column + 4, 1, 1)

                #PE-mode
                self.combobox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.combobox_4.addItem("disabled")
                self.combobox_4.addItem("disabled")
                self.combobox_4.addItem("Self timed")
                self.combobox_4.addItem("Clock timed")
                self.gridLayout.addWidget(self.combobox_4, row + 4 + i, column + 5, 1, 1)

                # drive strength
                self.combobox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.combobox_5.addItem("0")
                self.combobox_5.addItem("1.0")
                self.combobox_5.addItem("1.5")
                self.combobox_5.addItem("2.0")
                self.combobox_5.addItem("2.5")
                self.combobox_5.addItem("3.0")
                self.combobox_5.addItem("3.5")
                self.combobox_5.addItem("4.0")
                self.gridLayout.addWidget(self.combobox_5, row + 4 + i, column + 6, 1, 1)

            column += 8

            #EC channel -- NEED TO ADD THE OTHER REGISTERS!
            self.gridLayoutWidget_5 = QtWidgets.QWidget(Dialog)
            self.gridLayoutWidget_5.setGeometry(QtCore.QRect(460, 620, 515, 101))
            self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
            self.gridLayout_5.setContentsMargins(0, 0, 0, 0)

            self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_14.setText("EC Channel:")
            self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 3)

            self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_18.setText("Invert")
            self.gridLayout_5.addWidget(self.label_18, 1, 0, 1, 1)

            self.checkbox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
            self.gridLayout_5.addWidget(self.checkbox_4, 2, 0, 1, 1)

            self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_19.setText("Enable")
            self.gridLayout_5.addWidget(self.label_19, 1, 1, 1, 1)

            self.checkbox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
            self.gridLayout_5.addWidget(self.checkbox_5, 2, 1, 1, 1)

            self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_15.setText("PE-Strength")
            self.gridLayout_5.addWidget(self.label_15, 1, 2, 1, 1)

            self.combobox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
            self.combobox_6.addItem("0")
            self.combobox_6.addItem("1.0")
            self.combobox_6.addItem("1.5")
            self.combobox_6.addItem("2.0")
            self.combobox_6.addItem("2.5")
            self.combobox_6.addItem("3.0")
            self.combobox_6.addItem("3.5")
            self.combobox_6.addItem("4.0")
            self.gridLayout_5.addWidget(self.combobox_6, 2, 2, 1, 1)

            self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_16.setText("PE Mode")
            self.gridLayout_5.addWidget(self.label_16, 1, 3, 1, 1)

            self.combobox_7 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
            self.combobox_7.addItem("disabled")
            self.combobox_7.addItem("disabled")
            self.combobox_7.addItem("Self timed")
            self.combobox_7.addItem("Clock timed")
            self.gridLayout_5.addWidget(self.combobox_7, 2, 3, 1, 1)

            self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_17.setText("Drive Strength")
            self.gridLayout_5.addWidget(self.label_17, 1, 4, 1, 1)

            self.combobox_8 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
            self.combobox_8.addItem("0")
            self.combobox_8.addItem("1.0")
            self.combobox_8.addItem("1.5")
            self.combobox_8.addItem("2.0")
            self.combobox_8.addItem("2.5")
            self.combobox_8.addItem("3.0")
            self.combobox_8.addItem("3.5")
            self.combobox_8.addItem("4.0")
            self.gridLayout_5.addWidget(self.combobox_8, 2, 4, 1, 1)

            self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_5)
            self.label_20.setText("PE-Width")
            self.gridLayout_5.addWidget(self.label_20, 1, 5, 1, 1)

            self.combobox_9 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
            self.combobox_9.addItem("120")
            self.combobox_9.addItem("360")
            self.combobox_9.addItem("600")
            self.combobox_9.addItem("840")
            self.gridLayout_5.addWidget(self.combobox_9, 2, 5, 1, 1)

            # Total page buttons
            self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 750, 1180, 121))
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

            self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.pushButton_3.setText("Apply")
            self.horizontalLayout.addWidget(self.pushButton_3)

            self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.pushButton_2.setText("OK")
            self.horizontalLayout.addWidget(self.pushButton_2)
            self.pushButton_2.clicked.connect(self.save)
            self.pushButton_2.clicked.connect(Dialog.reject)

            self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.pushButton.setText("Cancel")
            self.horizontalLayout.addWidget(self.pushButton)
            self.pushButton.clicked.connect(Dialog.reject)


    def save(self):
        self.EPTX = 0
        self.clocks = 4
        row = 0
        column = 0

        #define variables
        self.datarate_val = 0
        self.PEWidth_val = 1
        self.Enable_val = 2
        self.PEStrength_val = 3
        self.PEMode_val = 4
        self.Drive_strength_val = 5
        self.mirror_enable_val = 6
        self.invert_val = 7

        #define lists
        dataRate_data = []
        PEWidth_data = []
        Enable_data = []
        PEStrength_data = []
        PEMode_data = []
        DriveStrength_data = []
        mirrorEnable_data = []
        invert_data = []


        for i in range(self.clocks):
            if column == 16:
                column = 0
                row += 10

            #data rate
            data_rate_box = self.gridLayout.itemAtPosition(row + 1, column + 3).widget()
            dataRate_data.append([self.EPTX, i, self.datarate_val, data_rate_box.currentIndex()])

            #mirror enable
            mirrorEnable_box = self.gridLayout.itemAtPosition(row + 2, column + 3).widget()
            if mirrorEnable_box.isChecked():
                mirrorEnable_data.append([self.EPTX, i, self.mirror_enable_val, '1'])
            else:
                mirrorEnable_data.append([self.EPTX, i, self.mirror_enable_val, '0'])

            #looping over channels
            p = 0
            for j in range(0,4):
                #enable
                enable_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 1).widget()
                if enable_box.isChecked():
                    Enable_data.append([self.EPTX, i, self.Enable_val + p, '1'])
                else:
                    Enable_data.append([self.EPTX, i, self.Enable_val + p, '0'])

                #invert
                invert_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 2).widget()
                if invert_box.isChecked():
                    invert_data.append([self.EPTX, i, self.invert_val + p, '1'])
                else:
                    invert_data.append([self.EPTX, i, self.invert_val + p, '0'])

                #PE-Width
                PEWidth_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 3).widget()
                PEWidth_data.append([self.EPTX, i, self.PEWidth_val + p, PEWidth_box.currentIndex()])

                #PE-Strength
                PEStrength_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 4).widget()
                PEStrength_data.append([self.EPTX, i, self.PEStrength_val + p, PEStrength_box.currentIndex()])

                #PE-Mode
                PEMode_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 5).widget()
                PEMode_data.append([self.EPTX, i, self.PEMode_val + p, PEMode_box.currentIndex()])

                #Drive Strength
                DriveStrength_box = self.gridLayout.itemAtPosition(row + 4 + j, column + 6).widget()
                DriveStrength_data.append([self.EPTX, i, self.Drive_strength_val + p, DriveStrength_box.currentIndex()])

                p += 6

            column += 8


        #EC channel! ################
        EC_invert_val = 26
        EC_enable_val = 27
        EC_PEStrength_val = 28
        EC_PEMode_val = 29
        EC_DriveStrength_val = 30
        EC_PEWidth_val = 31

        #invert
        EC_invert_box = self.gridLayout_5.itemAtPosition(2, 0).widget()
        if EC_invert_box.isChecked():
            EC_invert_data = [self.EPTX, 4, EC_invert_val, '1']
        else:
            EC_invert_data = [self.EPTX, 4, EC_invert_val, '0']

        #enable
        EC_enable_box = self.gridLayout_5.itemAtPosition(2, 1).widget()
        if EC_enable_box.isChecked():
            EC_enable_data = [self.EPTX, 4, EC_enable_val, '1']
        else:
            EC_enable_data = [self.EPTX, 4, EC_enable_val, '0']

        #PE-Strength
        EC_PEStrength_box = self.gridLayout_5.itemAtPosition(2, 2).widget()
        EC_PEStrength_data = [self.EPTX, 4, EC_PEStrength_val, EC_PEStrength_box.currentIndex()]

        #PE-Mode
        EC_PEMode_box = self.gridLayout_5.itemAtPosition(2, 3).widget()
        EC_PEMode_data = [self.EPTX, 4, EC_PEMode_val, EC_PEMode_box.currentIndex()]

        #drive strength
        EC_driveStrength_box = self.gridLayout_5.itemAtPosition(2, 4).widget()
        EC_driveStrength_data = [self.EPTX, 4, EC_DriveStrength_val, EC_driveStrength_box.currentIndex()]

        #PE-Width
        EC_PEWidth_box = self.gridLayout_5.itemAtPosition(2, 5).widget()
        EC_PEWidth_data = [self.EPTX, 4, EC_PEWidth_val, EC_PEWidth_box.currentIndex()]

        #Call function!!
        for DR in dataRate_data:
            function(DR[0], DR[1], DR[2], DR[3])

        for enbl in reversed(Enable_data):
            function(enbl[0], enbl[1], enbl[2], enbl[3])

        # 0x0a8
        function(EC_PEWidth_data[0], EC_PEWidth_data[1], EC_PEWidth_data[2], EC_PEWidth_data[3])
        function(EC_invert_data[0], EC_invert_data[1], EC_invert_data[2], EC_invert_data[3])
        function(EC_enable_data[0], EC_enable_data[1], EC_enable_data[2], EC_enable_data[3])
        for ME in reversed(mirrorEnable_data):
            function(ME[0], ME[1], ME[2], ME[3])

        # 0x0ab
        function(EC_PEStrength_data[0], EC_PEStrength_data[1], EC_PEStrength_data[2], EC_PEStrength_data[3])
        function(EC_PEMode_data[0], EC_PEMode_data[1], EC_PEMode_data[2], EC_PEMode_data[3])
        function(EC_driveStrength_data[0], EC_driveStrength_data[1], EC_driveStrength_data[2], EC_driveStrength_data[3])

        # 0x0ac
        for PES, PEM, DS in zip(PEStrength_data, PEMode_data, DriveStrength_data):
            function(PES[0], PES[1], PES[2], PES[3])
            function(PEM[0], PEM[1], PEM[2], PEM[3])
            function(DS[0], DS[1], DS[2], DS[3])

        post_function()

        # print(dataRate_data)
        # print(Enable_data)
        # print(DriveStrength_data)
        # print(PEMode_data)
        # print(PEStrength_data)



