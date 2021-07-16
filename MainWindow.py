
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
import sys
from pathlib import Path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

# Importing the popup windows
from setup_0 import Ui_Dialog as Form_8
from setup_1 import Ui_Dialog as Form_9
from setup_2 import Ui_Dialog as Form_10
from control_0 import Ui_Dialog as Form_11
from control_1 import Ui_Dialog as Form_12
from TDC_rename import Ui_Dialog as Form_13
from ASD import Ui_Dialog as Form_14
from ePortTX import Ui_Dialog as Form_15
from eportRX import Ui_Dialog as Form_16
from epclk import Ui_Dialog as Form_17
from PSCLK import Ui_Dialog as Form_18
from Equalizer import Ui_Dialog as Form_19
from LineDriver import Ui_Dialog as Form_20
from chip_config import Ui_Dialog as Form_21
from chip_mode import Ui_Dialog as Form_22
from Transmitter_mode import Ui_Dialog as Form_23

# import UART functions
sys.path.insert(0, "../UART_py3")

from serial_config_tdc import *
from TDCreg import *
from TDC_config_low_level_function import *

from CSM_WriteReg import *
import time
timestr = time.strftime("%Y-%m-%d-%H%M%S")

class Ui_MainWindow(object):

    def __init__(self, ser, TDC_inst):
        self.ser = ser
        self.TDC_inst = TDC_inst
        self.val = 0
        self.val_2 = 0

    def setupUi(self, MainWindow):

        tree_LpGBT = ET.parse('LpGBT_default_2.xml')
        tree_LpGBT.write('LpGBT_transfer.xml')

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 743)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        #tab setup
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(19, 19, 820, 441))
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_3, "")

        # menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        # self.menu = QtWidgets.QMenu(self.menubar)
        self.menu = self.menubar.addMenu("file")
        # self.menu.setObjectName("TDC")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        #TDC menu options
        self.TDCSaveDefault = QtWidgets.QAction(MainWindow)
        self.TDCSaveDefault.triggered.connect(self.save_setup_func_TDC)
        self.TDCSaveAs = QtWidgets.QAction(MainWindow)
        self.TDCSaveAs.triggered.connect(self.saveFileAs_TDC)
        self.TDCLoadFrom = QtWidgets.QAction(MainWindow)
        self.TDCLoadFrom.triggered.connect(self.loadFileFrom_TDC)
        self.TDCLoadDefault = QtWidgets.QAction(MainWindow)
        self.TDCLoadDefault.triggered.connect(self.loadFileDefault_TDC)
        self.menu.addAction(self.TDCLoadDefault)
        self.menu.addAction(self.TDCLoadFrom)
        self.menu.addAction(self.TDCSaveDefault)
        self.menu.addAction(self.TDCSaveAs)
        #ASD menu options
        self.ASDSaveDefault = QtWidgets.QAction(MainWindow)
        self.ASDSaveDefault.triggered.connect(self.save_setup_func_ASD)
        self.ASDSaveAs = QtWidgets.QAction(MainWindow)
        self.ASDSaveAs.triggered.connect(self.saveFileAs_ASD)
        self.ASDLoadFrom = QtWidgets.QAction(MainWindow)
        self.ASDLoadFrom.triggered.connect(self.loadFileFrom_ASD)
        self.ASDLoadDefault = QtWidgets.QAction(MainWindow)
        self.ASDLoadDefault.triggered.connect(self.loadFileDefault_ASD)
        self.menu.addAction(self.ASDLoadDefault)
        self.menu.addAction(self.ASDLoadFrom)
        self.menu.addAction(self.ASDSaveDefault)
        self.menu.addAction(self.ASDSaveAs)
        #menu action
        self.menubar.addAction(self.menu.menuAction())

