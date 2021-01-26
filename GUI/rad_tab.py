from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from TDC_config_low_level_function import *
from crc8_D81 import *
from StyleSheet import *


class rad_tab(object):
    """docstring for rad_tab"""

    def __init__(self, MainWindow, TDC_inst):
        self.TDC_inst = TDC_inst
        self.refresh_rate = 1
        self.processing = False
        self.setup_UI(MainWindow)
        # self.threadpool = QThreadPool()
        

    def setup_UI(self, MainWindow):
        
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        #CRC_cal
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("CRC_cal")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_CRC_cal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_CRC_cal, 0, 1, 1, 1)
        self.label_CRC_cal.setText(crc_cal(self.TDC_inst))

        #CRC
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("CRC_JTAG")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_CRC_JTAG = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_CRC_JTAG, 1, 1, 1, 1)
        self.label_CRC_JTAG.setText(format(int(self.TDC_inst.CRC[0], 2), '08X'))   

        #CRC status
        # instruction error
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("CRC_Status")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_CRC_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.label_CRC_status, 2, 1, 1, 1)
        self.label_CRC_status.setStyleSheet(LedRed)

        #update_CRC
        self.pushButton_update_CRC = QtWidgets.QPushButton()
        self.pushButton_update_CRC.setText("Update CRC")
        self.gridLayout.addWidget(self.pushButton_update_CRC,3,0,1,1)
        self.pushButton_update_CRC.clicked.connect(self.update_CRC)

        #CRC_monitor start
        self.pushButton_start_monitor = QtWidgets.QPushButton()
        self.pushButton_start_monitor.setText("Start Monitoring")
        self.gridLayout.addWidget(self.pushButton_start_monitor,4,0,1,1)
        self.pushButton_start_monitor.clicked.connect(self.start_monitor)
        #CRC_monitor stop
        self.pushButton_stop_monitor = QtWidgets.QPushButton()
        self.pushButton_stop_monitor.setText("Stop Monitoring")
        self.gridLayout.addWidget(self.pushButton_stop_monitor,4,1,1,1)
        self.pushButton_stop_monitor.clicked.connect(self.stop_monitor)



    def update_CRC(self):
        self.TDC_inst.read_status_0()
        crc_cal_tmp = crc_cal(self.TDC_inst)
        # print(crc_cal_tmp)
        crc_jtag = format(int(self.TDC_inst.CRC[0], 2), '08X')
        # print(crc_jtag)
        self.label_CRC_cal.setText(crc_cal_tmp)
        self.label_CRC_JTAG.setText(crc_jtag)
        self.label_CRC_status.setStyleSheet(LedGreen if crc_cal_tmp==crc_jtag else LedRed)

    def start_monitor(self):    

        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()
        self.pushButton_start_monitor.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.pushButton_start_monitor.setEnabled(True)
        )

    def stop_monitor(self):
        self.processing = False

class Worker(QObject):
    """docstring for Worker"""

    finished = pyqtSignal()

    def __init__(self, rad_tab):
        super(Worker, self).__init__()
        self.rad_tab = rad_tab

    def run(self):       
        self.rad_tab.processing = True         
        crc_cal_tmp = crc_cal(self.rad_tab.TDC_inst)  
        print("Monitoring JTAG CRC started!")      
        while self.rad_tab.processing:
            self.rad_tab.TDC_inst.read_status_0()
            crc_jtag = format(int(self.rad_tab.TDC_inst.CRC[0], 2), '08X')
            self.rad_tab.label_CRC_JTAG.setText(crc_jtag)
            if crc_cal_tmp==crc_jtag:
                self.rad_tab.label_CRC_status.setStyleSheet(LedGreen)
            else:
                self.rad_tab.label_CRC_status.setStyleSheet(LedRed)
            time.sleep(1)
        print("Monitoring stopped.")
        self.finished.emit()

        




