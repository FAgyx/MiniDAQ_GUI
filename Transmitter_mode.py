from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET

class Ui_Dialog(object):

    def __init__(self, TDC_inst):
        self.TDC_inst = TDC_inst

    def setupUi(self, Dialog):

        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 230)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.label.setObjectName("label")
        # self.label.setText("Transmitter Mode")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 241, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        ##########################################
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 241, 65))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Apply
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save)

        # OK
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(Dialog.reject)

        # Cancel
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(Dialog.reject)

        ########### loading xml default ##########
        if root[3][0].text == '0x0':
            self.comboBox.setCurrentIndex(0)
        if root[3][0].text == '0x1':
            self.comboBox.setCurrentIndex(1)

        if root[3][1].text == '0x0':
            self.comboBox_2.setCurrentIndex(0)
        if root[3][1].text == '0x1':
            self.comboBox_2.setCurrentIndex(1)
        ##########################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Transmitter Mode:"))
        self.label_3.setText(_translate("Dialog", "Tx Encoding:"))
        self.label_2.setText(_translate("Dialog", "Tx Data Rate:"))
        self.comboBox.setItemText(0, _translate("Dialog", "5 Gbps "))
        self.comboBox.setItemText(1, _translate("Dialog", "10 Gbps"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "FEC5"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "FEC12"))
        self.pushButton.setText(_translate("Dialog", "Apply"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))

    def save(self):
        print("in progress")
        import xml.etree.ElementTree as ET
        # tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
        tree_ePortTX = ET.parse('LpGBT_transfer.xml')
        root = tree_ePortTX.getroot()

        if self.comboBox.currentIndex() == 0:
            root[3][0].text = '0x0'
        if self.comboBox.currentIndex() == 1:
            root[3][0].text = '0x1'

        if self.comboBox_2.currentIndex() == 0:
            root[3][1].text = '0x0'
        if self.comboBox_2.currentIndex() == 1:
            root[3][1].text = '0x1'

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