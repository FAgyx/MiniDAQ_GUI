# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chip_config.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET

# tree_ePortTX = ET.parse('LpGBT_default.xml')
# root = tree_ePortTX.getroot()

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst
        # self.CSM_inst = CSM_inst

    def setupUi(self, Dialog):

        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 293)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 31))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 70, 321, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 219, 321, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        ################# xml file loading ###############
        # High speed data output
        if root[8][0].text == '0x1':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

        # High speed data input
        if root[8][1].text == '0x1':
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)

        # Chip address (unsure)
        ###################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #testing
        # self.checkBox_2.setChecked(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Chip Configuration:"))
        self.label_2.setText(_translate("Dialog", "Invert High Speed Data Output:"))
        self.label_3.setText(_translate("Dialog", "Invert High Speed Data Input:"))
        self.label_4.setText(_translate("Dialog", "Chip Address:"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    def save(self):
        print('in progress')
        import xml.etree.ElementTree as ET
        # tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        #High speed data output
        if self.checkBox.isChecked() == True:
            root[8][0].text = '0x1'
        else:
            root[8][0].text = '0x0'

        #High speed data input
        if self.checkBox_2.isChecked() == True:
            root[8][1].text = '0x1'
        else:
            root[8][1].text = '0x0'

        # Chip address (unsure)

        tree_ePortTX.write('LpGBT_auto_saved.xml')
        tree_ePortTX.write('LpGBT_transfer.xml')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
