from TDC_config_low_level_function import *


class ASDreg(object):
    def __init__(self,ser):
        self.ser = ser
        self.asd_align = ['000']
        trst_0(self.ser)
        trst_1(self.ser)
        
    
    def reset_ASD(self):
        trst_0(self.ser)
        trst_1(self.ser)
        self.ASD0_CHANNEL_0_MODE = ['00']
        self.ASD0_CHANNEL_1_MODE = ['00']
        self.ASD0_CHANNEL_2_MODE = ['00']
        self.ASD0_CHANNEL_3_MODE = ['00']
        self.ASD0_CHANNEL_4_MODE = ['00']
        self.ASD0_CHANNEL_5_MODE = ['00']
        self.ASD0_CHANNEL_6_MODE = ['00']
        self.ASD0_CHANNEL_7_MODE = ['00']
        self.ASD0_CHIP_MODE =['0']
        self.ASD0_DEADTIME =['111']
        self.ASD0_INT_GATE =['0101']
        self.ASD0_RUND_CURR =['100']
        self.ASD0_HYST_DAC =['1110']
        self.ASD0_WILK_THR_DAC =['010']
        self.ASD0_MAIN_THR_DAC =['01101010']
        self.ASD0_CAP_SELECT =['000']
        self.ASD0_CH_MASK_TST_CTRL =['00000000']
        self.ASD0_VMON =['00']
        self.ASD0_setup =   [self.ASD0_CHANNEL_0_MODE,self.ASD0_CHANNEL_1_MODE,self.ASD0_CHANNEL_2_MODE,self.ASD0_CHANNEL_3_MODE,
                            self.ASD0_CHANNEL_4_MODE,self.ASD0_CHANNEL_5_MODE,self.ASD0_CHANNEL_6_MODE,self.ASD0_CHANNEL_7_MODE,
                            self.ASD0_CHIP_MODE,self.ASD0_DEADTIME,self.ASD0_INT_GATE,self.ASD0_RUND_CURR,self.ASD0_HYST_DAC,
                            self.ASD0_WILK_THR_DAC,self.ASD0_MAIN_THR_DAC,self.ASD0_CAP_SELECT,self.ASD0_CH_MASK_TST_CTRL,self.ASD0_VMON]
        self.ASD1_CHANNEL_0_MODE =['00']
        self.ASD1_CHANNEL_1_MODE =['00']
        self.ASD1_CHANNEL_2_MODE =['00']
        self.ASD1_CHANNEL_3_MODE =['00']
        self.ASD1_CHANNEL_4_MODE =['00']
        self.ASD1_CHANNEL_5_MODE =['00']
        self.ASD1_CHANNEL_6_MODE =['00']
        self.ASD1_CHANNEL_7_MODE =['00']
        self.ASD1_CHIP_MODE =['0']
        self.ASD1_DEADTIME =['111']
        self.ASD1_INT_GATE =['0101']
        self.ASD1_RUND_CURR =['100']
        self.ASD1_HYST_DAC =['1110']
        self.ASD1_WILK_THR_DAC =['010']
        self.ASD1_MAIN_THR_DAC =['01101010']
        self.ASD1_CAP_SELECT =['000']
        self.ASD1_CH_MASK_TST_CTRL =['00000000']
        self.ASD1_VMON =['00']
        self.ASD1_setup =   [self.ASD1_CHANNEL_0_MODE,self.ASD1_CHANNEL_1_MODE,self.ASD1_CHANNEL_2_MODE,self.ASD1_CHANNEL_3_MODE,
                            self.ASD1_CHANNEL_4_MODE,self.ASD1_CHANNEL_5_MODE,self.ASD1_CHANNEL_6_MODE,self.ASD1_CHANNEL_7_MODE,
                            self.ASD1_CHIP_MODE,self.ASD1_DEADTIME,self.ASD1_INT_GATE,self.ASD1_RUND_CURR,self.ASD1_HYST_DAC,
                            self.ASD1_WILK_THR_DAC,self.ASD1_MAIN_THR_DAC,self.ASD1_CAP_SELECT,self.ASD1_CH_MASK_TST_CTRL,self.ASD1_VMON]
        self.ASD2_CHANNEL_0_MODE =['00']
        self.ASD2_CHANNEL_1_MODE =['00']
        self.ASD2_CHANNEL_2_MODE =['00']
        self.ASD2_CHANNEL_3_MODE =['00']
        self.ASD2_CHANNEL_4_MODE =['00']
        self.ASD2_CHANNEL_5_MODE =['00']
        self.ASD2_CHANNEL_6_MODE =['00']
        self.ASD2_CHANNEL_7_MODE =['00']
        self.ASD2_CHIP_MODE =['0']
        self.ASD2_DEADTIME =['111']
        self.ASD2_INT_GATE =['0101']
        self.ASD2_RUND_CURR =['100']
        self.ASD2_HYST_DAC =['1110']
        self.ASD2_WILK_THR_DAC =['010']
        self.ASD2_MAIN_THR_DAC =['01101010']
        self.ASD2_CAP_SELECT =['000']
        self.ASD2_CH_MASK_TST_CTRL =['00000000']
        self.ASD2_VMON =['00']
        self.ASD2_setup =   [self.ASD2_CHANNEL_0_MODE,self.ASD2_CHANNEL_1_MODE,self.ASD2_CHANNEL_2_MODE,self.ASD2_CHANNEL_3_MODE,
                            self.ASD2_CHANNEL_4_MODE,self.ASD2_CHANNEL_5_MODE,self.ASD2_CHANNEL_6_MODE,self.ASD2_CHANNEL_7_MODE,
                            self.ASD2_CHIP_MODE,self.ASD2_DEADTIME,self.ASD2_INT_GATE,self.ASD2_RUND_CURR,self.ASD2_HYST_DAC,
                            self.ASD2_WILK_THR_DAC,self.ASD2_MAIN_THR_DAC,self.ASD2_CAP_SELECT,self.ASD2_CH_MASK_TST_CTRL,self.ASD2_VMON]
        self.ASD_setup = self.ASD0_setup + self.ASD1_setup + self.ASD2_setup


    def update_ASD(self):
        self.asd_bin_str = ''.join(self.asd_align)
        for s in self.ASD_setup:
            self.asd_bin_str = self.asd_bin_str + ''.join(s)
        self.setup_0_str=bin_to_hex(self.asd_bin_str)
        update_reg(0,self.setup_0_str[0:16],self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+self.setup_0_str[16:21],self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(10,self.ser)
        update_JTAG_inst('\x09',self.ser)
        update_bit_length(165,self.ser)
        start_action(self.ser)


    def list_to_string(self,var):
        string_temp = ''
        for s in self.__dict__[var]:
            string_temp=string_temp+''.join(s)
        return string_temp