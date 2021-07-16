# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Equalizer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from LpGBT_functions_two import *

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):

        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 388)
        Dialog.setWindowTitle("Equalizer")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 50, 371, 211))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("Resistance 3 (kOhm):")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("Attenuation (V/V):")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("Capacitance (fF):")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setText("Resistance 0 (kOhm):")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setText("Resistance 1 (kOhm):")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setText("Resistance 2 (kOhm):")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("1/3")
        self.comboBox.addItem("2/3")
        self.comboBox.addItem("1/1")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("0")
        self.comboBox_2.addItem("70")
        self.comboBox_2.addItem("140")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.addItem("0")
        self.comboBox_3.addItem("0.4")
        self.comboBox_3.addItem("1.0")
        self.comboBox_3.addItem("1.6")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_7.addItem("0")
        self.comboBox_7.addItem("0.6")
        self.comboBox_7.addItem("1.2")
        self.comboBox_7.addItem("2.4")
        self.gridLayout.addWidget(self.comboBox_7, 3, 1, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_8.addItem("0")
        self.comboBox_8.addItem("3.0")
        self.comboBox_8.addItem("4.9")
        self.comboBox_8.addItem("7.1")
        self.gridLayout.addWidget(self.comboBox_8, 4, 1, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_9.addItem("0")
        self.comboBox_9.addItem("3.0")
        self.comboBox_9.addItem("4.9")
        self.comboBox_9.addItem("7.1")
        self.gridLayout.addWidget(self.comboBox_9, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 181, 21))
        self.label_7.setText("Equalizer: ")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 290, 371, 71))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setText("Apply")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setText("OK")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setText("Cancel")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        ## testing
        # self.comboBox_9.setCurrentIndex(2)

        # ################## xml loading ######################
        # # attenuation
        # if root[6][0].text == '0x0':
        #     self.comboBox.setCurrentIndex(0)
        # if root[6][0].text == '0x1':
        #     self.comboBox.setCurrentIndex(1)
        # if root[6][0].text == '0x3':
        #     self.comboBox.setCurrentIndex(2)
        #
        # # Capacitance
        # if root[6][1].text == '0x0':
        #     self.comboBox_2.setCurrentIndex(0)
        # if root[6][1].text == '0x1':
        #     self.comboBox_2.setCurrentIndex(1)
        # if root[6][1].text == '0x3':
        #     self.comboBox_3.setCurrentIndex(2)
        #
        # # Resistance 3
        # if root[6][2].text == '0x0':
        #     self.comboBox_3.setCurrentIndex(0)
        # if root[6][2].text == '0x1':
        #     self.comboBox_3.setCurrentIndex(1)
        # if root[6][2].text == '0x2':
        #     self.comboBox_3.setCurrentIndex(2)
        # if root[6][2].text == '0x3':
        #     self.comboBox_3.setCurrentIndex(3)
        #
        # # Resistance 2
        # if root[6][3].text == '0x0':
        #     self.comboBox_7.setCurrentIndex(0)
        # if root[6][3].text == '0x1':
        #     self.comboBox_7.setCurrentIndex(1)
        # if root[6][3].text == '0x2':
        #     self.comboBox_7.setCurrentIndex(2)
        # if root[6][3].text == '0x3':
        #     self.comboBox_7.setCurrentIndex(3)
        #
        # # Resistance 1
        # if root[6][4].text == '0x0':
        #     self.comboBox_8.setCurrentIndex(0)
        # if root[6][4].text == '0x1':
        #     self.comboBox_8.setCurrentIndex(1)
        # if root[6][4].text == '0x2':
        #     self.comboBox_8.setCurrentIndex(2)
        # if root[6][4].text == '0x3':
        #     self.comboBox_8.setCurrentIndex(3)
        #
        # # Resistance 0
        # if root[6][5].text == '0x0':
        #     self.comboBox_9.setCurrentIndex(0)
        # if root[6][5].text == '0x1':
        #     self.comboBox_9.setCurrentIndex(1)
        # if root[6][5].text == '0x2':
        #     self.comboBox_9.setCurrentIndex(2)
        # if root[6][5].text == '0x3':
        #     self.comboBox_9.setCurrentIndex(3)

    def save(self):
        self.Equalizer = 6
        self.attenuation_val = 0
        self.EQCap_val = 1
        self.EQRes3_val = 2
        self.EQRes2_val = 3
        self.EQRes1_val = 4
        self.EQRes0_val = 5

        self.atten_data = [self.Equalizer, 0, self.attenuation_val, self.comboBox.currentIndex()]
        self.EQCap_data = [self.Equalizer, 0, self.EQCap_val, self.comboBox_2.currentIndex()]
        self.EQRes3_data = [self.Equalizer, 0, self.EQRes3_val, self.comboBox_3.currentIndex()]
        self.EQRes2_data = [self.Equalizer, 0, self.EQRes2_val, self.comboBox_7.currentIndex()]
        self.EQRes1_data = [self.Equalizer, 0, self.EQRes1_val, self.comboBox_8.currentIndex()]
        self.EQRes0_data = [self.Equalizer, 0, self.EQRes0_val, self.comboBox_9.currentIndex()]

        function(self.atten_data[0], self.atten_data[1], self.atten_data[2], self.atten_data[3])
        function(self.EQCap_data[0], self.EQCap_data[1], self.EQCap_data[2], self.EQCap_data[3])
        function(self.EQRes3_data[0], self.EQRes3_data[1], self.EQRes3_data[2], self.EQRes3_data[3])
        function(self.EQRes2_data[0], self.EQRes2_data[1], self.EQRes2_data[2], self.EQRes2_data[3])
        function(self.EQRes1_data[0], self.EQRes1_data[1], self.EQRes1_data[2], self.EQRes1_data[3])
        function(self.EQRes0_data[0], self.EQRes0_data[1], self.EQRes0_data[2], self.EQRes0_data[3])

        print("Equalizer's registers addresses and values \n %s:" % add_and_reg)
        post_function()


        # print("in progress")
        # import xml.etree.ElementTree as ET
        # # tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
        # tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        # root = tree_ePortTX.getroot()
        #
        # #attenuation
        # if self.comboBox.currentIndex() == 0:
        #     root[6][0].text = '0x0'
        # if self.comboBox.currentIndex() == 1:
        #     root[6][0].text = '0x1'
        # if self.comboBox.currentIndex() == 2:
        #     root[6][0].text = '0x3'
        #
        # #Capacitance
        # if self.comboBox_2.currentIndex() == 0:
        #     root[6][1].text = '0x0'
        # if self.comboBox_2.currentIndex() == 1:
        #     root[6][1].text = '0x1'
        # if self.comboBox_2.currentIndex() == 2:
        #     root[6][1].text = '0x3'
        #
        #
        # #Resistance 3
        # if self.comboBox_3.currentIndex() == 0:
        #     root[6][2].text = '0x0'
        # if self.comboBox_3.currentIndex() == 1:
        #     root[6][2].text = '0x1'
        # if self.comboBox_3.currentIndex() == 2:
        #     root[6][2].text = '0x2'
        # if self.comboBox_3.currentIndex() == 3:
        #     root[6][2].text = '0x3'
        #
        # # Resistance 2
        # if self.comboBox_7.currentIndex() == 0:
        #     root[6][3].text = '0x0'
        # if self.comboBox_7.currentIndex() == 1:
        #     root[6][3].text = '0x1'
        # if self.comboBox_7.currentIndex() == 2:
        #     root[6][3].text = '0x2'
        # if self.comboBox_7.currentIndex() == 3:
        #     root[6][3].text = '0x3'
        #
        # # Resistance 1
        # if self.comboBox_8.currentIndex() == 0:
        #     root[6][4].text = '0x0'
        # if self.comboBox_8.currentIndex() == 1:
        #     root[6][4].text = '0x1'
        # if self.comboBox_8.currentIndex() == 2:
        #     root[6][4].text = '0x2'
        # if self.comboBox_8.currentIndex() == 3:
        #     root[6][4].text = '0x3'
        #
        # # Resistance 0
        # if self.comboBox_9.currentIndex() == 0:
        #     root[6][5].text = '0x0'
        # if self.comboBox_9.currentIndex() == 1:
        #     root[6][5].text = '0x1'
        # if self.comboBox_9.currentIndex() == 2:
        #     root[6][5].text = '0x2'
        # if self.comboBox_9.currentIndex() == 3:
        #     root[6][5].text = '0x3'
        #
        # tree_ePortTX.write('LpGBT_auto_saved.xml')
        # tree_ePortTX.write('LpGBT_transfer.xml')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
