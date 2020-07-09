# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


############ channel popup script #################

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 400)

        #main grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 631, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #Enabling all channels checkbox
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 1, 1, 1)
        self.checkBox.clicked.connect(self.checked_box)

        #All of the channels 
        #Channel 1
        self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 2, 1, 1, 1)
        self.checkBox_1.clicked.connect(self.checked_box_1)

        #Channel 2 
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)
        self.checkBox_2.clicked.connect(self.checked_box_2)

        #channel 3
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 3, 1, 1)
        self.checkBox_3.clicked.connect(self.checked_box_3)

        #channel 4
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 2, 4, 1, 1)
        self.checkBox_4.clicked.connect(self.checked_box_4)

        #channel 5
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 4, 1, 1, 1)
        self.checkBox_5.clicked.connect(self.checked_box_5)

        #channel 6
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 4, 2, 1, 1)
        self.checkBox_6.clicked.connect(self.checked_box_6)

        #channel 7
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 4, 3, 1, 1)
        self.checkBox_7.clicked.connect(self.checked_box_7)

        #channel 8
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 4, 4, 1, 1)
        self.checkBox_8.clicked.connect(self.checked_box_8)

        #channel 9 
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 5, 1, 1, 1)
        self.checkBox_9.clicked.connect(self.checked_box_9)

        #channel 10
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 5, 2, 1, 1)
        self.checkBox_10.clicked.connect(self.checked_box_10)

        #channel 11 
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout.addWidget(self.checkBox_11, 5, 3, 1, 1)
        self.checkBox_11.clicked.connect(self.checked_box_11)

        #channel 12 
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 5, 4, 1, 1)
        self.checkBox_12.clicked.connect(self.checked_box_12)

        #channel 13 
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 6, 1, 1, 1)
        self.checkBox_13.clicked.connect(self.checked_box_13)

        #channel 14 
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout.addWidget(self.checkBox_14, 6, 2, 1, 1)
        self.checkBox_14.clicked.connect(self.checked_box_14)

        #channel 15
        self.checkBox_15 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout.addWidget(self.checkBox_15, 6, 3, 1, 1)
        self.checkBox_15.clicked.connect(self.checked_box_15)

        #channel 16 
        self.checkBox_16 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout.addWidget(self.checkBox_16, 6, 4, 1, 1)
        self.checkBox_16.clicked.connect(self.checked_box_16)

        #channel 17 
        self.checkBox_17 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout.addWidget(self.checkBox_17, 7, 1, 1, 1)
        self.checkBox_17.clicked.connect(self.checked_box_17)

        #channel 18 
        self.checkBox_18 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout.addWidget(self.checkBox_18, 7, 2, 1, 1)
        self.checkBox_18.clicked.connect(self.checked_box_18)

        #channel 19 
        self.checkBox_19 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout.addWidget(self.checkBox_19, 7, 3, 1, 1)
        self.checkBox_19.clicked.connect(self.checked_box_19)

        #channel 20 
        self.checkBox_20 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout.addWidget(self.checkBox_20, 7, 4, 1, 1)
        self.checkBox_20.clicked.connect(self.checked_box_20)

        #channel 21 
        self.checkBox_21 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout.addWidget(self.checkBox_21, 10, 1, 1, 1)
        self.checkBox_21.clicked.connect(self.checked_box_21)

        #channel 22
        self.checkBox_22 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout.addWidget(self.checkBox_22, 10, 2, 1, 1)
        self.checkBox_22.clicked.connect(self.checked_box_22)

        #channel 23 
        self.checkBox_23 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout.addWidget(self.checkBox_23, 10, 3, 1, 1)
        self.checkBox_23.clicked.connect(self.checked_box_23)

        #channel 24 
        self.checkBox_24 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout.addWidget(self.checkBox_24, 10, 4, 1, 1)
        self.checkBox_24.clicked.connect(self.checked_box_24)



        #Other stuff here
        #Enable specific channels label 
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        #General vertical layout for Save Button
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 310, 631, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Save button
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(Dialog.reject)

        ## Tring out the list->string way, but it isn't working out exactly as planned, it will just re-print out channels.
        #self.message = []
        #self.message_string = ''.join(self.message)

        #enabeling the messages to print on the TDC tab
        self.message = ""
        self.message_1 = ""
        self.message_2 = ""
        self.message_3 = ""
        self.message_4 = ""
        self.message_5 = ""
        self.message_6 = ""
        self.message_7 = ""
        self.message_8 = ""
        self.message_9 = ""
        self.message_10 = ""
        self.message_11 = ""
        self.message_12 = ""
        self.message_13 = ""
        self.message_14 = ""
        self.message_15 = ""
        self.message_16 = ""
        self.message_17 = ""
        self.message_18 = ""
        self.message_19 = ""
        self.message_20 = ""
        self.message_21 = ""
        self.message_22 = ""
        self.message_23 = ""
        self.message_24 = ""

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Enable all Channels"))
        self.label.setText(_translate("Dialog", "Enable Specific Channels: "))

        self.checkBox_1.setText(_translate("Dialog", "Channel 1"))
        self.checkBox_2.setText(_translate("Dialog", "Channel 2"))
        self.checkBox_3.setText(_translate("Dialog", "Channel 3"))
        self.checkBox_4.setText(_translate("Dialog", "Channel 4"))
        self.checkBox_5.setText(_translate("Dialog", "Channel 5"))
        self.checkBox_6.setText(_translate("Dialog", "Channel 6"))
        self.checkBox_7.setText(_translate("Dialog", "Channel 7"))
        self.checkBox_8.setText(_translate("Dialog", "Channel 8"))
        self.checkBox_9.setText(_translate("Dialog", "Channel 9"))
        self.checkBox_10.setText(_translate("Dialog", "Channel 10"))
        self.checkBox_11.setText(_translate("Dialog", "Channel 11"))
        self.checkBox_12.setText(_translate("Dialog", "Channel 12"))
        self.checkBox_13.setText(_translate("Dialog", "Channel 13"))
        self.checkBox_14.setText(_translate("Dialog", "Channel 14"))
        self.checkBox_15.setText(_translate("Dialog", "Channel 15"))
        self.checkBox_16.setText(_translate("Dialog", "Channel 16"))
        self.checkBox_17.setText(_translate("Dialog", "Channel 17"))
        self.checkBox_18.setText(_translate("Dialog", "Channel 18"))
        self.checkBox_19.setText(_translate("Dialog", "Channel 19"))
        self.checkBox_20.setText(_translate("Dialog", "Channel 20"))
        self.checkBox_21.setText(_translate("Dialog", "Channel 21"))
        self.checkBox_22.setText(_translate("Dialog", "Channel 22"))
        self.checkBox_23.setText(_translate("Dialog", "Channel 23"))
        self.checkBox_24.setText(_translate("Dialog", "Channel 24"))

        self.pushButton.setText(_translate("Dialog", "Save"))


    #more of the list to string method, again doesn't exactly work as planned (maybe useful for something else though??)
    #def checked_box(self): 
    #    if self.checkBox_2.isChecked() == True:
    #        self.message.append("Channel 1")
    #        self.message_string = ''.join(self.message)
    #    if self.checkBox_3.isChecked() == True: 
    #        self.message.append("Channel 2")
    #        self.message_string = ' '.join(self.message)


    #Functions for the checkboxes
    #enabling all the channels 
    def checked_box(self): 
        if self.checkBox.isChecked() == True:
            self.message = "All channels enabled    "
        else:
            self.message = ""

    #enabling each channel individually 
    def checked_box_1(self): 
        if self.checkBox_1.isChecked() == True:
            self.message_1 = "Channel 1   "
        else:
            self.message_1 = ""

    def checked_box_2(self): 
        if self.checkBox_2.isChecked() == True: 
            self.message_2 = "Channel 2   "
        else: 
            self.message_2 = ""

    def checked_box_3(self): 
        if self.checkBox_3.isChecked() == True: 
            self.message_3 = "Channel 3   "
        else: 
            self.message_3 = ""

    def checked_box_4(self): 
        if self.checkBox_4.isChecked() == True: 
            self.message_4 = "Channel 4   "
        else: 
            self.message_4 = ""

    def checked_box_5(self): 
        if self.checkBox_5.isChecked() == True: 
            self.message_5 = "Channel 5   "
        else: 
            self.message_5 = ""

    def checked_box_6(self): 
        if self.checkBox_6.isChecked() == True: 
            self.message_6 = "Channel 6   "
        else: 
            self.message_6 = ""

    def checked_box_7(self): 
        if self.checkBox_7.isChecked() == True: 
            self.message_7 = "Channel 7   "
        else: 
            self.message_7 = ""

    def checked_box_8(self): 
        if self.checkBox_8.isChecked() == True: 
            self.message_8 = "Channel 8   "
        else: 
            self.message_8 = ""

    def checked_box_9(self): 
        if self.checkBox_9.isChecked() == True: 
            self.message_9 = "Channel 9   "
        else: 
            self.message_9 = ""

    def checked_box_10(self): 
        if self.checkBox_10.isChecked() == True:
            self.message_10 = "Channel 10  "
        else:
            self.message_10 = ""

    def checked_box_11(self): 
        if self.checkBox_11.isChecked() == True: 
            self.message_11 = "Channel 11  "
        else: 
            self.message_11 = ""

    def checked_box_12(self): 
        if self.checkBox_12.isChecked() == True: 
            self.message_12 = "Channel 12  "
        else: 
            self.message_12 = ""

    def checked_box_13(self): 
        if self.checkBox_13.isChecked() == True: 
            self.message_13 = "Channel 13  "
        else: 
            self.message_13 = ""

    def checked_box_14(self): 
        if self.checkBox_14.isChecked() == True: 
            self.message_14 = "Channel 14  "
        else: 
            self.message_14 = ""

    def checked_box_15(self): 
        if self.checkBox_15.isChecked() == True: 
            self.message_15 = "Channel 15  "
        else: 
            self.message_15 = ""

    def checked_box_16(self): 
        if self.checkBox_16.isChecked() == True: 
            self.message_16 = "Channel 16  "
        else: 
            self.message_16 = ""

    def checked_box_17(self): 
        if self.checkBox_17.isChecked() == True: 
            self.message_17 = "Channel 17  "
        else: 
            self.message_17 = ""

    def checked_box_18(self): 
        if self.checkBox_18.isChecked() == True: 
            self.message_18 = "Channel 18  "
        else: 
            self.message_18 = ""

    def checked_box_19(self): 
        if self.checkBox_19.isChecked() == True:
            self.message_19 = "Channel 19  "
        else:
            self.message_19 = ""

    def checked_box_20(self): 
        if self.checkBox_20.isChecked() == True: 
            self.message_20 = "Channel 20  "
        else: 
            self.message_20 = ""

    def checked_box_21(self): 
        if self.checkBox_21.isChecked() == True: 
            self.message_21 = "Channel 21  "
        else: 
            self.message_21 = ""

    def checked_box_22(self): 
        if self.checkBox_22.isChecked() == True: 
            self.message_22 = "Channel 22  "
        else: 
            self.message_22 = ""

    def checked_box_23(self): 
        if self.checkBox_23.isChecked() == True: 
            self.message_23 = "Channel 23  "
        else: 
            self.message_23 = ""

    def checked_box_24(self): 
        if self.checkBox_24.isChecked() == True: 
            self.message_24 = "Channel 24  "
        else: 
            self.message_24 = ""


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
