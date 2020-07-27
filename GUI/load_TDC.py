import sys

import xml.etree.ElementTree as ET
#tree = ET.parse('TDC_config_default.xml')
tree = ET.parse('TDC_default.xml')
root = tree.getroot()

# import UART functions
sys.path.insert(0, "../UART_py3")

from serial_config_tdc import *
from TDCreg import *
from TDC_config_low_level_function import *


class loading:

    def __init__(self,ser):
        self.ser = ser
        
    def loading_tdc(self):
        print("TDC_config_default loaded")
        #mode set
        #self.TDC_inst.enable_new_ttc[0] = root[0][0].text
        # self.TDC_inst.enable_master_reset_code[0] = root[0][1].text
        # self.TDC_inst.enable_direct_bunch_reset[0] = root[0][2].text
        # self.TDC_inst.enable_direct_trigger[0] = root[0][3].text
        # self.TDC_inst.auto_roll_over[0] = root[0][4].text
        # self.TDC_inst.bypass_bcr_distribution[0] = root[0][5].text
        # self.TDC_inst.enable_trigger[0] = root[0][6].text
        # self.TDC_inst.channel_data_debug[0] = root[0][7].text
        # self.TDC_inst.enable_leading[0] = root[0][8].text
        # self.TDC_inst.enable_pair[0] = root[0][9].text
        # self.TDC_inst.enable_fake_hit[0] = root[0][10].text
        # self.TDC_inst.enable_trigger_timeout[0] = root[0][11].text
        # self.TDC_inst.enable_high_speed[0] = root[0][12].text
        # self.TDC_inst.enable_legacy[0] = root[0][13].text
        # self.TDC_inst.full_width_res[0] = root[0][14].text
        # self.TDC_inst.enable_8b10b[0] = root[0][15].text
        # self.TDC_inst.enable_insert[0] = root[0][16].text
        # self.TDC_inst.enable_error_packet[0] = root[0][17].text
        # self.TDC_inst.enable_TDC_ID[0] = root[0][18].text
        # self.TDC_inst.enable_error_notify[0] = root[0][19].text

        # #internal_counter
        # self.TDC_inst.combine_time_out_config[0] = root[1][0].text
        # self.TDC_inst.fake_hit_time_interval[0] = root[1][1].text
        # self.TDC_inst.syn_packet_number[0] = root[1][2].text
        # self.TDC_inst.roll_over[0] = root[1][3].text
        # self.TDC_inst.coarse_count_offset[0] = root[1][4].text
        # self.TDC_inst.bunch_offset[0] = root[1][5].text
        # self.TDC_inst.event_offset[0] = root[1][6].text
        # self.TDC_inst.match_window[0] = root[1][7].text

        # #fine_time_lut
        # self.TDC_inst.fine_sel[0] = root[2][0].text
        # self.TDC_inst.lut0[0] = root[2][1].text
        # self.TDC_inst.lut1[0] = root[2][2].text
        # self.TDC_inst.lut2[0] = root[2][3].text
        # self.TDC_inst.lut3[0] = root[2][4].text
        # self.TDC_inst.lut4[0] = root[2][5].text
        # self.TDC_inst.lut5[0] = root[2][6].text
        # self.TDC_inst.lut6[0] = root[2][7].text
        # self.TDC_inst.lut7[0] = root[2][8].text
        # self.TDC_inst.lut8[0] = root[2][9].text
        # self.TDC_inst.lut9[0] = root[2][10].text
        # self.TDC_inst.luta[0] = root[2][11].text
        # self.TDC_inst.lutb[0] = root[2][12].text
        # self.TDC_inst.lutc[0] = root[2][13].text
        # self.TDC_inst.lutd[0] = root[2][14].text
        # self.TDC_inst.lute[0] = root[2][15].text
        # self.TDC_inst.lutf[0] = root[2][16].text

        # #reset_option
        # self.TDC_inst.rst_ePLL[0] = root[3][0].text
        # self.TDC_inst.reset_jtag_in[0] = root[3][1].text
        # self.TDC_inst.event_reset_jtag_in[0] = root[3][2].text
        # self.TDC_inst.chnl_fifo_overflow_clear[0] = root[3][3].text
        # self.TDC_inst.debug_port_select[0] = root[3][4].text

        # #ePll_option
        # self.TDC_inst.phase_clk160[0] = root[4][0].text
        # self.TDC_inst.phase_clk320_0[0] = root[4][1].text
        # self.TDC_inst.phase_clk320_1[0] = root[4][2].text
        # self.TDC_inst.phase_clk320_2[0] = root[4][3].text
        # self.TDC_inst.ePllRes[0] = root[4][4].text
        # self.TDC_inst.ePllIcp[0] = root[4][5].text
        # self.TDC_inst.ePllCap[0] = root[4][6].text

        # #data_rate
        # if root[6][0].text == '1':
        #     self.comboBox.setCurrentIndex(0)
        #     self.TDC_inst.run_320M_data_rate()
        # if root[6][1].text == '1':
        #     self.comboBox.setCurrentIndex(1)
        #     self.TDC_inst.run_160M_data_rate()
        # if root[6][2].text == '1':
        #     self.comboBox.setCurrentIndex(2)
        #     self.TDC_inst.run_80M_data_rate()

        # #trigger_mode
        # if root[7][0].text == '0':
        #     self.comboBox_2.setCurrentIndex(0)
        #     self.TDC_inst.run_triggerless_mode()
        # if root[7][0].text == '1':
        #     self.comboBox_2.setCurrentIndex(1)
        #     self.TDC_inst.run_trigger_mode()

        # #format
        # if root[8][0].text == '1':
        #     self.comboBox_3.setCurrentIndex(0)
        #     self.TDC_inst.run_pair_mode()
        # if root[8][1].text == '1':
        #     self.comboBox_3.setCurrentIndex(1)
        #     self.TDC_inst.run_single_edge_mode()
        # if root[8][2].text == '1':
        #     self.comboBox_3.setCurrentIndex(2)
        #     self.TDC_inst.run_double_edge_mode()
        # if root[8][3].text == '1':
        #     self.comboBox_3.setCurrentIndex(3)
        #     self.TDC_inst.run_pair_full_width_mode()
        # if root[8][4].text == '1':
        #     self.comboBox_3.setCurrentIndex(4)
        #     self.TDC_inst.run_debug_mode()
        # if root[8][5].text == '1':
        #     self.comboBox_3.setCurrentIndex(5)
        #     self.TDC_inst.run_TDCID_mode()

        # #edge_type
        # if root[9][0].text == '0':
        #     self.comboBox_4.setCurrentIndex(0)
        #     self.TDC_inst.set_rising_is_leading()
        # if root[9][0].text == '1':
        #     self.comboBox_4.setCurrentIndex(1)
        #     self.TDC_inst.set_falling_is_leading()

        # #clk_160_phase
        # self.spinBox.setValue(int(root[10][0].text))
        # self.phase_clk160_binary = format(self.spinBox.value(), '05b')
        # self.TDC_inst.phase_clk160[0] = self.phase_clk160_binary

        # #clk_320_phase
        # self.spinBox_2.setValue(int(root[11][0].text))
        # self.phase_clk320_0_binary = format(self.spinBox_2.value() + 4, '04b')[-4:]
        # self.TDC_inst.phase_clk320_0[0] = self.phase_clk320_0_binary
        # self.phase_clk320_1_binary = format(self.spinBox_2.value(), '04b')
        # self.TDC_inst.phase_clk320_1[0] = self.phase_clk320_1_binary

