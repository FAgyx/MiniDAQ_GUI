# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datarate_popup_2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


############## data rate popup script #############

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(318, 260)

        #Vertical layout 
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 281, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #reselect dline checkbox
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        #Data rate label
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        #combobox for datarate 
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("run_320M_data_rate")
        self.comboBox.addItem("run_160M_data_rate")
        self.comboBox.addItem("run_80M_data_rate")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox.currentIndexChanged.connect(self.changed)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        #Save button
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save_button)
        self.pushButton.clicked.connect(Dialog.reject)

        #enabling message to print on TDC tab
        self.message = self.comboBox.currentText()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Data Rate"))
        self.checkBox.setText(_translate("Dialog", "Reselect dline"))
        self.label.setText(_translate("Dialog", "Data Rate:"))
        self.pushButton.setText(_translate("Dialog", "Save"))

    #Function for the combobox 
    def changed(self):
        self.message = self.comboBox.currentText()

    def save_button(self):
        if self.comboBox.currentIndex() == 0:
            self.TDC_inst.run_320M_data_rate()
        if self.comboBox.currentIndex() == 1:
            self.TDC_inst.run_160M_data_rate()
        if self.comboBox.currentIndex() == 2:
            self.TDC_inst.run_80M_data_rate()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
