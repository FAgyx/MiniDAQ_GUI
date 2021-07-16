class ASD_chip(object):
    def __init__(self):
        self.reset_ASD_chip_setup()        
    
    def reset_ASD_chip_setup(self):
        self.channel_0_mode = ['00']
        self.channel_1_mode = ['00']
        self.channel_2_mode = ['00']
        self.channel_3_mode = ['00']
        self.channel_4_mode = ['00']
        self.channel_5_mode = ['00']
        self.channel_6_mode = ['00']
        self.channel_7_mode = ['00']
        self.chip_mode =['0']
        self.deadtime =['111']
        self.int_gate =['0100']
        self.rundown_curr =['010']
        self.hyst =['1110']
        self.wilk_thr =['010']
        self.main_thr =['01100110']
        self.unused =['0000000000000']
        self.setup =   [self.channel_0_mode,self.channel_1_mode,self.channel_2_mode,self.channel_3_mode,
                        self.channel_4_mode,self.channel_5_mode,self.channel_6_mode,self.channel_7_mode,
                        self.chip_mode,self.deadtime,self.int_gate,self.rundown_curr,self.hyst,
                        self.wilk_thr,self.main_thr,self.unused]


class ASD_mezz(object):
    def __init__(self):
        self.ASD0 = ASD_chip()   
        self.ASD1 = ASD_chip()
        self.ASD2 = ASD_chip()
        self.ASD_mezz_setup = [self.ASD0.setup, self.ASD1.setup, self.ASD2.setup]

    
         


    # def update_ASD(self):
    #     self.asd_bin_str = ''.join(self.asd_align)
    #     for s in self.ASD_setup:
    #         self.asd_bin_str = self.asd_bin_str + ''.join(s)
    #     self.setup_0_str=bin_to_hex(self.asd_bin_str)
    #     update_reg(0,self.setup_0_str[0:16],self.ser)
    #     update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+self.setup_0_str[16:21],self.ser)
    #     update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
    #     update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
    #     update_config_period(10,self.ser)
    #     update_JTAG_inst('\x09',self.ser)
    #     update_bit_length(165,self.ser)
    #     start_action(self.ser)


    # def list_to_string(self,var):
    #     string_temp = ''
    #     for s in self.__dict__[var]:
    #         string_temp=string_temp+''.join(s)
    #     return string_temp