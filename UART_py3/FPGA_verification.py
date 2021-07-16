import serial
from TDC_config_low_level_function import *
from serial_config_tdc import *
from TDCreg import *
# if used in linux, uncomment the initialization below and choose the right device
# ser = serial.Serial( port='/dev/ttyUSB0', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)

# if used in windows, uncomment the initialization below and choose the right device
ser = serial.Serial(port='COM4', baudrate = 115200, bytesize = serial.EIGHTBITS,parity =serial.PARITY_EVEN, stopbits = serial.STOPBITS_ONE, timeout=0.1)

TDC0 = TDCreg(ser)
TDC0.DAQ_init()
TDC0.update_periodic_hit()
# #
# verificate_pass_TD_CODE = verificate_ID_CODE(ser)
# verificate_pass_setup0 = verificate_setup0(ser)
# verificate_pass_setup1 = verificate_setup1(ser)
# verificate_pass_setup2 = verificate_setup2(ser)
# verificate_pass_control0 = verificate_control0(ser)
# verificate_pass_control1 = verificate_control1(ser)
# verificate_pass_spi = verificate_spi(ser)
# #
# #
# # #ASD_config(ser, 5, '\x15')
# #
#
# trst_0(ser)
# trst_1(ser)
#
# #chip 1 14 10101
# #chip 8: 31 3
# TDC0.set_ePLL_phase(clk_160_phase=31, clk_320_phase=4)
# TDC0.run_320M_data_rate()
# # TDC0.run_80M_data_rate()
# # TDC0.run_160M_data_rate()
# TDC0.reselect_dline()   # select the right dline phase
#
# TDC0.run_triggerless_mode()
# # TDC0.run_trigger_mode(100)
#
#
# # TDC0.enable_legacy_ttc()
#
# # TDC0.disable_8b10b()
#
#
# # TDC0.run_pair_full_width_mode()
# # TDC0.config_pairing_timeout(1023)  # time = input*6.25ns, maximum input 1023
# # TDC0.run_idle_insert_mode(10)
# # TDC0.run_error_insert_mode()
# # TDC0.config_TDCID(0x1abcd)
# # TDC0.run_TDCID_mode()
# # TDC0.run_pair_mode()  # LSB = (2^input)*0.78125ns, Range = (2^input)*200ns
# TDC0.run_single_edge_mode()
# # TDC0.run_double_edge_mode()
#
#
#
# # TDC0.rising_is_leading[0]='111111111111111111111111'#rising
# TDC0.rising_is_leading[0]='000000000000000000000000'#falling
# TDC0.channel_enable_r[0] ='000000000000000000000000'
# TDC0.channel_enable_f[0] ='000000000000000000000000'
# TDC0.update_setup_0()
# tdc_master_reset_1(ser)
# tdc_master_reset_0(ser)
#
#
# update_hit_width(ser,10)  # width_time = width*6.25 ns, minimum 6.25ns
# update_inv_hit(ser,'notinv')
# update_hit_delay(ser,0)
# update_hit_mask_hit(ser,'\x00\x00\x01')
# # start_single_hit(ser)
#
# #
# update_hit_interval(ser,200)   # hit rate = 160MHz/interval
# hit_start(ser)
# hit_stop(ser)
#
#
# # enable_ttc_trigger(ser)
# # update_ttc_interval(ser,800)
# # # start_ttc(ser)
# # # TDC0.single_trigger()
# # # TDC0.event_reset()
# # stop_ttc(ser)
#
#
#
#
#
# # TDC0.event_reset_jtag_in[0] = '1'
# # TDC0.update_control_0()
# # TDC0.event_reset_jtag_in[0] = '0'
# # TDC0.update_control_0()
#
# # #
# # # new TTC master reset single
# # TDC0.reset_setup_0()
# # TDC0.enable_new_ttc[0]='1'
# # TDC0.enable_master_reset_code[0] = '1'
# # TDC0.update_setup_0()
# # update_ttc_delay(ser, 1)
# # ttc_mode_select(ser, 1)
# # update_new_ttc_code(ser, '\x09')
# # single_TTC(ser)
# # # new TTC master reset repeat
# # update_ttc_interval(ser, 50)
# # start_ttc(ser)
# # stop_ttc(ser)
# #
# # # legacy TTC master reset single
# # TDC0.reset_setup_0()
# # TDC0.enable_new_ttc[0]='0'
# # TDC0.enable_master_reset_code[0] = '1'
# # TDC0.update_setup_0()
# # update_ttc_delay(ser, 1)
# # ttc_mode_select(ser, 0)
# # enable_ttc_master_reset(ser)
# # single_TTC(ser)
# # # legacy TTC master reset repeat
# # update_ttc_interval(ser, 50)
# # start_ttc(ser)
# # stop_ttc(ser)
# #
# #
# # #bcr auto roll over
# # TDC0.reset_setup_0()
# # TDC0.auto_roll_over[0] = '1'
# # TDC0.roll_over[0] = '000001000000'
# # TDC0.bunch_offset[0] = '000000000000'
# # TDC0.update_setup_0()
# # TDC0.update_setup_1()
# #

