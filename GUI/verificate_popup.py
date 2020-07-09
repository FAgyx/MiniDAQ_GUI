# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


###### verificate TDC options popup script #######

from PyQt5 import QtCore, QtGui, QtWidgets
#import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 470)

        #Main vertical layout
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 90, 311, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Verificate_ID_code checkbox 
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox.clicked.connect(self.checked_box)

        #Verificate_setup0 checkbox
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_3.clicked.connect(self.checked_box_3)

        #Verificate_setup1 checkbox
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_4.clicked.connect(self.checked_box_4)

        #Verificate_setup2 checkbox
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_2.clicked.connect(self.checked_box_2)

        #Verificate_control0 checkbox
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_6.clicked.connect(self.checked_box_6)

        #Verificate_control1 checkbox
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_5.clicked.connect(self.checked_box_5)

        #Verificate_spi checkbox
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_7.clicked.connect(self.checked_box_7)

        #get_status0 checkbox
        self.checkBox_8 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_8.clicked.connect(self.checked_box_8)

        #get_status1 checkbox
        self.checkBox_10 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.checkBox_10.clicked.connect(self.checked_box_10)

        #upper vertical layout
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 361, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #Run all verificate TDC functions
        self.checkBox_9 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_2.addWidget(self.checkBox_9)
        self.checkBox_9.clicked.connect(self.checked_box_9)


        #The Save button at the bottom
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(19, 390, 351, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton.clicked.connect(Dialog.reject)

        #enabling the messages to print on the TDC tab
        self.message_1 = ""
        self.message_3 = ""
        self.message_4 = ""
        self.message_2 = ""
        self.message_6 = ""
        self.message_5 = ""
        self.message_7 = ""
        self.message_8 = ""
        self.message_9 = ""
        self.message_10 = ""

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Verificate TDC"))
        self.checkBox.setText(_translate("Dialog", "Verificate_ID_Code"))
        self.checkBox_3.setText(_translate("Dialog", "Verificate_setup0"))
        self.checkBox_4.setText(_translate("Dialog", "Verificate_setup1"))
        self.checkBox_2.setText(_translate("Dialog", "Verificate_setup2"))
        self.checkBox_6.setText(_translate("Dialog", "Verificate_control0"))
        self.checkBox_5.setText(_translate("Dialog", "Verificate_control1"))
        self.checkBox_7.setText(_translate("Dialog", "Verificate_spi"))
        self.checkBox_8.setText(_translate("Dialog", "get_status0"))
        self.checkBox_10.setText(_translate("Dialog", "get_status1"))
        self.checkBox_9.setText(_translate("Dialog", "Run All Verificate TDC Functions"))
        self.label.setText(_translate("Dialog", "Select Verificate funciton:"))
        self.pushButton.setText(_translate("Dialog", "Save"))


    #Functions for the checkboxes
    #Verificate_ID_code
    def checked_box(self): 
        if self.checkBox.isChecked() == True:
            self.message_1 = "Verificate_ID_Code  "
        else:
            self.message_1 = ""

    #Verificate_setup0
    def checked_box_3(self): 
        if self.checkBox_3.isChecked() == True: 
            self.message_3 = "Verificate_setup0  "
        else: 
            self.message_3 = ""

    #Verificate_setup1
    def checked_box_4(self): 
        if self.checkBox_4.isChecked() == True: 
            self.message_4 = "Verificate_setup1  "
        else: 
            self.message_4 = ""

    #Verificate_setup2
    def checked_box_2(self): 
        if self.checkBox_2.isChecked() == True: 
            self.message_2 = "Verificate_setup2  "
        else: 
            self.message_2 = ""

    #Verificate_control0
    def checked_box_6(self): 
        if self.checkBox_6.isChecked() == True: 
            self.message_6 = "Verificate_control0  "
        else: 
            self.message_6 = ""

    #Verificate_control1
    def checked_box_5(self): 
        if self.checkBox_5.isChecked() == True: 
            self.message_5 = "Verificate_control1  "
        else: 
            self.message_5 = ""

    #Verificate_spi
    def checked_box_7(self): 
        if self.checkBox_7.isChecked() == True: 
            self.message_7 = "Verificate_spi  "
        else: 
            self.message_7 = ""

    #get_status0
    def checked_box_8(self): 
        if self.checkBox_8.isChecked() == True: 
            self.message_8 = "get_status0  "
        else: 
            self.message_8 = ""

    #get_status1
    def checked_box_10(self): 
        if self.checkBox_10.isChecked() == True: 
            self.message_10 = "get_status1  "
        else: 
            self.message_10 = ""

    #Run all verificate TDC functions
    def checked_box_9(self):
        if self.checkBox_9.isChecked() == True: 
            self.message_9 = "All verificate TDC options  "
        else: 
            self.message_9 = ""


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        sys.exit(Dialog)
