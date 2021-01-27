#from test_5 import Ui_MainWindow
from MainWIndow_addASD_condensed import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import serial
sys.path.insert(0, "../UART_py3")
from TDCreg import *
from serial_config_tdc import *
import logging
from PyQt5.QtCore import *



class StartQT5(QtWidgets.QMainWindow):
    def __init__(self, ser, TDC_inst, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow(ser, TDC_inst)
        self.logfile = open('log.txt','a')
        self.ui.setupUi(self)


    def normalOutputWritten(self,text):
        self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.ui.textBrowser.insertPlainText(text)
        self.logfile.write(text)

class OutLog:
    def __init__(self, edit, out=None, color=None):
        """(edit, out=None, color=None) -> can write stdout, stderr to a
        QTextEdit.
        edit = QTextEdit
        out = alternate stream ( can be the original sys.stdout )
        color = alternate color (i.e. color stderr a different color)
        """
        self.edit = edit
        self.out = out
        self.color = color

    def write(self, m):
        # if self.color:
        #     tc = self.edit.textColor()
        #     self.edit.setTextColor(self.color)
        # e = datetime.datetime.now()
        # m = "%s %s %s %s:%s:%s>>" %(e.month, e.day, e.year, e.hour, e.minute, e.second) + m
        # m = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ">>" + m
        self.edit.moveCursor(QtGui.QTextCursor.End)
        if m == '\n' :
            self.edit.insertPlainText(m)
        else:
            self.edit.insertPlainText(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ">>")
            self.edit.insertPlainText(m)
        # if self.color:
        #     self.edit.setTextColor(tc)
        if self.out:
            self.out.write(m)

    def flush(self):
        pass
#

class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        if text == '\n' :
            text = text
        else:
            text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ">>" + text
        self.textWritten.emit(str(text))

    def flush(self):
        pass

#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ser = serial.Serial(port='COM3', baudrate = 115200, bytesize = serial.EIGHTBITS,
                        parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)


    TDC_inst = TDCreg(ser)

    myapp = StartQT5(ser, TDC_inst)
    myapp.show()

    # sys.stderr = OutLog(myapp.ui.textBrowser, sys.stderr)
    # sys.stdout = OutLog(myapp.ui.textBrowser, sys.stdout)
    sys.stdout = EmittingStream(textWritten=myapp.normalOutputWritten)
    # logging.basicConfig(format="%(message)s",level=logging.INFO,stream=sys.stdout)
    sys.exit(app.exec_())