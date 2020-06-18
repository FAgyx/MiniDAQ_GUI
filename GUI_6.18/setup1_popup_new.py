# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup1_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


################ setup1 popup script ####################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 420)

        #Main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 351, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #combine_time_out_config
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit.textChanged.connect(self.changed_line1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        #fake_hit_time_interval
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_2.textChanged.connect(self.changed_line2)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        #syn_packet_number
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_3.textChanged.connect(self.changed_line3)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        #roll_over
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_4.textChanged.connect(self.changed_line4)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        #coarse_count_offset
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_5.textChanged.connect(self.changed_line5)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        #bunch_offset
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 0, 1, 1)
        self.lineEdit_6.textChanged.connect(self.changed_line6)

        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        #event_offset
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 0, 1, 1)
        self.lineEdit_7.textChanged.connect(self.changed_line7) 

        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)       

        #match_window
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)
        self.lineEdit_8.textChanged.connect(self.changed_line8)

        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)


        #Save button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 360, 351, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.reject)

        #enabling the messages to print on the TDC tab
        self.message_1 = ""
        self.message_2 = ""
        self.message_3 = ""
        self.message_4 = ""
        self.message_5 = ""
        self.message_6 = ""
        self.message_7 = ""
        self.message_8 = ""

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setup1"))
        self.label_4.setText(_translate("Dialog", "roll_over"))
        self.label_6.setText(_translate("Dialog", "bunch_offset"))
        self.label_5.setText(_translate("Dialog", "coarse_count_offset"))
        self.label_3.setText(_translate("Dialog", "Syn_packet_number"))
        self.label_7.setText(_translate("Dialog", "event_offset"))
        self.label_8.setText(_translate("Dialog", "match_window"))
        self.label.setText(_translate("Dialog", "combine_time_out_config"))
        self.label_2.setText(_translate("Dialog", "fake_hit_time_interval"))
        self.pushButton.setText(_translate("Dialog", "Run setup1"))

    #Functions for the line edits 
    def changed_line1(self): 
        self.message_1 = "combine_time_out_config: " + self.lineEdit.text() + "    "

    def changed_line2(self): 
       self.message_2 = "fake_hit_time_interval: " + self.lineEdit_2.text() + "    "

    def changed_line3(self): 
        self.message_3 = "syn_packet_number: " + self.lineEdit_3.text() + "    "

    def changed_line4(self): 
        self.message_4 = "roll_over: " + self.lineEdit_4.text() + "    "

    def changed_line5(self): 
        self.message_5 = "coarse_count_offset: " + self.lineEdit_5.text() + "    "

    def changed_line6(self): 
        self.message_6 = "bunch_offset: " + self.lineEdit_6.text() + "    "

    def changed_line7(self): 
        self.message_7 = " event_offset: " + self.lineEdit_7.text() + "    "

    def changed_line8(self): 
        self.message_8 = "match_window: " + self.lineEdit_8.text() + "    "


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
