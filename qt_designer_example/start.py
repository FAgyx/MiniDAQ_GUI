from test import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class StartQT5(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = StartQT5()
	myapp.show()
	sys.exit(app.exec_())