##################################################################
        #CSM file stuff
        self.menu_2 = self.menubar.addMenu("File_CSM")
        self.LpGBTLoadDefault = QtWidgets.QAction(MainWindow)
        self.LpGBTLoadDefault.setText("LpGBT load default setup")
        self.LpGBTLoadDefault.triggered.connect(self.loadFileDefault_LpGBT)

        self.LpGBTLoadFrom = QtWidgets.QAction(MainWindow)
        self.LpGBTLoadFrom.setText("LpGBT load setup From")
        self.LpGBTLoadFrom.triggered.connect(self.loadFileFrom_LpGBT)

        self.LpGBTSaveDefault = QtWidgets.QAction(MainWindow)
        self.LpGBTSaveDefault.setText("LpGBT save setup as default")
        self.LpGBTSaveDefault.triggered.connect(self.SaveFileDefault_LpGBT)

        self.LpGBTSaveAs = QtWidgets.QAction(MainWindow)
        self.LpGBTSaveAs.setText("LpGBT save setup to")
        self.LpGBTSaveAs.triggered.connect(self.SaveFileAs_LpGBT)

        self.menu_2.addAction(self.LpGBTLoadDefault)
        self.menu_2.addAction(self.LpGBTLoadFrom)
        self.menu_2.addAction(self.LpGBTSaveDefault)
        self.menu_2.addAction( self.LpGBTSaveAs)
