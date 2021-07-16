import serial
from TDC_config_low_level_function import *
from serial_config_tdc import *
from TDCreg import *
ser = serial.Serial( port='COM9', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.01)
TDC0 = TDCreg(ser)

tdc_high_speed(ser)
update_data_length(ser, 4)
tdc_triggerless_mode(ser)
update_input_deserial_para(ser)
reselect_input_deserial(ser)


verificate_pass_TD_CODE = verificate_ID_CODE(ser)
verificate_pass_setup0 = verificate_setup0(ser)
verificate_pass_setup1 = verificate_setup1(ser)
verificate_pass_setup2 = verificate_setup2(ser)
verificate_pass_control0 = verificate_control0(ser)
verificate_pass_control1 = verificate_control1(ser)
verificate_pass_spi = verificate_spi(ser)







######################################  new ttc mode test ############################################################

trst_0(ser)
trst_1(ser)
TDC0.auto_roll_over[0] = '0'
TDC0.enable_new_ttc[0]='1'
TDC0.update_setup_0()
tdc_master_reset_1(ser)
tdc_master_reset_0(ser)

update_ttc_delay(ser, 1)
ttc_mode_select(ser, 1)
update_new_ttc_code(ser, '\x0e')


update_ttc_interval(ser,7)
#Note: 
	# 1. interverl has to be larger than 3
	# 2. The maxmin coarse counter you can find is (intervel + 1)*2 -1
	# 3. Please using randhit through VIO.


start_ttc(ser)
# stop_ttc(ser)


######################################  legacy ttc mode test ############################################################
trst_0(ser)
trst_1(ser)
TDC0.auto_roll_over[0] = '0'
TDC0.enable_new_ttc[0]='0'
TDC0.update_setup_0()
tdc_master_reset_1(ser)
tdc_master_reset_0(ser)


update_ttc_delay(ser, 1)
ttc_mode_select(ser, 0)
enable_ttc_BCR(ser)
update_ttc_interval(ser,15)
#Note: 
	# 1. interval has to be larger than 15
	# 1.1 interval will ruond up of 4. For examplr, 16, 17, 18 and 19 is the same as 19 
	# 2. The maxmin coarse counter you can find is (intervel + 1)*2 -1
	# 3. Please using randhit through VIO.


start_ttc(ser)
# stop_ttc(ser)