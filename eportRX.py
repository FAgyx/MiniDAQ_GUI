from PyQt5 import QtCore, QtGui, QtWidgets
from LpGBT_functions__two_change_setup import *

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1875, 766)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1855, 610))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.groups = 7
        column = 0
        column_two = 1
        row = 0
        row_two = 1

        # loop over the groups (0-6)
        for i in range(self.groups):
            if column == 32:
                column = 0
                column_two = 1
                row += 9
                row_two += 9

            self.label = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label.setText("G%s" % i)
            self.label.setFont(QtGui.QFont("Calbri", 8))
            self.gridLayout.addWidget(self.label, row, column, 1, 1)

            self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_2.setText("Data rate (5Gbps, 10,gbps):")
            self.gridLayout.addWidget(self.label_2, row + 1, column, 1, 3)

            self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.comboBox.addItem("disabled")
            self.comboBox.addItem("160 Mbps, 320 Mbps")
            self.comboBox.addItem("320 Mbps, 640 Mbps")
            self.comboBox.addItem("640 Mbps, 1280 Mbps")
            self.gridLayout.addWidget(self.comboBox, row + 1, column_two + 2, 1, 2)

            self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_3.setText("Tracking mode:")
            self.gridLayout.addWidget(self.label_3, row + 2, column, 1, 2)

            self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
            self.comboBox_5.addItem("Fixed phase")
            self.comboBox_5.addItem("Initial training")
            self.comboBox_5.addItem("Cont. phase tracking")
            self.comboBox_5.addItem("Cont. phase tracking with init. phase")
            self.gridLayout.addWidget(self.comboBox_5, row + 2, column_two + 1, 1, 3)

            self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_4.setText("Enable")
            self.gridLayout.addWidget(self.label_4, row + 3, column_two, 1, 1)

            for i in range(4):
                self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
                self.gridLayout.addWidget(self.checkBox, row + 4 + i, column_two, 1, 1)

            self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_5.setText("Phase Select")
            self.gridLayout.addWidget(self.label_5, row + 3, column_two + 1, 1, 1)

            for i in range(4):
                self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
                self.gridLayout.addWidget(self.spinBox_2, row + 4 + i, column_two + 1, 1, 1)

            self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_6.setText("Control")
            self.gridLayout.addWidget(self.label_6, row + 3, column_two + 2, 1, 1)

            for i in range(4):
                self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.comboBox_3.addItem("Term")
                self.comboBox_3.addItem("AcBias")
                self.comboBox_3.addItem("Inv")
                self.gridLayout.addWidget(self.comboBox_3, row + 4 + i, column_two + 2, 1, 1)

            self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_8.setText("Equalization")
            self.gridLayout.addWidget(self.label_8, row + 3, column_two + 3, 1, 1)

            for i in range(4):
                self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
                self.comboBox_2.addItem("300 MHz, 4.9 dB")
                self.comboBox_2.addItem("125 MHz, 7.8 dB")
                self.comboBox_2.addItem("70 MHz, 10.7 dB")
                self.gridLayout.addWidget(self.comboBox_2, row + 4 + i, column_two + 3, 1, 1)

            self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_9.setText("  ")
            self.gridLayout.addWidget(self.label_9, row + 3, column_two + 6, 1, 1)

            self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_10.setText("Ch0:")
            self.gridLayout.addWidget(self.label_10, row + 4, column, 1, 1)

            self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_11.setText("Ch1:")
            self.gridLayout.addWidget(self.label_11, row + 5, column, 1, 1)

            self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_12.setText("Ch2:")
            self.gridLayout.addWidget(self.label_12, row + 6, column, 1, 1)

            self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_13.setText("Ch3:")
            self.gridLayout.addWidget(self.label_13, row + 7, column, 1, 1)

            self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
            self.label_14.setText("          ")
            self.gridLayout.addWidget(self.label_14, row + 3, column, 1, 1)

            column += 8
            column_two += 8

        # EC channel stuff
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("Ec Channel:")
        self.gridLayout.addWidget(self.label_15, 10, 25, 2, 1)

        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setText("Enable:")
        self.gridLayout.addWidget(self.label_16, 12, 25, 1, 1)

        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.checkBox_4, 12, 26, 1, 2)

        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setText("Tracking Mode:")
        self.gridLayout.addWidget(self.label_17, 13, 25, 1, 1)

        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.spinBox_3, 13, 26, 1, 2)

        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setText("Phase Select:")
        self.gridLayout.addWidget(self.label_18, 14, 25, 1, 1)

        self.spinBox_4 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.spinBox_4, 14, 26, 1, 2)

        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setText("Control:")
        self.gridLayout.addWidget(self.label_19, 15, 25, 1, 1)

        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.addItem("Term")
        self.comboBox_4.addItem("AcBias")
        self.comboBox_4.addItem("Inv")
        self.gridLayout.addWidget(self.comboBox_4, 15, 26, 1, 2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 660, 1671, 80))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setText("Apply")
        self.pushButton_3.clicked.connect(self.save)
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
        self.groups = 7
        self.EPRX = 1

        # setup parameters
        column = 0
        column_two = 1
        row = 0
        row_two = 1
        self.ch3_enable_val = 0
        self.ch2_enable_val = 1
        self.ch1_enable_val = 2
        self.ch0_enable_val = 3
        self.data_rate_val = 4
        self.track_mode_val = 5
        self.EC_val = 6
        self.Phase_select_val = 7
        self.Invert_val = 8
        self.AcBias_val = 9
        self.Term_val = 10
        self.Eq_val = 11
        self.EC_PS_val = 27
        self.EC_inv_val = 28
        self.EC_AcBias_val = 29
        self.EC_Term_val = 30
        self.EC_enable_val = 31

        # setup lists
        self.ch3_enable_data = []
        self.ch2_enable_data = []
        self.ch1_enable_data = []
        self.ch0_enable_data = []
        self.data_rate_data = []
        self.track_mode_data = []
        self.phase_select_data = []
        self.invert_data = []
        self.AcBias_data = []
        self.term_data = []
        self.Eq_data = []

        # loop over groups, i is group!!
        test_list = []
        for i in range(self.groups):
            if column == 32:
                column = 0
                column_two = 1
                row += 9
                row_two += 9

            # ch3 enable saving
            ch3_enable_check_box = self.gridLayout.itemAtPosition(row + 4 + 3, column_two).widget()
            if ch3_enable_check_box.isChecked():
                self.ch3_enable_data.append([self.EPRX, i, self.ch3_enable_val, '1'])
            else:
                self.ch3_enable_data.append([self.EPRX, i, self.ch3_enable_val, '0'])

            # ch2 enable saving
            ch2_enable_check_box = self.gridLayout.itemAtPosition(row + 4 + 2, column_two).widget()
            if ch2_enable_check_box.isChecked():
                self.ch2_enable_data.append([self.EPRX, i, self.ch2_enable_val, '1'])
            else:
                self.ch2_enable_data.append([self.EPRX, i, self.ch2_enable_val, '0'])

            # ch1 enable saving
            ch1_enable_check_box = self.gridLayout.itemAtPosition(row + 4 + 1, column_two).widget()
            if ch1_enable_check_box.isChecked():
                self.ch1_enable_data.append([self.EPRX, i, self.ch1_enable_val, '1'])
            else:
                self.ch1_enable_data.append([self.EPRX, i, self.ch1_enable_val, '0'])

            # ch0 enable saving
            ch0_enable_check_box = self.gridLayout.itemAtPosition(row + 4, column_two).widget()
            if ch0_enable_check_box.isChecked():
                self.ch0_enable_data.append([self.EPRX, i, self.ch0_enable_val, '1'])
            else:
                self.ch0_enable_data.append([self.EPRX, i, self.ch0_enable_val, '0'])

            # data rate
            data_rate_box = self.gridLayout.itemAtPosition(row + 1, column_two + 2).widget()
            self.data_rate_data.append([self.EPRX, i, self.data_rate_val, data_rate_box.currentIndex()])

            # track mode
            track_mode_box = self.gridLayout.itemAtPosition(row + 2, column_two + 1).widget()
            self.track_mode_data.append([self.EPRX, i, self.track_mode_val, track_mode_box.currentIndex()])

            # phase select
            p = 0
            for j in range(0, 4):
                phase_select_box = self.gridLayout.itemAtPosition(row + 4 + j, column_two + 1).widget()
                self.phase_select_data.append([self.EPRX, i, self.Phase_select_val + p, phase_select_box.value()])
                p += 5

            # Invert, AcBias, Term together
            p = 0
            for j in range(0, 4):
                control_box = self.gridLayout.itemAtPosition(row + 4 + j, column_two + 2).widget()
                if control_box.currentIndex() == 0:
                    test_list.append(j)
                    self.term_data.append([self.EPRX, i, self.Term_val + p, '1'])
                    self.AcBias_data.append([self.EPRX, i, self.AcBias_val + p, '0'])
                    self.invert_data.append([self.EPRX, i, self.Invert_val + p, '0'])
                if control_box.currentIndex() == 1:
                    self.term_data.append([self.EPRX, i, self.Term_val + p, '0'])
                    self.AcBias_data.append([self.EPRX, i, self.AcBias_val + p, '1'])
                    self.invert_data.append([self.EPRX, i, self.Invert_val + p, '0'])
                if control_box.currentIndex() == 2:
                    self.term_data.append([self.EPRX, i, self.Term_val + p, '0'])
                    self.AcBias_data.append([self.EPRX, i, self.AcBias_val + p, '0'])
                    self.invert_data.append([self.EPRX, i, self.Invert_val + p, '1'])
                p += 5

            # Equalization
            p = 0
            for j in range(0, 4):
                Eq_box = self.gridLayout.itemAtPosition(row + 4 + j, column_two + 3).widget()
                self.Eq_data.append([self.EPRX, i, self.Eq_val + p, Eq_box.currentIndex()])
                p += 5

            column += 8
            column_two += 8

        for ch3Enbl, ch2Enbl, ch1Enbl, ch0Enbl, dataRte, trkMde in zip(self.ch3_enable_data,
                                                                       self.ch2_enable_data, self.ch1_enable_data,
                                                                       self.ch0_enable_data, self.data_rate_data,
                                                                       self.track_mode_data):
            # EPRX Group Control
            function(ch3Enbl[0], ch3Enbl[1], ch3Enbl[2], ch3Enbl[3])
            function(ch2Enbl[0], ch2Enbl[1], ch2Enbl[2], ch2Enbl[3])
            function(ch1Enbl[0], ch1Enbl[1], ch1Enbl[2], ch1Enbl[3])
            function(ch0Enbl[0], ch0Enbl[1], ch0Enbl[2], ch0Enbl[3])
            function(dataRte[0], dataRte[1], dataRte[2], dataRte[3])
            function(trkMde[0], trkMde[1], trkMde[2], trkMde[3])

        # EC Channel Control
        track_mode_EC_box = self.gridLayout.itemAtPosition(13, 26).widget()
        self.EC_channel_control = [self.EPRX, 7, self.EC_val, track_mode_EC_box.value()]
        function(self.EC_channel_control[0], self.EC_channel_control[1], self.EC_channel_control[2],
                 self.EC_channel_control[3])


        # EPRX CHN CNTR
        for PS, inv, AcBias, Term, Eq in zip(self.phase_select_data, self.invert_data, self.AcBias_data, self.term_data,
                                             self.Eq_data):
            function(PS[0], PS[1], PS[2], PS[3])
            function(inv[0], inv[1], inv[2], inv[3])
            function(AcBias[0], AcBias[1], AcBias[2], AcBias[3])
            function(Term[0], Term[1], Term[2], Term[3])
            function(Eq[0], Eq[1], Eq[2], Eq[3])


        # EC Chn Cntr
        phase_select_EC_box = self.gridLayout.itemAtPosition(14, 26).widget()
        self.PS_EC_chn_cntr = [self.EPRX, 7, self.EC_PS_val, phase_select_EC_box.value()]

        # Invert, AcBias, Term together
        control_box_EC = self.gridLayout.itemAtPosition(15, 26).widget()
        if control_box_EC.currentIndex() == 0:
            self.EC_term_data = [self.EPRX, 7, self.EC_Term_val, '1']
            self.EC_AcBias_data = [self.EPRX, 7, self.EC_AcBias_val, '0']
            self.EC_invert_data = [self.EPRX, 7, self.EC_inv_val, '0']
        if control_box_EC.currentIndex() == 1:
            self.EC_term_data = [self.EPRX, 7, self.EC_Term_val, '0']
            self.EC_AcBias_data = [self.EPRX, 7, self.EC_AcBias_val, '1']
            self.EC_invert_data = [self.EPRX, 7, self.EC_inv_val, '0']
        if control_box_EC.currentIndex() == 2:
            self.EC_term_data = [self.EPRX, 7, self.EC_Term_val, '0']
            self.EC_AcBias_data = [self.EPRX, 7, self.EC_AcBias_val, '0']
            self.EC_invert_data = [self.EPRX, 7, self.EC_inv_val, '1']

        #enable
        enable_EC_box = self.gridLayout.itemAtPosition(12, 26).widget()
        if enable_EC_box.isChecked():
            self.enable_EC_data = [self.EPRX, 7, self.EC_enable_val, '1']
        else:
            self.enable_EC_data = [self.EPRX, 7, self.EC_enable_val, '0']

        function(self.PS_EC_chn_cntr[0], self.PS_EC_chn_cntr[1], self.PS_EC_chn_cntr[2], self.PS_EC_chn_cntr[3])
        function(self.EC_invert_data[0], self.EC_invert_data[1], self.EC_invert_data[2], self.EC_invert_data[3])
        function(self.EC_AcBias_data[0], self.EC_AcBias_data[1], self.EC_AcBias_data[2], self.EC_AcBias_data[3])
        function(self.EC_term_data[0], self.EC_term_data[1], self.EC_term_data[2], self.EC_term_data[3])
        function(self.enable_EC_data[0], self.enable_EC_data[1], self.enable_EC_data[2], self.enable_EC_data[3])

        print("EPRX Control - addresses and values : \n %s " % add_and_reg)
        print(" END OF RUN ")
        post_function()