##########################################################################

        #general functions layout
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 261, 261))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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

        #data rate combobox
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        if self.TDC_inst.enable_high_speed[0] == '1':
            self.comboBox.setCurrentIndex(0)
            self.TDC_inst.run_320M_data_rate()
        if self.TDC_inst.enable_high_speed[0] == '0':
            self.comboBox.setCurrentIndex(1)
            self.TDC_inst.run_160M_data_rate()
        if self.TDC_inst.enable_legacy[0] == '1':
            self.comboBox.setCurrentIndex(2)
            self.TDC_inst.run_80M_data_rate()
        self.comboBox.activated.connect(self.data_rate)

        #trigger mode combobox
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        if self.TDC_inst.enable_trigger[0] == '0':
            self.comboBox_2.setCurrentIndex(0)
        if self.TDC_inst.enable_trigger[0] == '1':
            self.comboBox_2.setCurrentIndex(1)
        self.comboBox_2.activated.connect(self.trigger_mode)

        # format combobox
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.activated.connect(self.format)

        #edge type combobox
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.comboBox_4.activated.connect(self.edge_type)

        #160 phase spinbox
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)
        self.spinBox.setValue(int(format(int(self.TDC_inst.phase_clk160[0], 2), 'd')))
        self.spinBox.valueChanged.connect(self.spinbox_160)

        #320 phase spinbox
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.spinBox_2, 5, 1, 1, 1)
        self.spinBox_2.setValue(int(format(int(self.TDC_inst.phase_clk320_1[0], 2), 'd')))
        self.spinBox_2.valueChanged.connect(self.spinbox_320)

        #JTAG IN layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 30, 160, 271))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        #mode set button
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.open_mode_set)
        #internal counter button
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.open_internal_counter)
        #fine time lut button
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.open_fine_time_lut)
        #reset option button
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.open_reset_option)
        #ePll option button
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_5.clicked.connect(self.open_ePll_option)
        #TDC status button
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_6.clicked.connect(self.open_TDC_status)
        #verificate JTAG button
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_7.clicked.connect(self.verificate_all)

        #TRST and master reset layout
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(610, 45, 161, 100))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        #TRST button
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_8.clicked.connect(self.TRST)
        #master reset checkbox
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.checkBox.toggled.connect(self.master_reset)

        #ASD buttons layout
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(610, 190, 161, 111))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        #ASD0 button
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_10.clicked.connect(self.open_ASD0)
        #ASD1 button
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_11.clicked.connect(self.open_ASD1)
        #ASD2 button
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_12.clicked.connect(self.open_ASD2)

        #init button
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(65, 340, 171, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.init_settings)

        ###########################################################################

        # button for saving CSM config
        self.pushButton_CSM_save = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_CSM_save.setGeometry(QtCore.QRect(50, 20, 191, 41))
        self.pushButton_CSM_save.setText('Save LpGBT')
        self.pushButton_CSM_save.clicked.connect(self.save_LpGBT)

        # button for saving lpGBT status
        self.pushButton_status = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_status.setGeometry(QtCore.QRect(270, 20, 191, 41))
        self.pushButton_status.setText('lpGBT Status')

        #core label
        self.label_core = QtWidgets.QLabel(self.tab_3)
        self.label_core.setGeometry(QtCore.QRect(50, 90, 160, 30))

        #button for ePortTX
        self.pushButton_eportTX = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_eportTX.setGeometry(QtCore.QRect(50, 130, 145, 30))
        # self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_eportTX.setText("ePortTX")
        self.pushButton_eportTX.clicked.connect(self.open_eportTX)

        #button for ePortRX
        self.pushButton_eportRX = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_eportRX.setGeometry(QtCore.QRect(50, 175, 145, 30))
        # self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_eportRX.setText("ePortRX")
        self.pushButton_eportRX.clicked.connect(self.open_eportRX)

        # button for Chip mode
        self.pushButton_Chip_Mode = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Chip_Mode.setGeometry(QtCore.QRect(50, 220, 145, 30))
        # self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_Chip_Mode.setText("Chip Mode")
        self.pushButton_Chip_Mode.clicked.connect(self.open_chip_mode)

        # button for transmitter mode
        self.pushButton_Transmitter_Mode = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Transmitter_Mode.setGeometry(QtCore.QRect(50, 265, 145, 30))
        # self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_Transmitter_Mode.setText("Transmitter Mode")
        self.pushButton_Transmitter_Mode.clicked.connect(self.open_transmitter_mode)

        # Clock label
        self.label_clock = QtWidgets.QLabel(self.tab_3)
        self.label_clock.setGeometry(QtCore.QRect(240, 90, 160, 30))

        #button for ePortClk
        self.pushButton_eportclk = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_eportclk.setGeometry(QtCore.QRect(240, 130, 145, 30))
        self.pushButton_eportclk.setText("ePort Clock")
        self.pushButton_eportclk.clicked.connect(self.open_eportClk)

        #button for phase shifter
        self.pushButton_ps = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_ps.setGeometry(QtCore.QRect(240, 175, 145, 30))
        self.pushButton_ps.setText("Phase Shift Clock")
        self.pushButton_ps.clicked.connect(self.open_phase_shifter)

        # High Speed label
        self.label_HS = QtWidgets.QLabel(self.tab_3)
        self.label_HS.setGeometry(QtCore.QRect(430, 90, 160, 30))

        #button for equalizer
        self.pushButton_equalizer = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_equalizer.setGeometry(QtCore.QRect(430, 130, 145, 30))
        self.pushButton_equalizer.setText("Equalizer")
        self.pushButton_equalizer.clicked.connect(self.open_Equalizer)

        # button for line driver
        self.pushButton_ld = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_ld.setGeometry(QtCore.QRect(430, 175, 145, 30))
        self.pushButton_ld.setText("Line Driver")
        self.pushButton_ld.clicked.connect(self.open_line_driver)

        # button for Chip Config
        self.pushButton_Chip_config = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Chip_config.setGeometry(QtCore.QRect(430, 220, 145, 30))
        self.pushButton_Chip_config.setText("Chip Config")
        self.pushButton_Chip_config.clicked.connect(self.open_chip_config)


        ###########################################################################

        #general printout layout
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 480, 800, 201))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        #general textbrowser
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MiniDAQ GUI"))
        self.menu.setTitle(_translate("MainWindow", "file"))
        self.TDCSaveDefault.setText(_translate("MainWindow", "save TDC setup as default"))
        self.TDCSaveAs.setText(_translate("MainWindow", "save TDC setup to"))
        self.TDCLoadFrom.setText(_translate("MainWindow", "load TDC setup from"))
        self.TDCLoadDefault.setText(_translate("MainWindow", "load TDC default setup"))
        self.ASDSaveDefault.setText(_translate("MainWindow", "save ASD setup as default"))
        self.ASDSaveAs.setText(_translate("MainWindow", "save ASD setup to"))
        self.ASDLoadFrom.setText(_translate("MainWindow", "load ASD setup from"))
        self.ASDLoadDefault.setText(_translate("MainWindow", "load ASD default setup"))
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
        self.comboBox_4.setItemText(0, _translate("MainWindow", "rising"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "falling"))
        self.label_3.setText(_translate("MainWindow", "Format:"))
        self.label_5.setText(_translate("MainWindow", "Clk160_phase: "))
        self.label_4.setText(_translate("MainWindow", "EdgeType:"))
        self.label_6.setText(_translate("MainWindow", "Clk320_1_phase:"))
        self.label_7.setText(_translate("MainWindow", "JTAG IN"))
        # self.label_9.setText(_translate("MainWindow", "ASD setup"))
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
        self.pushButton_10.setText(_translate("MainWindow", "setup_ASD0"))
        self.pushButton_11.setText(_translate("MainWindow", "setup_ASD1"))
        self.pushButton_12.setText(_translate("MainWindow", "setup_ASD2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "TDC"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "CSM"))
        self.label_core.setText(_translate("MainWindow", "Core:"))
        self.label_clock.setText(_translate("MainWindow", "Clocks:"))
        self.label_HS.setText(_translate("MainWindow", "High Speed:"))
        self.label_8.setText(_translate("MainWindow", "GUI run information"))

    #### functions calling to the popup windows  ####
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

    #ASD0
    def open_ASD0(self):
        dialog = QtWidgets.QDialog()
        ASD_name = 'ASD0'
        dialog.ui = Form_14(self.TDC_inst.asd_mezz.ASD0, self.TDC_inst.asd_mezz, ASD_name)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    #ASD1
    def open_ASD1(self):
        dialog = QtWidgets.QDialog()
        ASD_name = 'ASD1'
        dialog.ui = Form_14(self.TDC_inst.asd_mezz.ASD1, self.TDC_inst.asd_mezz, ASD_name)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    # ASD2
    def open_ASD2(self):
        dialog = QtWidgets.QDialog()
        ASD_name = 'ASD2'
        dialog.ui = Form_14(self.TDC_inst.asd_mezz.ASD2, self.TDC_inst.asd_mezz, ASD_name)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_eportTX(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_15(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_eportRX(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_16(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_eportClk(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_17(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_phase_shifter(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_18(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_Equalizer(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_19(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_line_driver(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_20(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_chip_config(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_21(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_chip_mode(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_22(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def open_transmitter_mode(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_23(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()


    ### functions to save values ###
    def verificate_all(self):
        verificate_all(self.ser)

    def data_rate(self):
        if self.comboBox.currentIndex() == 0:
            self.TDC_inst.run_320M_data_rate()
        if self.comboBox.currentIndex() == 1:
            self.TDC_inst.run_160M_data_rate()
        if self.comboBox.currentIndex() == 2:
            self.TDC_inst.run_80M_data_rate()

    def trigger_mode(self):
        if self.comboBox_2.currentIndex() == 0:
            self.TDC_inst.run_triggerless_mode()
        if self.comboBox_2.currentIndex() == 1:
            self.TDC_inst.run_trigger_mode()

    def format(self):
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

    def edge_type(self):
        if self.comboBox_4.currentIndex() == 0:
            self.TDC_inst.set_rising_is_leading()
        if self.comboBox_4.currentIndex() == 1:
            self.TDC_inst.set_falling_is_leading()

    def spinbox_160(self):
        self.phase_clk160_binary = format(self.spinBox.value(), '05b')
        self.TDC_inst.phase_clk160[0] = self.phase_clk160_binary

    def spinbox_320(self):
        self.phase_clk320_0_binary = format(self.spinBox_2.value()+4, '04b')[-4:]
        self.TDC_inst.phase_clk320_0[0] = self.phase_clk320_0_binary

        self.phase_clk320_1_binary = format(self.spinBox_2.value(), '04b')
        self.TDC_inst.phase_clk320_1[0] = self.phase_clk320_1_binary

    #Init button
    def init_settings(self):
        self.TDC_inst.DAQ_init()

    #TRST button
    def TRST(self):
        self.TDC_inst.reset_all_reg()

    #master reset
    def master_reset(self):
        if self.checkBox.isChecked() == True:
            tdc_master_reset_1(self.ser)
            print("master reset 1")
        if self.checkBox.isChecked() == False:
            tdc_master_reset_0(self.ser)
            print("master reset 0")

    #TDC load from
    def loadFileFrom_TDC(self):
        self.val = 1
        current_dir = str(Path.cwd())
        self.fname = QFileDialog.getOpenFileName(caption='open file', directory=current_dir)
        if self.fname[0]:
            self.load_setup_func_TDC()

    #TDC load default
    def loadFileDefault_TDC(self):
        self.val = 0
        self.load_setup_func_TDC()

    def load_setup_func_TDC(self):
        if self.val == 1:
            tree = ET.parse(self.fname[0])
            root = tree.getroot()
            print(self.fname[0] + " loaded")
        if self.val == 0:
            tree = ET.parse('TDC_default.xml')
            root = tree.getroot()
            print(str(Path.cwd()) + '\TDC_default.xml loaded')

        #mode set
        self.TDC_inst.enable_new_ttc[0] = root[0][0].text
        self.TDC_inst.enable_master_reset_code[0] = root[0][1].text
        self.TDC_inst.enable_direct_bunch_reset[0] = root[0][2].text
        self.TDC_inst.enable_direct_trigger[0] = root[0][3].text
        self.TDC_inst.auto_roll_over[0] = root[0][4].text
        self.TDC_inst.bypass_bcr_distribution[0] = root[0][5].text
        self.TDC_inst.enable_trigger[0] = root[0][6].text
        self.TDC_inst.channel_data_debug[0] = root[0][7].text
        self.TDC_inst.enable_leading[0] = root[0][8].text
        self.TDC_inst.enable_pair[0] = root[0][9].text
        self.TDC_inst.enable_fake_hit[0] = root[0][10].text
        self.TDC_inst.enable_trigger_timeout[0] = root[0][11].text
        self.TDC_inst.enable_high_speed[0] = root[0][12].text
        self.TDC_inst.enable_legacy[0] = root[0][13].text
        self.TDC_inst.full_width_res[0] = root[0][14].text
        self.TDC_inst.enable_8b10b[0] = root[0][15].text
        self.TDC_inst.enable_insert[0] = root[0][16].text
        self.TDC_inst.enable_error_packet[0] = root[0][17].text
        self.TDC_inst.enable_TDC_ID[0] = root[0][18].text
        self.TDC_inst.enable_error_notify[0] = root[0][19].text

        # edge_type
        if root[9][0].text == '0':
            self.comboBox_4.setCurrentIndex(1)
            self.TDC_inst.set_falling_is_leading()
        if root[9][0].text == '1':
            self.comboBox_4.setCurrentIndex(0)
            self.TDC_inst.set_rising_is_leading()

        #individual channels
        #rising is leading
        self.rising_is_leading_listing = list(self.TDC_inst.rising_is_leading[0])
        for i in range (24):
            self.rising_is_leading_listing[i] = root[0][22][i].text
        self.TDC_inst.rising_is_leading[0] = ''.join(self.rising_is_leading_listing)
        #channel enable r
        self.channel_enable_r_list = list(self.TDC_inst.channel_enable_r[0])
        for i in range (24):
            self.channel_enable_r_list[i] = root[0][23][i].text
        self.TDC_inst.channel_enable_r[0] = ''.join(self.channel_enable_r_list)
        #channel enable f
        self.channel_enable_f_list = list(self.TDC_inst.channel_enable_f[0])
        for i in range (24):
            self.channel_enable_f_list[i] = root[0][24][i].text
        self.TDC_inst.channel_enable_f[0] = ''.join(self.channel_enable_f_list)

        #TDC_ID
        self.TDC_inst.TDC_ID[0] = root[0][20].text
        self.TDC_inst.width_select[0] = root[0][21].text

        #internal_counter
        for i in range(8):
            self.TDC_inst.setup_1[i][0] = root[1][i].text

        #fine_time_lut
        for i in range(17):
            self.TDC_inst.chnl_decode[i][0] = root[2][i].text

        #reset_option
        for i in range(5):
            self.TDC_inst.reset_control[i][0] = root[3][i].text

        #ePll_option
        for i in range(7):
            self.TDC_inst.ePLL_control[i][0] = root[4][i].text

        #data_rate
        if root[6][0].text == '1':
            self.comboBox.setCurrentIndex(0)
            self.TDC_inst.run_320M_data_rate()
        if root[6][1].text == '1':
            self.comboBox.setCurrentIndex(1)
            self.TDC_inst.run_160M_data_rate()
        if root[6][2].text == '1':
            self.comboBox.setCurrentIndex(2)
            self.TDC_inst.run_80M_data_rate()

        #trigger_mode
        if root[7][0].text == '0':
            self.comboBox_2.setCurrentIndex(0)
            self.TDC_inst.run_triggerless_mode()
        if root[7][0].text == '1':
            self.comboBox_2.setCurrentIndex(1)
            self.TDC_inst.run_trigger_mode()

        #format
        if root[8][0].text == '1':
            self.comboBox_3.setCurrentIndex(0)
            self.TDC_inst.run_pair_mode()
        if root[8][1].text == '1':
            self.comboBox_3.setCurrentIndex(1)
            self.TDC_inst.run_single_edge_mode()
        if root[8][2].text == '1':
            self.comboBox_3.setCurrentIndex(2)
            self.TDC_inst.run_double_edge_mode()
        if root[8][3].text == '1':
            self.comboBox_3.setCurrentIndex(3)
            self.TDC_inst.run_pair_full_width_mode()
        if root[8][4].text == '1':
            self.comboBox_3.setCurrentIndex(4)
            self.TDC_inst.run_debug_mode()
        if root[8][5].text == '1':
            self.comboBox_3.setCurrentIndex(5)
            self.TDC_inst.run_TDCID_mode()

        #clk_160_phase
        self.spinBox.setValue(int(root[10][0].text))
        self.phase_clk160_binary = format(self.spinBox.value(), '05b')
        self.TDC_inst.phase_clk160[0] = self.phase_clk160_binary

        #clk_320_phase
        self.spinBox_2.setValue(int(root[11][0].text))
        self.phase_clk320_0_binary = format(self.spinBox_2.value() + 4, '04b')[-4:]
        self.TDC_inst.phase_clk320_0[0] = self.phase_clk320_0_binary
        self.phase_clk320_1_binary = format(self.spinBox_2.value(), '04b')
        self.TDC_inst.phase_clk320_1[0] = self.phase_clk320_1_binary

    # TDC save to
    def saveFileAs_TDC(self):
        current_dir = str(Path.cwd())
        self.file_name = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", current_dir, '.xml')[0]

        if self.file_name:
            self.save_setup_func_TDC()
            file_2 = open('TDC_auto_saved.xml', 'r')
            data_2 = file_2.read()
            with open(self.file_name, 'w') as f:
                f.write(data_2)
                print("current TDC setup saved to selected directory")
                f.close()

    #TDC default save
    def save_setup_func_TDC(self):
        tree = ET.parse('TDC_default.xml')
        root = tree.getroot()
        file_saved_name_list = ["TDC_saved_", timestr, ".xml"]
        file_saved_name = ''.join(file_saved_name_list)
        #print("current TDC setup saved as: %s" %file_saved_name)
        print('current TDC setup save as: TDC_auto_saved.xml')

        # mode set
        root[0][0].text = self.TDC_inst.enable_new_ttc[0]
        root[0][1].text = self.TDC_inst.enable_master_reset_code[0]
        root[0][2].text = self.TDC_inst.enable_direct_bunch_reset[0]
        root[0][3].text = self.TDC_inst.enable_direct_trigger[0]
        root[0][4].text = self.TDC_inst.auto_roll_over[0]
        root[0][5].text = self.TDC_inst.bypass_bcr_distribution[0]
        root[0][6].text = self.TDC_inst.enable_trigger[0]
        root[0][7].text = self.TDC_inst.channel_data_debug[0]
        root[0][8].text = self.TDC_inst.enable_leading[0]
        root[0][9].text = self.TDC_inst.enable_pair[0]
        root[0][10].text = self.TDC_inst.enable_fake_hit[0]
        root[0][11].text = self.TDC_inst.enable_trigger_timeout[0]
        root[0][12].text = self.TDC_inst.enable_high_speed[0]
        root[0][13].text = self.TDC_inst.enable_legacy[0]
        root[0][14].text = self.TDC_inst.full_width_res[0]
        root[0][15].text = self.TDC_inst.enable_8b10b[0]
        root[0][16].text = self.TDC_inst.enable_insert[0]
        root[0][17].text = self.TDC_inst.enable_error_packet[0]
        root[0][18].text = self.TDC_inst.enable_TDC_ID[0]
        root[0][19].text = self.TDC_inst.enable_error_notify[0]
        root[0][20].text = self.TDC_inst.TDC_ID[0]
        root[0][21].text = self.TDC_inst.width_select[0]

        #individual channels
        self.rising_is_leading_listing = list(self.TDC_inst.rising_is_leading[0])
        self.channel_enable_r_list = list(self.TDC_inst.channel_enable_r[0])
        self.channel_enable_f_list = list(self.TDC_inst.channel_enable_f[0])
        #rising is leading
        for i in range (24):
            root[0][22][i].text = self.rising_is_leading_listing[i]
        #channel enable r
        for i in range (24):
            root[0][23][i].text = self.channel_enable_r_list[i]
        #channel enable f
        for i in range (24):
            root[0][24][i].text = self.channel_enable_f_list[i]

        #internal counter
        for i in range(8):
            root[1][i].text = self.TDC_inst.setup_1[i][0]

        # fine_time_lut
        for i in range(17):
            root[2][i].text = self.TDC_inst.chnl_decode[i][0]

        #reset option
        for i in range(5):
            root[3][i].text = self.TDC_inst.reset_control[i][0]

        #ePll option
        for i in range(7):
            root[4][i].text = self.TDC_inst.ePLL_control[i][0]

        # data_rate
        if self.comboBox.currentIndex() == 0:
            root[6][0].text = '1'
            root[6][1].text = '0'
            root[6][2].text = '0'
        if self.comboBox.currentIndex() == 1:
            root[6][0].text = '0'
            root[6][1].text = '1'
            root[6][2].text = '0'
        if self.comboBox.currentIndex() == 2:
            root[6][0].text = '0'
            root[6][1].text = '0'
            root[6][2].text = '1'

        # trigger_mode
        if self.comboBox_2.currentIndex() == 0:
            root[7][0].text = '0'
        if self.comboBox_2.currentIndex() == 1:
            root[7][0].text = '1'

        # format
        if self.comboBox_3.currentIndex() == 0:
            root[8][0].text = '1'
            root[8][1].text = '0'
            root[8][2].text = '0'
            root[8][3].text = '0'
            root[8][4].text = '0'
            root[8][5].text = '0'
        if self.comboBox_3.currentIndex() == 1:
            root[8][0].text = '0'
            root[8][1].text = '1'
            root[8][2].text = '0'
            root[8][3].text = '0'
            root[8][4].text = '0'
            root[8][5].text = '0'
        if self.comboBox_3.currentIndex() == 2:
            root[8][0].text = '0'
            root[8][1].text = '0'
            root[8][2].text = '1'
            root[8][3].text = '0'
            root[8][4].text = '0'
            root[8][5].text = '0'
        if self.comboBox_3.currentIndex() == 3:
            root[8][0].text = '0'
            root[8][1].text = '0'
            root[8][2].text = '0'
            root[8][3].text = '1'
            root[8][4].text = '0'
            root[8][5].text = '0'
        if self.comboBox_3.currentIndex() == 4:
            root[8][0].text = '0'
            root[8][1].text = '0'
            root[8][2].text = '0'
            root[8][3].text = '0'
            root[8][4].text = '1'
            root[8][5].text = '0'
        if self.comboBox_3.currentIndex() == 5:
            root[8][0].text = '0'
            root[8][1].text = '0'
            root[8][2].text = '0'
            root[8][3].text = '0'
            root[8][4].text = '0'
            root[8][5].text = '1'

        #edge type
        if self.comboBox_4.currentIndex() == 0:
            root[9][0].text = '0'
        if self.comboBox_4.currentIndex() == 1:
            root[9][0].text = '1'

        # clk_160 and clk_320 phase
        root[10][0].text = str(self.spinBox.value())
        root[11][0].text = str(self.spinBox_2.value())

        tree.write('TDC_auto_saved.xml')

    #ASD load default
    def loadFileDefault_ASD(self):
        self.val_2 = 0
        self.load_setup_func_ASD()

    #ASD load from
    def loadFileFrom_ASD(self):
        self.val_2 = 1
        current_dir = str(Path.cwd())
        self.fname_ASD = QFileDialog.getOpenFileName(caption='open file', directory=current_dir)
        if self.fname_ASD[0]:
            self.load_setup_func_ASD()

    def load_setup_func_ASD(self):
        if self.val_2 == 1:
            tree_ASD = ET.parse(self.fname_ASD[0])
            root = tree_ASD.getroot()
            print(self.fname_ASD[0] + " loaded")
        if self.val_2 == 0:
            tree_ASD = ET.parse('ASD_default.xml')
            root = tree_ASD.getroot()
            print(str(Path.cwd()) +'\ASD_default.xml loaded')

        self.ASD_list = [self.TDC_inst.asd_mezz.ASD0, self.TDC_inst.asd_mezz.ASD1, self.TDC_inst.asd_mezz.ASD2]
        self.index = 0
        for ASD in self.ASD_list:
            for i in range(15):
                ASD.setup[i][0] = root[self.index][i].text
            self.index += 1

    #ASD save as
    def saveFileAs_ASD(self):
        current_dir = str(Path.cwd())
        self.file_name_ASD = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", current_dir, '.xml')[0]

        if self.file_name_ASD:
            self.save_setup_func_ASD()
            file_3 = open('ASD_auto_saved.xml', 'r')
            data_3 = file_3.read()
            with open(self.file_name_ASD, 'w') as f:
                f.write(data_3)
                print("current ASD setup saved to selected directory")
                f.close()

    #ASD save default
    def save_setup_func_ASD(self):
        tree = ET.parse('ASD_default.xml')
        root = tree.getroot()
        file_saved_name_list = ["ASD_saved_", timestr, ".xml"]
        file_saved_name = ''.join(file_saved_name_list)
        #print("current TDC setup saved as: %s" %file_saved_name)
        print('current ASD setup save as: ASD_auto_saved.xml')

        self.ASD_list = [self.TDC_inst.asd_mezz.ASD0, self.TDC_inst.asd_mezz.ASD1, self.TDC_inst.asd_mezz.ASD2]
        self.ASD_index = 0
        for ASD in self.ASD_list:
            for i in range(15):
                root[self.ASD_index][i].text = ASD.setup[i][0]
            self.ASD_index += 1

        tree.write('ASD_auto_saved.xml')

    def save_LpGBT(self):   #working on this stuff! ############################################################## 44 #
        ePortTX_writeReg()
        # print("ePortTX values saved")

#######################################################
    def loadFileDefault_LpGBT(self):
        tree_LpGBT = ET.parse('LpGBT_default.xml')
        root = tree_LpGBT.getroot()
        print(str(Path.cwd()) + '\LpGBT_default.xml loaded')
        tree_LpGBT.write('LpGBT_transfer.xml')

    def loadFileFrom_LpGBT(self):
        current_dir = str(Path.cwd())
        self.fname_LpGBT = QFileDialog.getOpenFileName(caption='open file', directory=current_dir)
        if self.fname_LpGBT[0]:
            tree_LpGBT = ET.parse(self.fname_LpGBT[0])
            root = tree_LpGBT.getroot()
            print(self.fname_LpGBT[0] + " loaded")
            tree_LpGBT.write('LpGBT_transfer.xml')

    def SaveFileDefault_LpGBT(self):   # Not sure if I really need to do something else here/if I should actually execute this funciton, it already saves!
        tree_LpGBT = ET.parse('LpGBT_auto_saved.xml')
        root = tree_LpGBT.getroot()
        tree_LpGBT.write('LpGBT_auto_saved.xml')
        print("current LpGBT setup saved as: LpGBT_auto_saved.xml")

    def SaveFileAs_LpGBT(self):
        current_dir = str(Path.cwd())
        self.file_name_LpGBT = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", current_dir, '.xml')[0]

        if self.file_name_LpGBT:
            file_3 = open('LpGBT_auto_saved.xml', 'r')
            data_3 = file_3.read()
            with open(self.file_name_LpGBT, 'w') as f:
                f.write(data_3)
                print("current LpGBT setup saved to selected directory")
                f.close()

########################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())