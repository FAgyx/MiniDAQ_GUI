import serial
import time
import sys
from TDC_config_low_level_function import *


ser = serial.Serial( port='COM6', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.01)

# verificate ID code
trst_1(ser)
update_config_period(0,ser)
update_JTAG_inst('\x09',ser)
update_bit_length(5,ser)
update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05',ser)
start_action(ser)


ser.close()