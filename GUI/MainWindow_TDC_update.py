# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_trying.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Importing the popup windows
# from verificate_popup import Ui_Dialog as Form
# from ePLL_popup import Ui_Dialog as Form_2
# from datarate_popup import Ui_Dialog as Form_3
# from runmode_popup import Ui_Dialog as Form_4
# from wordmode_popup import Ui_Dialog as Form_5
# from edgetype_popup import Ui_Dialog as Form_6
# from channel_popup import Ui_Dialog as Form_7
from setup_0_popup import Ui_Dialog as Form_8
from setup_1_popup import Ui_Dialog as Form_9
from setup_2_popup import Ui_Dialog as Form_10
from control_0_popup import Ui_Dialog as Form_11
from control_1_popup import Ui_Dialog as Form_12
from read_only_popup import Ui_Dialog as Form_13

# import UART functions
sys.path.insert(0, "../UART_py3")

from serial_config_tdc import *
from TDCreg import *
from TDC_config_low_level_function import *


class Ui_MainWindow(object):

    def __init__(self, ser, TDC_inst):
        self.ser = ser
        self.TDC_inst = TDC_inst

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 773)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(19, 19, 820, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 261, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.data_rate)

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.activated.connect(self.trigger_mode)

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.activated.connect(self.format)

        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.comboBox_4.activated.connect(self.edge_type)

        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)
        self.spinBox.setValue(int(format(int(self.TDC_inst.phase_clk160[0], 2), 'd')))
        #self.spinBox.setValue(int(self.TDC_inst.updated_phase_clk160[0]))
        #self.spinBox.setValue(int(self.TDC_inst.enable_high_speed[0]))
        self.spinBox.valueChanged.connect(self.spinbox_160)


        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 5, 1, 1, 1)
        ######### What do we want to have here??
        self.spinBox_2.setValue(int(format(int(self.TDC_inst.phase_clk320_1[0], 2), 'd')))
        self.spinBox_2.valueChanged.connect(self.spinbox_320)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 30, 160, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.open_mode_set)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.open_internal_counter)

        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.open_fine_time_lut)

        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.open_reset_option)

        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.open_ePll_option)

        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.open_TDC_status)

        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_7.clicked.connect(self.verificate_all)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(610, 40, 161, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_8.clicked.connect(self.TRST)

        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox.toggled.connect(self.master_reset)

        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(65, 340, 171, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.init_settings)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(580, 380, 211, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 530, 800, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)

        #general textbrowser
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Hit gen"))
        self.label.setText(_translate("MainWindow", "Mode:"))
        self.label_2.setText(_translate("MainWindow", "Data Rate: "))
        self.comboBox.setItemText(0, _translate("MainWindow", "320Mb"))
        self.comboBox.setItemText(1, _translate("MainWindow", "160Mb"))
        self.comboBox.setItemText(2, _translate("MainWindow", "80Mb"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Triggerless"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Triggered"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "pair"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "edge"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "double_edge"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "pair_full_width"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "debug"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "TDC_ID"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "leading"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "falling"))
        self.label_3.setText(_translate("MainWindow", "Format:"))
        self.label_5.setText(_translate("MainWindow", "Clk160_phase: "))
        self.label_4.setText(_translate("MainWindow", "EdgeType:"))
        self.label_6.setText(_translate("MainWindow", "Clk320_1_phase:"))
        self.label_7.setText(_translate("MainWindow", "JTAG IN"))
        self.pushButton.setText(_translate("MainWindow", "mode set"))
        self.pushButton_2.setText(_translate("MainWindow", "internal counter"))
        self.pushButton_3.setText(_translate("MainWindow", "fine time lut"))
        self.pushButton_4.setText(_translate("MainWindow", "reset option"))
        self.pushButton_5.setText(_translate("MainWindow", "ePll option"))
        self.pushButton_6.setText(_translate("MainWindow", "TDC status"))
        self.pushButton_7.setText(_translate("MainWindow", "Verificate JTAG"))
        self.pushButton_8.setText(_translate("MainWindow", "TRST"))
        self.checkBox.setText(_translate("MainWindow", "master reset"))
        self.pushButton_9.setText(_translate("MainWindow", "Init"))
        self.pushButton_10.setText(_translate("MainWindow", "Load Setup"))
        self.pushButton_11.setText(_translate("MainWindow", "Save Setup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "TDC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ASD"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "CSM"))
        self.label_8.setText(_translate("MainWindow", "GUI run information"))

    #### functions calling to the popup windows  ####

    # For the Registers
    # mode set
    def open_mode_set(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_8(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

     #internal counter
    def open_internal_counter(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_9(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    #fine time lut
    def open_fine_time_lut(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_10(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    #reset option
    def open_reset_option(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_11(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    # ePll option
    def open_ePll_option(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_12(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.spinBox.setValue(dialog.ui.clk160_value)
        self.spinBox_2.setValue(dialog.ui.clk320_1_value)
        dialog.show()

    #TDC status
    def open_TDC_status(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_13(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    #Verificate all
    def verificate_all(self):
        verificate_all(self.ser)

    #data rate stuff
    def data_rate(self):
        # data rate
        if self.comboBox.currentIndex() == 0:
            self.TDC_inst.run_320M_data_rate()
        if self.comboBox.currentIndex() == 1:
            self.TDC_inst.run_160M_data_rate()
        if self.comboBox.currentIndex() == 2:
            self.TDC_inst.run_80M_data_rate()
        # self.TDC_inst.set_FPGA_sample_rate()

    def trigger_mode(self):
        # mode
        if self.comboBox_2.currentIndex() == 0:
            self.TDC_inst.run_triggerless_mode()
        if self.comboBox_2.currentIndex() == 1:
            self.TDC_inst.run_trigger_mode()
        # self.TDC_inst.set_trigger_type()

    def format(self):
        # format
        if self.comboBox_3.currentIndex() == 0:
            self.TDC_inst.run_pair_mode()
        if self.comboBox_3.currentIndex() == 1:
            self.TDC_inst.run_single_edge_mode()
        if self.comboBox_3.currentIndex() == 2:
            self.TDC_inst.run_double_edge_mode()
        if self.comboBox_3.currentIndex() == 3:
            self.TDC_inst.run_pair_full_width_mode()
        if self.comboBox_3.currentIndex() == 4:
            self.TDC_inst.run_debug_mode()
        if self.comboBox_3.currentIndex() == 5:
            self.TDC_inst.run_TDCID_mode()
        # self.TDC_inst.set_word_byte()

    def edge_type(self):
        # Edge type
        if self.comboBox_4.currentIndex() == 0:
            self.TDC_inst.set_rising_is_leading()
        if self.comboBox_4.currentIndex() == 1:
            self.TDC_inst.set_falling_is_leading()

    def spinbox_160(self):
        # phase_clk160
        self.phase_clk160_binary = format(self.spinBox.value(), '05b')
        self.TDC_inst.phase_clk160[0] = self.phase_clk160_binary

    def spinbox_320(self):
        self.phase_clk320_0_binary = format(self.spinBox_2.value()+4, '04b')[-4:]
        self.TDC_inst.phase_clk320_0[0] = self.phase_clk320_0_binary

        self.phase_clk320_1_binary = format(self.spinBox_2.value(), '04b')
        self.TDC_inst.phase_clk320_1[0] = self.phase_clk320_1_binary

    #Init button!
    def init_settings(self):
        self.TDC_inst.DAQ_init()

    #TRST button connect
    def TRST(self):
        self.TDC_inst.reset_all_reg()

    def master_reset(self):
        if self.checkBox.isChecked() == True:
            tdc_master_reset_1(self.ser)
            #print("what")
            print("master reset 1")
        if self.checkBox.isChecked() == False:
            tdc_master_reset_0(self.ser)
            print("master reset 0")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
