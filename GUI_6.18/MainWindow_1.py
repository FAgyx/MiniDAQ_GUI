# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!



####### This is the script for the main window!          #######
####### all other python files get read through this     #######


import sys
from PyQt5 import * 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

# Importing the popup windows
from verificate_popup import Ui_Dialog as Form
from register_popup import Ui_Dialog as Form_1
from ePLL_popup import Ui_Dialog as Form_2
from datarate_popup_2_new import Ui_Dialog as Form_3
from runmode_popup_2_new import Ui_Dialog as Form_4
from wordmode_popup_2_new import Ui_Dialog as Form_5
from edgetype_popup_2_new import Ui_Dialog as Form_6
from channel_popup import Ui_Dialog as Form_7
from setup0_popup_new import Ui_Dialog as Form_8
from setup1_popup_new import Ui_Dialog as Form_9
from setup2_popup_new import Ui_Dialog as Form_10 
from control0_popup_new import Ui_Dialog as Form_11
from control1_popup_new import Ui_Dialog as Form_12

# import UART functions
sys.path.insert(0, "../UART_py3")

from serial_config_tdc import *



class Ui_MainWindow(object):
    #setting up the main window and tabs
    def __init__(self, ser = None, TDC_inst = ""):
    #def __init__(self, ser, TDC_inst):
        self.ser = ser
        self.TDC_inst = TDC_inst



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 670))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(300, 30, 231, 41))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        #setting up the grid layout in tab 2
        #main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 730, 500))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #upper layout 
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 730, 90))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Main layout parameters 
        #Verificate TDC
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 2)
        self.pushButton_2.clicked.connect(self.open_dialog)

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 1, 2, 1, 1)

        #ePLL Phase 
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 2)
        self.pushButton_3.clicked.connect(self.open_dialog_3)

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 2, 2, 1, 1)

        #Data rate
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 2)
        self.pushButton_4.clicked.connect(self.open_dialog_4)

        self.textBrowser_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 3, 2, 1, 1)

        #Run mode
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 2)
        self.pushButton_5.clicked.connect(self.open_dialog_5)

        self.textBrowser_13 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout.addWidget(self.textBrowser_13, 5, 2, 1, 1)

        #Word mode
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 6, 0, 1, 2)
        self.pushButton_7.clicked.connect(self.open_dialog_6)

        self.textBrowser_14 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.gridLayout.addWidget(self.textBrowser_14, 6, 2, 1, 1)

        #Edge type
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 7, 0, 1, 2)
        # self.pushButton_8.clicked.connect(self.open_dialog_7)
        self.pushButton_8.clicked.connect(self.printsth)

        self.textBrowser_15 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.gridLayout.addWidget(self.textBrowser_15, 7, 2, 1, 1)

        #Channel enable
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 8, 0, 1, 2)
        self.pushButton_9.clicked.connect(self.open_dialog_8)

        self.textBrowser_16 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.gridLayout.addWidget(self.textBrowser_16, 8, 2, 1, 1)

        #General Functions label
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        #Resulting specifications label 
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)


        #Register Select operations
        #Label 
        self.label_register = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_register.setObjectName("label_register")
        self.horizontalLayout.addWidget(self.label_register)

        #Register Select buttons
        #setup0
        self.registerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout.addWidget(self.registerButton)
        self.registerButton.clicked.connect(self.open_dialog_reg_1)

        #setup1
        self.registerButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton_2.setObjectName("registerButton_2")
        self.horizontalLayout.addWidget(self.registerButton_2)
        self.registerButton_2.clicked.connect(self.open_dialog_reg_2)

        #setup2
        self.registerButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton_3.setObjectName("registerButton_3")
        self.horizontalLayout.addWidget(self.registerButton_3)
        self.registerButton_3.clicked.connect(self.open_dialog_reg_3)

        #control0
        self.registerButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton_4.setObjectName("registerButton_4")
        self.horizontalLayout.addWidget(self.registerButton_4)
        self.registerButton_4.clicked.connect(self.open_dialog_reg_4)

        #control1
        self.registerButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.registerButton_5.setObjectName("registerButton_5")
        self.horizontalLayout.addWidget(self.registerButton_5)
        self.registerButton_5.clicked.connect(self.open_dialog_reg_5)

        self.tabWidget.addTab(self.tab_2, "")

        #Print box on the main page (not on TDC tab)
        #Layout
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 685, 730, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #label 
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        #main print textBrowser
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 1, 0, 1, 1)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 18))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General tab"))
        self.pushButton_2.setText(_translate("MainWindow", "Verificate TDC Options"))
        self.pushButton_3.setText(_translate("MainWindow", "Set ePLL Phase"))
        self.pushButton_7.setText(_translate("MainWindow", "Word Mode"))
        self.pushButton_8.setText(_translate("MainWindow", "Edge Type"))
        self.pushButton_9.setText(_translate("MainWindow", "Channel Enable"))
        self.pushButton_4.setText(_translate("MainWindow", "Data Rate"))
        self.pushButton_5.setText(_translate("MainWindow", "Run Mode"))
        self.label_3.setText(_translate("MainWindow", "General Functions: "))
        self.label_5.setText(_translate("MainWindow", "Resutling Specifications:"))
        self.label_register.setText(_translate("MainWindow", "Detailed options:"))
        self.registerButton.setText(_translate("MainWindow", "Setup 0"))
        self.registerButton_2.setText(_translate("MainWindow", "Setup 1"))
        self.registerButton_3.setText(_translate("MainWindow", "Setup 2"))
        self.registerButton_4.setText(_translate("MainWindow", "Control 0"))
        self.registerButton_5.setText(_translate("MainWindow", "Control 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "TDC"))
        self.label_2.setText(_translate("MainWindow", "GUI run information and Print() content: "))

    #### These are the functions calling to the popup windows  ####

    #For the Registers
    #Setup0
    def open_dialog_reg_1(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_8(self.TDC_inst)
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.ui.pushButton.clicked: 
            self.textBrowser_2.setText("Setup0 Run   " + dialog.ui.message_1 + dialog.ui.message_2 + 
                dialog.ui.message_3 + dialog.ui.message_4 + dialog.ui.message_5 + dialog.ui.message_6 
                + dialog.ui.message_7 + dialog.ui.message_8 + dialog.ui.message_9 + dialog.ui.message_10
                + dialog.ui.message_11 + dialog.ui.message_12 + dialog.ui.message_13 + dialog.ui.message_14
                + dialog.ui.message_15 + dialog.ui.message_16 + dialog.ui.message_17 + dialog.ui.message_18
                + dialog.ui.message_19 + dialog.ui.message_20 + dialog.ui.message_21 + dialog.ui.message_22 
                + dialog.ui.message_23 + dialog.ui.message_24 + dialog.ui.message_25 + dialog.ui.message_26)
        dialog.show()

    #Setup1
    def open_dialog_reg_2(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_9()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.ui.pushButton.clicked:
            self.textBrowser_2.setText("Setup1 Run    " + dialog.ui.message_1 + dialog.ui.message_2 + 
                dialog.ui.message_3 + dialog.ui.message_4 + dialog.ui.message_5 + 
                dialog.ui.message_6 + dialog.ui.message_7 + dialog.ui.message_8)
        dialog.show()

    #Setup2
    def open_dialog_reg_3(self): 
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_10()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.ui.pushButton.clicked: 
            self.textBrowser_2.setText("Setup2 Run   " + dialog.ui.message_1 + dialog.ui.message_2)
        dialog.show()

    #Control0
    def open_dialog_reg_4(self): 
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_11()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.ui.pushButton.clicked: 
            self.textBrowser_2.setText("Control0 Run    " + dialog.ui.message_1 + dialog.ui.message_2
             + dialog.ui.message_3 + dialog.ui.message_4 + dialog.ui.message_5)
        dialog.show()

    #Control1
    def open_dialog_reg_5(self): 
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_12()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        if dialog.ui.pushButton.clicked: 
            self.textBrowser_2.setText("Control1 Run    " + dialog.ui.message_1 + dialog.ui.message_2
             + dialog.ui.message_3 + dialog.ui.message_4 + dialog.ui.message_5 + dialog.ui.message_6
             + dialog.ui.message_7 )
        dialog.show()


    #For the general functions 
    #Verificate TDC
    def open_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_3.setText(dialog.ui.message_9 + dialog.ui.message_1 +
         dialog.ui.message_3 + dialog.ui.message_4 + dialog.ui.message_2 + dialog.ui.message_6 
         + dialog.ui.message_5 + dialog.ui.message_7 + dialog.ui.message_8 + dialog.ui.message_10)
        dialog.show()


    #ePLL phase
    def open_dialog_3(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_2()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_4.setText(dialog.ui.message_set)
        dialog.show()


    #Data rate
    def open_dialog_4(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_3()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_6.setText(dialog.ui.message)
        dialog.show()

    #Run mode
    def open_dialog_5(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_4()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_13.setText(dialog.ui.message)
        dialog.show()

    #word mode
    def open_dialog_6(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_5()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_14.setText(dialog.ui.message)
        dialog.show()

    #edge type
    def open_dialog_7(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_6()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_15.setText(dialog.ui.message)
        dialog.show()

    #channel enable 
    def open_dialog_8(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Form_7()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        self.textBrowser_16.setText(dialog.ui.message + dialog.ui.message_1 + dialog.ui.message_2 + dialog.ui.message_3 + dialog.ui.message_4 
            + dialog.ui.message_5 + dialog.ui.message_6 + dialog.ui.message_7 + dialog.ui.message_8 + dialog.ui.message_9 
            + dialog.ui.message_10 + dialog.ui.message_11 + dialog.ui.message_12 + dialog.ui.message_13 + dialog.ui.message_14
            + dialog.ui.message_15 + dialog.ui.message_16 + dialog.ui.message_17 + dialog.ui.message_18 + dialog.ui.message_19 
            + dialog.ui.message_20 + dialog.ui.message_21 + dialog.ui.message_22 + dialog.ui.message_23 + dialog.ui.message_24)
        dialog.show()


    def printsth(self):
        verificate_ID_CODE(self.ser)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #Dialog = QtWidgets.QDialog()
    #ui = Ui_MainWindow()
    #ui.setupUi(Dialog)
    #Dialog.show()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())