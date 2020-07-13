#from test_5 import Ui_MainWindow
from MainWindow_TDC_update import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
import serial
sys.path.insert(0, "../UART_py3")
from TDCreg import *
from serial_config_tdc import *

########################################################
#fun()
########################################################

class StartQT5(QtWidgets.QMainWindow):
    def __init__(self, ser, TDC_inst, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow(ser, TDC_inst)
        self.ui.setupUi(self)

class OutLog:
    def __init__(self, edit, out=None, color=None):
        """(edit, out=None, color=None) -> can write stdout, stderr to a
        QTextEdit.
        edit = QTextEdit
        out = alternate stream ( can be the original sys.stdout )
        color = alternate color (i.e. color stderr a different color)
        """
        self.edit = edit
        self.out = None
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
#
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ser = serial.Serial(port='COM5', baudrate = 115200, bytesize = serial.EIGHTBITS,
                        parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)


    TDC_inst = TDCreg(ser)

    #verificate_all(ser)
    #TDC_inst.update_setup_0()
    #TDC_inst.read_status_0()
    #TDC_inst.read_status_1()
    #TDC_inst.update_control_1()
    #TDC_inst.update_control_1()
    #print(TDC_inst.control_1_indictor)
    #TDC_inst.DAQ_init()

    myapp = StartQT5(ser, TDC_inst)
    myapp.show()
    sys.stdout = OutLog(myapp.ui.textBrowser, sys.stdout)
    sys.exit(app.exec_())