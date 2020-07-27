import xml.etree.ElementTree as ET
from xml.dom import minidom

def generateXML(fileName):
	configuration = ET.Element('configuration')

	#mode_set variables 
	mode_set = ET.SubElement(configuration, 'mode_set')
	enable_new_ttc = ET.SubElement(mode_set, 'enable_new_ttc')
	enable_new_ttc.text = '0'
	enable_master_reset_code = ET.SubElement(mode_set, 'enable_master_reset_code')
	enable_master_reset_code.text = '0'
	enable_direct_bunch_reset = ET.SubElement(mode_set, 'enable_direct_bunch_reset')
	enable_direct_bunch_reset.text = '0'
	enable_direct_trigger = ET.SubElement(mode_set, 'enable_direct_trigger')
	enable_direct_trigger.text = '0'
	auto_roll_over = ET.SubElement(mode_set, 'auto_roll_over')
	auto_roll_over.text = '1'
	bypass_bcr_distribution = ET.SubElement(mode_set, 'bypass_bcr_distribution')
	bypass_bcr_distribution.text = '0'
	enable_trigger = ET.SubElement(mode_set, 'enable_trigger')
	enable_trigger.text = '0'
	channel_data_debug = ET.SubElement(mode_set, 'channel_data_debug')
	channel_data_debug.text = '0'
	enable_leading = ET.SubElement(mode_set, 'enable_leading')
	enable_leading.text = '0'
	enable_pair = ET.SubElement(mode_set, 'enable_pair')
	enable_pair.text = '1'
	enable_fake_hit = ET.SubElement(mode_set, 'enable_fake_hit')
	enable_fake_hit.text = '0'
	enable_trigger_timeout = ET.SubElement(mode_set, 'enable_trigger_timeout')
	enable_trigger_timeout.text = '0'
	enable_high_speed = ET.SubElement(mode_set, 'enable_high_speed')
	enable_high_speed.text = '1'
	enable_legacy = ET.SubElement(mode_set, 'enable_legacy')
	enable_legacy.text = '0'
	full_width_res = ET.SubElement(mode_set, 'full_width_res')
	full_width_res.text = '0'
	enable_8b10b = ET.SubElement(mode_set, 'enable_8b10b')
	enable_8b10b.text = '1'
	enable_insert = ET.SubElement(mode_set, 'enable_insert')
	enable_insert.text = '0'
	enable_error_packet = ET.SubElement(mode_set, 'enable_error_packet')
	enable_error_packet.text = '0'
	enable_TDC_ID = ET.SubElement(mode_set, 'enable_TDC_ID')
	enable_TDC_ID.text = '0'
	enable_error_notify = ET.SubElement(mode_set, 'enable_error_notify')
	enable_error_notify.text = '0'

	rising_is_leading = ET.SubElement(mode_set, 'rising_is_leading')
	channel_0 = ET.SubElement(rising_is_leading, 'channel_0')
	channel_0.text = '1'
	channel_1 = ET.SubElement(rising_is_leading, 'channel_1')
	channel_1.text = '1'
	channel_2 = ET.SubElement(rising_is_leading, 'channel_2')
	channel_2.text = '1'
	channel_3 = ET.SubElement(rising_is_leading, 'channel_3')
	channel_3.text = '1'
	channel_4 = ET.SubElement(rising_is_leading, 'channel_4')
	channel_4.text = '1'
	channel_5 = ET.SubElement(rising_is_leading, 'channel_5')
	channel_5.text = '1'
	channel_6 = ET.SubElement(rising_is_leading, 'channel_6')
	channel_6.text = '1'
	channel_7 = ET.SubElement(rising_is_leading, 'channel_7')
	channel_7.text = '1'
	channel_8 = ET.SubElement(rising_is_leading, 'channel_8')
	channel_8.text = '1'
	channel_9 = ET.SubElement(rising_is_leading, 'channel_9')
	channel_9.text = '1'
	channel_10 = ET.SubElement(rising_is_leading, 'channel_10')
	channel_10.text = '1'
	channel_11 = ET.SubElement(rising_is_leading, 'channel_11')
	channel_11.text = '1'
	channel_12 = ET.SubElement(rising_is_leading, 'channel_12')
	channel_12.text = '1'
	channel_13 = ET.SubElement(rising_is_leading, 'channel_13')
	channel_13.text = '1'
	channel_14 = ET.SubElement(rising_is_leading, 'channel_14')
	channel_14.text = '1'
	channel_15 = ET.SubElement(rising_is_leading, 'channel_15')
	channel_15.text = '1'
	channel_16 = ET.SubElement(rising_is_leading, 'channel_16')
	channel_16.text = '1'
	channel_17 = ET.SubElement(rising_is_leading, 'channel_17')
	channel_17.text = '1'
	channel_18 = ET.SubElement(rising_is_leading, 'channel_18')
	channel_18.text = '1'
	channel_19 = ET.SubElement(rising_is_leading, 'channel_19')
	channel_19.text = '1'
	channel_20 = ET.SubElement(rising_is_leading, 'channel_20')
	channel_20.text = '1'
	channel_21 = ET.SubElement(rising_is_leading, 'channel_21')
	channel_21.text = '1'
	channel_22 = ET.SubElement(rising_is_leading, 'channel_22')
	channel_22.text = '1'
	channel_23 = ET.SubElement(rising_is_leading, 'channel_23')
	channel_23.text = '1'



	#internal_counter variables 
	internal_counter = ET.SubElement(configuration, 'internal_counter')
	combine_time_out_config = ET.SubElement(internal_counter, 'combine_time_out_config')
	combine_time_out_config.text = '0000101000'
	fake_hit_time_interval = ET.SubElement(internal_counter, 'fake_hit_time_interval')
	fake_hit_time_interval.text = '000100000000'
	syn_packet_number = ET.SubElement(internal_counter, 'syn_packet_number')
	syn_packet_number.text = '111111111111'
	roll_over = ET.SubElement(internal_counter, 'roll_over')
	roll_over.text = '111111111111'
	coarse_count_offset = ET.SubElement(internal_counter, 'coarse_count_offset')
	coarse_count_offset.text = '000000000000'
	bunch_offset = ET.SubElement(internal_counter, 'bunch_offset')
	bunch_offset.text = '111110011100'
	event_offset = ET.SubElement(internal_counter, 'event_offset')
	event_offset.text = '000000000000'
	match_window = ET.SubElement(internal_counter, 'match_window')
	match_window.text = '000000011111'

	#fine_time_lut variables 
	fine_time_lut = ET.SubElement(configuration, 'fine_time_lut')
	fine_sel = ET.SubElement(fine_time_lut, 'fine_sel')
	fine_sel.text = '0011'
	lut0 = ET.SubElement(fine_time_lut, 'lut0')
	lut0.text = '00'
	lut1 = ET.SubElement(fine_time_lut, 'lut1')
	lut1.text = '01'
	lut2 = ET.SubElement(fine_time_lut, 'lut2')
	lut2.text = '10'
	lut3 = ET.SubElement(fine_time_lut, 'lut3')
	lut3.text = '01'
	lut4 = ET.SubElement(fine_time_lut, 'lut4')
	lut4.text = '11'
	lut5 = ET.SubElement(fine_time_lut, 'lut5')
	lut5.text = '00'
	lut6 = ET.SubElement(fine_time_lut, 'lut6')
	lut6.text = '10'
	lut7 = ET.SubElement(fine_time_lut, 'lut7')
	lut7.text = '10'
	lut8 = ET.SubElement(fine_time_lut, 'lut8')
	lut8.text = '00'
	lut9 = ET.SubElement(fine_time_lut, 'lut9')
	lut9.text = '00'
	luta = ET.SubElement(fine_time_lut, 'luta')
	luta.text = '00'
	lutb = ET.SubElement(fine_time_lut, 'lutb')
	lutb.text = '01'
	lutc = ET.SubElement(fine_time_lut, 'lutc')
	lutc.text = '11'
	lutd = ET.SubElement(fine_time_lut, 'lutd')
	lutd.text = '00'
	lute = ET.SubElement(fine_time_lut, 'lute')
	lute.text = '11'
	lutf = ET.SubElement(fine_time_lut, 'lutf')
	lutf.text = '00'

	#reset_option variables 
	reset_option = ET.SubElement(configuration, 'reset_option')
	rst_ePLL = ET.SubElement(reset_option, 'rst_ePLL')
	rst_ePLL.text = '0'
	reset_jtag_in = ET.SubElement(reset_option, 'reset_jtag_in')
	reset_jtag_in.text = '0'
	event_reset_jtag_in = ET.SubElement(reset_option, 'event_reset_jtag_in')
	event_reset_jtag_in.text = '0'
	chnl_fifo_overflow_clear = ET.SubElement(reset_option, 'chnl_fifo_overflow_clear')
	chnl_fifo_overflow_clear.text = '0'
	debug_port_select = ET.SubElement(reset_option, 'debug_port_select')
	debug_port_select.text = '0000'

	#ePll_option variables 
	ePll_option = ET.SubElement(configuration, 'ePll_option')
	phase_clk160 = ET.SubElement(ePll_option, 'phase_clk160')
	phase_clk160.text = '01000'
	phase_clk320_0 = ET.SubElement(ePll_option, 'phase_clk320_0')
	phase_clk320_0.text = '0100'
	phase_clk320_1 = ET.SubElement(ePll_option, 'phase_clk320_1')
	phase_clk320_1.text = '0000'
	phase_clk320_2 = ET.SubElement(ePll_option, 'phase_clk320_2')
	phase_clk320_2.text = '0010'
	ePllRes = ET.SubElement(ePll_option, 'ePllRes')
	ePllRes.text = '0010'
	ePllIcp = ET.SubElement(ePll_option, 'ePllIcp')
	ePllIcp.text = '0100'
	ePllCap = ET.SubElement(ePll_option, 'ePllCap')
	ePllCap.text = '10'

	#TDC_status variables 
	TDC_status = ET.SubElement(configuration, 'TDC_status')

	#data_rate variables (1:run at that rate)
	data_rate = ET.SubElement(configuration, 'data_rate')
	run_320_rate = ET.SubElement(data_rate, 'run_320_rate')
	run_320_rate.text = '0'
	run_160_rate = ET.SubElement(data_rate, 'run_160_rate')
	run_160_rate.text = '1'
	run_80_rate = ET.SubElement(data_rate, 'run_80_rate')
	run_80_rate.text = '0'

	#trigger_mode variables (0: triggerless mode , 1: triggered mode)
	trigger_mode = ET.SubElement(configuration, 'trigger_mode')
	enable_trigger = ET.SubElement(trigger_mode, 'enable_trigger')
	enable_trigger.text = '1'

	#format variables   (choose one mode to run in, 1:run in that mode)
	formatting = ET.SubElement(configuration, 'formatting')
	pair_mode = ET.SubElement(formatting, 'pair_mode')
	pair_mode.text = '0'
	edge_mode = ET.SubElement(formatting, 'edge_mode')
	edge_mode.text = '1'
	double_edge_mode = ET.SubElement(formatting, 'double_edge_mode')
	double_edge_mode.text = '0'
	pair_full_width_mode = ET.SubElement(formatting, 'pair_full_width_mode')
	pair_full_width_mode.text = '0'
	debug_mode = ET.SubElement(formatting, 'debug_mode')
	debug_mode.text = '0'
	TDC_ID_mode = ET.SubElement(formatting, 'TDC_ID_mode')
	TDC_ID_mode.text = '0'

	#edge_type variables (0:rising_is_leading, 1:falling_is_leading)
	edge_type = ET.SubElement(configuration, 'edge_type')
	leading_type = ET.SubElement(edge_type, 'leading_type')
	leading_type.text = '1'

	#phase_clk160
	phase_clk160 = ET.SubElement(configuration, 'phase_clk160')
	phase_clk160_value = ET.SubElement(phase_clk160, 'phase_clk160_value')
	phase_clk160_value.text = '7'

	#phase_clk320_1
	phase_clk320_1 = ET.SubElement(configuration, 'phase_clk320_1')
	phase_clk320_1_value = ET.SubElement(phase_clk320_1, 'phase_clk320_1_value')
	phase_clk320_1_value.text = '5'


	#create a new XML file with correct indentations
	xmlstr = minidom.parseString(ET.tostring(configuration)).toprettyxml(indent="	")
	with open(fileName, "w") as f:
		f.write(xmlstr)

if __name__ == "__main__":
	generateXML("TDC_default_channels.xml")
