from PyQt5 import QtCore, QtGui, QtWidgets
from TDC_config_low_level_function import *

class hit_tab(object):
    """docstring for hit_tab"""

    def __init__(self, MainWindow, ser):
        self.hit_enable_chnl = ['111111111111111111111111']
        self.hit_interval = 400
        self.hit_width = 10
        self.hit_delay = 0
        self.hit_inv = 0
        self.ser = ser

        self.setup_UI(MainWindow)
        

    def setup_UI(self, MainWindow):
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 700, 50))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        #checkbox labels (0-23)
        for i in range(24):
            label_num = i
            label = QtWidgets.QLabel()
            self.gridLayout.addWidget(label, 0, i+1, 1, 1)
            label.setText("%d"%i)

        # hit enable checkboxes
        self.checkbox_list = []
        for i in range(24):
            checkBox = QtWidgets.QCheckBox()
            self.gridLayout.addWidget(checkBox, 1, i+1, 1, 1)
            if self.hit_enable_chnl[0][i] == '1':
                checkBox.setChecked(True)
            self.checkbox_list.append(checkBox)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 400, 50))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)

        #Check all button
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("Check All")
        self.gridLayout_2.addWidget(self.pushButton,2,1,1,1)
        self.pushButton.clicked.connect(self.all_hit_chnl_enable)

        #Clear all button
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setText("Clear All")
        self.gridLayout_2.addWidget(self.pushButton_2,2,2,1,1)
        self.pushButton_2.clicked.connect(self.all_hit_chnl_disable)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 200, 400, 200))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label.setText("hit_interval")

        self.spinBox_interval = QtWidgets.QSpinBox()
        self.gridLayout_3.addWidget(self.spinBox_interval, 0, 1, 1, 1)
        self.spinBox_interval.setMaximum(10000)
        self.spinBox_interval.setValue(self.hit_interval)

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        self.label.setText("160MHz/interval")

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label.setText("hit_width")

        self.spinBox_width = QtWidgets.QSpinBox()
        self.gridLayout_3.addWidget(self.spinBox_width, 1, 1, 1, 1)
        self.spinBox_width.setMaximum(10000)
        self.spinBox_width.setValue(self.hit_width)

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 1, 2, 1, 1)
        self.label.setText("(width+1)*6.25ns")

        self.label_2 = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_2.setText("hit_delay")

        self.spinBox_delay = QtWidgets.QSpinBox()
        self.gridLayout_3.addWidget(self.spinBox_delay, 2, 1, 1, 1)
        self.spinBox_delay.setMaximum(10000)
        self.spinBox_delay.setValue(self.hit_delay)

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 2, 2, 1, 1)
        self.label.setText("delay*6.25ns")

        self.label = QtWidgets.QLabel()
        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)
        self.label.setText("hit inverted")

        self.checkbox_inv = QtWidgets.QCheckBox()
        self.gridLayout_3.addWidget(self.checkbox_inv, 3, 1, 1, 1)
        self.checkbox_inv.setChecked(True if self.hit_inv == 1 else False)

        self.pushButton_hit_update = QtWidgets.QPushButton()
        self.pushButton_hit_update.setText("Update Hit Property")
        self.gridLayout_3.addWidget(self.pushButton_hit_update,4,0,1,1)
        self.pushButton_hit_update.clicked.connect(self.update_hit_property)

        self.pushButton_hit_start = QtWidgets.QPushButton()
        self.pushButton_hit_start.setText("Hit Start")
        self.gridLayout_3.addWidget(self.pushButton_hit_start,5,0,1,1)
        self.pushButton_hit_start.clicked.connect(self.hit_start_c)

        self.pushButton_hit_stop = QtWidgets.QPushButton()
        self.pushButton_hit_stop.setText("Hit Stop")
        self.gridLayout_3.addWidget(self.pushButton_hit_stop,5,1,1,1)
        self.pushButton_hit_stop.clicked.connect(self.hit_stop_c)

        self.pushButton_single_hit = QtWidgets.QPushButton()
        self.pushButton_single_hit.setText("Single Hit")
        self.gridLayout_3.addWidget(self.pushButton_single_hit,5,2,1,1)
        self.pushButton_single_hit.clicked.connect(self.single_hit_c)

        


    def all_hit_chnl_enable(self):
        for i in self.checkbox_list:
            i.setChecked(True)


    def all_hit_chnl_disable(self):
        for i in self.checkbox_list:
            i.setChecked(False)

    def update_hit_property(self):
        update_hit_interval(self.ser,self.spinBox_interval.value())
        update_hit_width(self.ser,self.spinBox_width.value())  
        update_inv_hit(self.ser,self.checkbox_inv.isChecked())
        update_hit_delay(self.ser,self.spinBox_delay.value())
        enable_list = list(self.hit_enable_chnl[0])
        for i in range(24):
            enable_list[23-i] = '1' if self.checkbox_list[i].isChecked() else '0'
        self.hit_enable_chnl[0] = ''.join(enable_list)
        update_hit_mask_hit(self.ser,self.hit_enable_chnl[0])
        print("Hit properties updated!")
        print("Interval="+str(self.spinBox_interval.value())
            +" width="+str(self.spinBox_width.value())
            +" delay="+str(self.spinBox_delay.value())
            +" inverted="+str(self.checkbox_inv.isChecked())
            +" hit_mask="+self.hit_enable_chnl[0])


    def hit_start_c(self):   
        hit_start(self.ser)    
        print("Hit Start!")

    def hit_stop_c(self):
        hit_stop(self.ser)
        print("Hit Stop!")

    def single_hit_c(self):
        start_single_hit(self.ser)
        print("Single hit sent!")

        
