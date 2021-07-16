# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup1_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

################ setup1 popup script ####################
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 420)

        #Main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 351, 331))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        #combine_time_out_config
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit.setText(format(int(self.TDC_inst.combine_time_out_config[0],2),'03X'))
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        #fake_hit_time_interval
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_2.setText(format(int(self.TDC_inst.fake_hit_time_interval[0], 2), '03X'))
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        #syn_packet_number
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_3.setText(format(int(self.TDC_inst.syn_packet_number[0], 2), '03X'))
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        #roll_over
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_4.setText(format(int(self.TDC_inst.roll_over[0], 2), '03X'))
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        #coarse_count_offset
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_5.setText(format(int(self.TDC_inst.coarse_count_offset[0], 2), '03X'))
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        #bunch_offset
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_6, 5, 0, 1, 1)
        self.lineEdit_6.setText(format(int(self.TDC_inst.bunch_offset[0], 2), '03X'))
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        #event_offset
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_7, 6, 0, 1, 1)
        self.lineEdit_7.setText(format(int(self.TDC_inst.event_offset[0], 2), '03X'))
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)

        #match_window
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)
        self.lineEdit_8.setText(format(int(self.TDC_inst.match_window[0], 2), '03X'))
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)

        #bottom button stuff
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 360, 351, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        #Apply button
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.apply_button)

        #OK button
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.OK_button)
        self.pushButton_2.clicked.connect(Dialog.reject)

        #Cancel button
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

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
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    #apply button
    def apply_button(self):
        self.save()

    #Ok button
    def OK_button(self):
        self.save()

    def save(self):
        self.lineEdit_binary = format(int(self.lineEdit.text(), 16), '010b')
        self.lineEdit_2_binary = format(int(self.lineEdit_2.text(), 16), '012b')
        self.lineEdit_3_binary = format(int(self.lineEdit_3.text(), 16), '012b')
        self.lineEdit_4_binary = format(int(self.lineEdit_4.text(), 16), '012b')
        self.lineEdit_5_binary = format(int(self.lineEdit_5.text(), 16), '012b')
        self.lineEdit_6_binary = format(int(self.lineEdit_6.text(), 16), '012b')
        self.lineEdit_7_binary = format(int(self.lineEdit_7.text(), 16), '012b')
        self.lineEdit_8_binary = format(int(self.lineEdit_8.text(), 16), '012b')

        self.TDC_inst.combine_time_out_config[0] = self.lineEdit_binary
        self.TDC_inst.fake_hit_time_interval[0] = self.lineEdit_2_binary
        self.TDC_inst.syn_packet_number[0] = self.lineEdit_3_binary
        self.TDC_inst.roll_over[0] = self.lineEdit_4_binary
        self.TDC_inst.coarse_count_offset[0] = self.lineEdit_5_binary
        self.TDC_inst.bunch_offset[0] = self.lineEdit_6_binary
        self.TDC_inst.event_offset[0] = self.lineEdit_7_binary
        self.TDC_inst.match_window[0] = self.lineEdit_8_binary

        #call update_setup_1 function
        self.TDC_inst.update_setup_1()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
