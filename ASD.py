
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def __init__(self, ASD_chip_inst, ASD_mezz_inst, ASD_name):
        self.ASD_chip_inst = ASD_chip_inst
        self.ASD_name = ASD_name
        self.ASD_mezz_inst = ASD_mezz_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 567)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 611, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #All channels on
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 9, 1, 1)
        self.pushButton.clicked.connect(self.all_channels_on)

        #All channels off
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 9, 1, 1)
        self.pushButton_2.clicked.connect(self.all_channels_off)

        #checkbox labels
        for i in range(8):
            label = QtWidgets.QLabel(self.gridLayoutWidget)
            label.setObjectName("label_%d"%i)
            self.gridLayout.addWidget(label, 0, i+1, 1, 1)
            label.setText("%d"%i)

        #checkboxes
        self.checkBox_list = []
        for i in range (8):
            checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
            self.gridLayout.addWidget(checkBox, 2, i+1, 1, 1)
            if self.ASD_chip_inst.setup[i][0] == '00':
                checkBox.setChecked(True)
            self.checkBox_list.append(checkBox)

        self.label_channel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_channel.setObjectName("label")
        self.gridLayout.addWidget(self.label_channel, 2, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 140, 191, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)

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
        self.spinbox_value = int(format(int(self.ASD_chip_inst.main_thr[0], 2), '02d'))
        self.spinbox_value_true = int(255 - self.spinbox_value*2)
        self.spinBox.setValue(self.spinbox_value_true)

        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 1, 1, 1)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(60, 310, 471, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        #chip mode
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("ADC mode")
        self.comboBox.addItem("TOT mode")
        self.horizontalLayout.addWidget(self.comboBox)
        if self.ASD_chip_inst.chip_mode[0] == '0':
            self.comboBox.setCurrentIndex(0)
        if self.ASD_chip_inst.chip_mode[0] == '1':
            self.comboBox.setCurrentIndex(1)

        #Disc 1 Hyst
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        n = 0
        for i in range(17):
            self.comboBox_2.addItem("%d"%n)
            n += 20
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.hyst_bin_rev = ''.join(reversed(str(self.ASD_chip_inst.hyst[0])))
        self.hyst_index = int(format(int(self.hyst_bin_rev, 2), 'd'))
        self.comboBox_2.setCurrentIndex(self.hyst_index)

        #wilk thr
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        wilkthr_val = 32
        for i in range(8):
            self.comboBox_4.addItem("%d  mV"%wilkthr_val)
            wilkthr_val += 32
        self.gridLayout_3.addWidget(self.comboBox_4, 1, 2, 1, 1)
        self.wilkthr_index = format(int(self.ASD_chip_inst.wilk_thr[0], 2), '02d')
        self.comboBox_4.setCurrentIndex(int(self.wilkthr_index))

        #deadtime
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_6.setObjectName("comboBox_6")
        deadtime_val = 40
        for i in range(8):
            self.comboBox_6.addItem("%d  ns"%deadtime_val)
            deadtime_val += 110
        self.gridLayout_3.addWidget(self.comboBox_6, 1, 4, 1, 1)
        self.deadtime_index = format(int(self.ASD_chip_inst.deadtime[0], 2), '02d')
        self.comboBox_6.setCurrentIndex(int(self.deadtime_index))

        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_5.setObjectName("comboBox_5")
        rundowncurr_val = 7.3
        for i in range(8):
            self.comboBox_5.addItem("%.1f  uA"%rundowncurr_val)
            rundowncurr_val -= 0.7
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 3, 1, 1)
        self.rundowncurr_index = format(int(self.ASD_chip_inst.rundown_curr[0], 2), '02d')
        self.comboBox_5.setCurrentIndex(int(self.rundowncurr_index))

        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        something_val = 8
        for i in range(16):
            self.comboBox_3.addItem("%.1f  ns"%something_val)
            something_val += 2.5
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.intgate_index = format(int(self.ASD_chip_inst.int_gate[0], 2), '02d')
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.ASD_name))
        self.pushButton.setText(_translate("Dialog", "All Channels On"))
        self.pushButton_2.setText(_translate("Dialog", "All Channels Off"))
        self.label_channel.setText(_translate("Dialog", "Channel:   "))
        self.label_10.setText(_translate("Dialog", "Chip Mode:"))
        self.label_11.setText(_translate("Dialog", "Main Thr (mV):"))
        self.label_12.setText(_translate("Dialog", "Disc1 Hyst (uA):"))
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

    def save(self):
        #channels
        for i in range(8):
            if self.checkBox_list[i].isChecked() == True:
                self.ASD_chip_inst.setup[i][0] = '00'
            else:
                self.ASD_chip_inst.setup[i][0] = '11'

        #chip_mode
        if self.comboBox.currentIndex() == 0:
            self.ASD_chip_inst.chip_mode[0] = '0'
        else:
            self.ASD_chip_inst.chip_mode[0] = '1'

        #hyst
        self.hyst_binary = format(self.comboBox_2.currentIndex(), '04b')
        self.hyst_binary_reversed = reversed(self.hyst_binary)
        self.hyst_binary_reversed_val = ''.join(self.hyst_binary_reversed)
        self.ASD_chip_inst.hyst[0] = self.hyst_binary_reversed_val

        #int_gate
        self.int_gate_index = self.comboBox_3.currentIndex()
        self.int_gate_binary = format(self.int_gate_index, '04b')
        self.ASD_chip_inst.int_gate[0] = self.int_gate_binary

        #Disc2 Thr - wilk thr
        self.wilk_thr_index = self.comboBox_4.currentIndex()
        self.wilk_thr_binary = format(self.wilk_thr_index, '03b')
        self.ASD_chip_inst.wilk_thr[0] = self.wilk_thr_binary

        #Rund Curr
        self.round_curr_index = self.comboBox_5.currentIndex()
        self.round_curr_binary = format(self.round_curr_index, '03b')
        self.ASD_chip_inst.rundown_curr[0] = self.round_curr_binary

        #deadtime
        self.dead_time_index = self.comboBox_6.currentIndex()
        self.dead_time_binary = format(self.dead_time_index, '03b')
        self.ASD_chip_inst.deadtime[0] = self.dead_time_binary

        #main_thr
        self.main_thr_val = int((255 - self.spinBox.value())/2)
        self.main_thr_binary = format(self.main_thr_val, '08b')
        self.ASD_chip_inst.main_thr[0] = self.main_thr_binary

    def save_single(self):
        self.save()
        print('Settings saved to ' + self.ASD_name)

    def save_all(self):
        self.save()
        for chip_setup in self.ASD_mezz_inst.ASD_mezz_setup:
            for i in range(len(chip_setup)):
                chip_setup[i][0] = self.ASD_chip_inst.setup[i][0]

        print('Settings saved to all ASDs')

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())