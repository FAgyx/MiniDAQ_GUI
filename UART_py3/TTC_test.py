import serial
from TDC_config_low_level_function import *
from serial_config_tdc import *
from TDCreg import *
ser = serial.Serial( port='COM5', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.01)
TDC0 = TDCreg(ser)


verificate_pass_TD_CODE = verificate_ID_CODE(ser)
verificate_pass_setup0 = verificate_setup0(ser)
verificate_pass_setup1 = verificate_setup1(ser)
verificate_pass_setup2 = verificate_setup2(ser)
verificate_pass_control0 = verificate_control0(ser)
verificate_pass_control1 = verificate_control1(ser)
verificate_pass_spi = verificate_spi(ser)


trst_0(ser)
trst_1(ser)
TDC0.phase_clk160[0]='10000'
TDC0.phase_clk320_0[0]='1100'
TDC0.phase_clk320_1[0]='1000'
TDC0.update_control_1()
tdc_master_reset_1(ser)
tdc_master_reset_0(ser)

tdc_high_speed(ser)
update_data_length(ser, 4)
tdc_triggerless_mode(ser)
update_input_deserial_para(ser)
reselect_input_deserial(ser)

# ###################### start hit #########################
update_hit_width(ser,1)
update_inv_hit(ser,'notinv')
update_hit_delay(ser,0)
# update_hit_mask_hit(ser,'\xFF\xFF\xFF')
update_hit_mask_hit(ser,'\x00\x00\x01')
# start_single_hit(ser)

update_hit_interval(ser,20)
hit_start(ser)
# hit_stop(ser)


# ###################### new TTC master reset #########################
# new TTC master reset single
TDC0.reset_setup_0()
TDC0.enable_new_ttc[0]='1'
TDC0.enable_master_reset_code[0] = '1'
TDC0.update_setup_0()
update_ttc_delay(ser, 1)
ttc_mode_select(ser, 1)
update_new_ttc_code(ser, '\x09')
single_TTC(ser)

# trigger 0_DErr for TTC in tdc_data_interface

# new TTC master reset repeat
update_ttc_interval(ser, 50)
start_ttc(ser)
stop_ttc(ser)

# ###################### legacy TTC master reset #########################
# legacy TTC master reset single
TDC0.reset_setup_0()
TDC0.enable_new_ttc[0]='0'
TDC0.enable_master_reset_code[0] = '1'
TDC0.update_setup_0()
update_ttc_delay(ser, 1)
ttc_mode_select(ser, 0)
enable_ttc_master_reset(ser)
single_TTC(ser)

# trigger 0_DErr for TTC in tdc_data_interface

# legacy TTC master reset repeat
update_ttc_interval(ser, 50)
start_ttc(ser)
stop_ttc(ser)


# ###################### bcr auto roll over #########################
#
TDC0.reset_setup_0()
TDC0.reset_setup_1()
TDC0.auto_roll_over[0] = '1'
TDC0.roll_over[0] = '111111111111'
TDC0.coarse_count_offset[0] = '000000000000'
TDC0.update_setup_0()
TDC0.update_setup_1()

# change roll_over[0] to see coarse counter MSB

# ###################### TTC new bcr #########################
#
TDC0.reset_setup_0()
TDC0.reset_setup_1()
TDC0.enable_new_ttc[0]='1'
# bcr with coarse count offset
TDC0.auto_roll_over[0] = '0'
TDC0.bypass_bcr_distribution[0] = '0'
# #by pass mode
# TDC0.bypass_bcr_distribution[0] = '1'
TDC0.update_setup_0()
TDC0.update_setup_1()
update_ttc_delay(ser, 1)
ttc_mode_select(ser, 1)
update_new_ttc_code(ser, '\x0C')
update_ttc_interval(ser, 200)
start_ttc(ser)
stop_ttc(ser)


# ###################### TTC legacy bcr #########################
TDC0.reset_setup_0()
TDC0.reset_setup_1()
TDC0.enable_new_ttc[0]='0'
# bcr with coarse count offset
TDC0.auto_roll_over[0] = '0'
TDC0.bypass_bcr_distribution[0] = '0'
# #by pass mode
# TDC0.bypass_bcr_distribution[0] = '1'
TDC0.update_setup_0()
TDC0.update_setup_1()
update_ttc_delay(ser, 1)
ttc_mode_select(ser, 0)
enable_ttc_BCR(ser)
update_ttc_interval(ser, 200)
start_ttc(ser)
stop_ttc(ser)
