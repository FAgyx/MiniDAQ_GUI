import serial
from TDC_config_low_level_function import *
from serial_config_tdc import *
from TDCreg import *
ser = serial.Serial( port='COM5', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.01)
TDC0 = TDCreg(ser)

tdc_high_speed(ser)
update_data_length(ser, 4)
tdc_trigger_mode(ser)
update_input_deserial_para(ser)
reselect_input_deserial(ser)


verificate_pass_TD_CODE = verificate_ID_CODE(ser)
verificate_pass_setup0 = verificate_setup0(ser)
verificate_pass_setup1 = verificate_setup1(ser)
verificate_pass_setup2 = verificate_setup2(ser)
verificate_pass_control0 = verificate_control0(ser)
verificate_pass_control1 = verificate_control1(ser)
# verificate_pass_spi = verificate_spi(ser)


trst_0(ser)
trst_1(ser)

tdc_master_reset_1(ser)
tdc_master_reset_0(ser)





TDC0.reset_setup_0()
TDC0.reset_setup_1()
TDC0.enable_trigger[0] = '1'
TDC0.enable_fake_hit[0] = '1'



# TDC0.match_window[0] = '000000010011'
TDC0.match_window[0] = '000000001011'
TDC0.bunch_offset[0] = '000000000000'
# TDC0.match_window[0] = '000000111111'
TDC0.update_setup_0()
TDC0.update_setup_1()



tdc_master_reset_1(ser)
tdc_master_reset_0(ser)

update_ttc_delay(ser, 1)
ttc_mode_select(ser, 0)
enable_ttc_trigger(ser)
# enable_ttc_event_reset(ser)
single_TTC(ser)

# ###################### start hit #########################
update_hit_width(ser,1)
update_inv_hit(ser,'notinv')
update_hit_delay(ser,0)
update_hit_mask_hit(ser,'\xFF\xFF\xFF')
# start_single_hit(ser)

update_hit_interval(ser,150)
hit_start(ser)
hit_stop(ser)