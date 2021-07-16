# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup2_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


################ setup2 popup script ###################
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 500)


        #Main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 301, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #fine_sel
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit.setText(self.TDC_inst.fine_sel[0])
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        #lut0
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_2.setText(self.TDC_inst.lut0[0])
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        # lut1
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_3.setText(self.TDC_inst.lut1[0])
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        # lut2
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_4.setText(self.TDC_inst.lut2[0])
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        # lut3
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.lineEdit_5.setText(self.TDC_inst.lut3[0])
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        # lut4
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.lineEdit_6.setText(self.TDC_inst.lut4[0])
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        # lut5
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.lineEdit_7.setText(self.TDC_inst.lut5[0])
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        # lut6
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.lineEdit_8.setText(self.TDC_inst.lut6[0])
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        # lut7
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_9, 0, 3, 1, 1)
        self.lineEdit_9.setText(self.TDC_inst.lut7[0])
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        # lut8
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_10, 1, 3, 1, 1)
        self.lineEdit_10.setText(self.TDC_inst.lut8[0])
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)

        # lut9
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_11, 2, 3, 1, 1)
        self.lineEdit_11.setText(self.TDC_inst.lut9[0])
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        # luta
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_12, 3, 3, 1, 1)
        # self.lineEdit_12.setText(self.TDC_inst.luta[0])
        self.lineEdit_12.setText(self.TDC_inst.chnl_decode[11][0])
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)

        # lutb
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_13, 4, 3, 1, 1)
        # self.lineEdit_13.setText(self.TDC_inst.lutb[0])
        self.lineEdit_13.setText(self.TDC_inst.chnl_decode[12][0])
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)

        # lutc
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_14, 5, 3, 1, 1)
        # self.lineEdit_14.setText(self.TDC_inst.lutc[0])
        self.lineEdit_14.setText(self.TDC_inst.chnl_decode[13][0])
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)

        # lutd
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_15, 6, 3, 1, 1)
        self.lineEdit_15.setText(self.TDC_inst.lutd[0])
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 2, 1, 1)

        # lute
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_16, 7, 3, 1, 1)
        self.lineEdit_16.setText(self.TDC_inst.lute[0])
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 2, 1, 1)

        # lutf
        self.lineEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.lineEdit_17, 8, 3, 1, 1)
        self.lineEdit_17.setText(self.TDC_inst.lutf[0])
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 2, 1, 1)

        # bottom button stuff
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(20, 440, 301, 31))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

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
        Dialog.setWindowTitle(_translate("Dialog", "Setup2"))
        self.label.setText(_translate("Dialog", "fine_sel"))
        self.label_2.setText(_translate("Dialog", "lut0"))
        self.label_3.setText(_translate("Dialog", "lut1"))
        self.label_4.setText(_translate( "Dialog", "lut2"))
        self.label_5.setText(_translate("Dialog", "lut3"))
        self.label_6.setText(_translate("Dialog", "lut4"))
        self.label_7.setText(_translate("Dialog", "lut5"))
        self.label_8.setText(_translate("Dialog", "lut6"))
        self.label_9.setText(_translate("Dialog", "lut7"))
        self.label_10.setText(_translate("Dialog", "lut8"))
        self.label_11.setText(_translate("Dialog", "lut9"))
        self.label_12.setText(_translate("Dialog", "luta"))
        self.label_13.setText(_translate("Dialog", "lutb"))
        self.label_14.setText(_translate("Dialog", "lutc"))
        self.label_15.setText(_translate("Dialog", "lutd"))
        self.label_16.setText(_translate("Dialog", "lute"))
        self.label_17.setText(_translate("Dialog", "lutf"))
        self.pushButton.setText(_translate("Dialog", "Run setup2"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    #apply button
    def apply_button(self):
        self.save()

    #OK button
    def OK_button(self):
        self.save()
        # print(self.TDC_inst.chnl_decode[0][0])

    #save changes
    def save(self):
        self.TDC_inst.fine_sel[0] = self.lineEdit.text()
        self.TDC_inst.lut0[0] = self.lineEdit_2.text()
        self.TDC_inst.lut1[0] = self.lineEdit_3.text()
        self.TDC_inst.lut2[0] = self.lineEdit_4.text()
        self.TDC_inst.lut3[0] = self.lineEdit_5.text()
        self.TDC_inst.lut4[0] = self.lineEdit_6.text()
        self.TDC_inst.lut5[0] = self.lineEdit_7.text()
        self.TDC_inst.lut6[0] = self.lineEdit_8.text()
        self.TDC_inst.lut7[0] = self.lineEdit_9.text()
        self.TDC_inst.lut8[0] = self.lineEdit_10.text()
        self.TDC_inst.lut9[0] = self.lineEdit_11.text()
        self.TDC_inst.luta[0] = self.lineEdit_12.text()
        self.TDC_inst.lutb[0] = self.lineEdit_13.text()
        self.TDC_inst.lutc[0] = self.lineEdit_14.text()
        self.TDC_inst.lutd[0] = self.lineEdit_15.text()
        self.TDC_inst.lute[0] = self.lineEdit_16.text()
        self.TDC_inst.lutf[0] = self.lineEdit_17.text()

        #Call update_setup_2 function
        self.TDC_inst.update_setup_2()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
