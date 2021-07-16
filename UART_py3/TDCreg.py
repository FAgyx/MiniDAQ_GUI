from TDC_config_low_level_function import *
from ASDreg import *

# test 1
class TDCreg(object):
    def __init__(self,ser):
        self.ser = ser
        self.wordbyte = 3
        self.reset_all_reg()
        self.setup_0_align = ['00000']
        self.setup_1_align = ['00']
        self.setup_2_align = ['0000']
        self.control_0_align = ['']
        self.control_1_align = ['0']
        self.hit_width = 10
        self.hit_interval = 10
        self.hit_inverse = '0'
        self.hit_enable = '\xFF\xFF\xFF'
        self.hit_delay = 0
        self.asd_mezz = ASD_mezz()
        trst_0(self.ser)
        trst_1(self.ser)

    def reset_setup_0(self):
        #setup_0
        #TTC_setup
        self.enable_new_ttc = ['0']
        self.enable_master_reset_code =['0']
        self.enable_direct_bunch_reset = ['0']
        self.enable_direct_event_reset = ['0']
        self.enable_direct_trigger = ['0']
        #bcr_distribute
        self.auto_roll_over = ['1']
        self.bypass_bcr_distribution =['0']
        #tdc_mode
        self.enable_trigger = ['0']
        self.channel_data_debug = ['0']
        self.enable_leading = ['0']
        self.enable_pair = ['1']
        self.enable_fake_hit = ['0']
        self.rising_is_leading = ['111111111111111111111111']
        self.channel_enable_r = ['111111111111111111111111']
        self.channel_enable_f = ['111111111111111111111111']
        #readout
        self.TDC_ID = ['1111010101010101010']
        self.enable_trigger_timeout = ['0']
        self.enable_high_speed = ['1']
        self.enable_legacy = ['0']
        self.full_width_res = ['0']
        self.width_select = ['000']
        self.enable_8b10b = ['1']
        self.enable_insert =['0']
        self.enable_error_packet = ['0']
        self.enable_TDC_ID = ['0']
        self.enable_error_notify = ['0']
        #setup_0
        self.TTC_setup = [self.enable_new_ttc , self.enable_master_reset_code , self.enable_direct_bunch_reset , self.enable_direct_event_reset , self.enable_direct_trigger]
        self.bcr_distribute = [self.auto_roll_over , self.bypass_bcr_distribution]
        self.tdc_mode = [self.enable_trigger , self.channel_data_debug , self.enable_leading , self.enable_pair , self.enable_fake_hit ,self.rising_is_leading , self.channel_enable_r , self.channel_enable_f]
        self.TDC_ID_l = [self.TDC_ID]
        self.readout = [self.enable_trigger_timeout , self.enable_high_speed , self.enable_legacy , self.full_width_res , self.width_select , self.enable_8b10b , self.enable_insert , self.enable_error_packet , self.enable_TDC_ID , self.enable_error_notify]
        self.setup_0 = self.TTC_setup + self.bcr_distribute + self.tdc_mode + self.TDC_ID_l + self.readout
        self.setup_0_indictor = ['0']

    def reset_setup_1(self):
        ##setup_1
        #timer_out
        self.combine_time_out_config = ['0000101000']
        self.fake_hit_time_interval =['000100000000']
        self.syn_packet_number = ['111111111111']        
        #coarse_out
        self.roll_over = ['111111111111']
        self.coarse_count_offset = ['000000000000']
        self.bunch_offset = ['111110011100']
        self.event_offset = ['000000000000']
        self.match_window = ['000000011111']
        #setup_1
        self.timer_out = [self.combine_time_out_config , self.fake_hit_time_interval , self.syn_packet_number]
        self.coarse_out = [self.roll_over , self.coarse_count_offset , self.bunch_offset , self.event_offset , self.match_window]
        self.setup_1 = self.timer_out +self.coarse_out 
        self.setup_1_indictor = ['0']

    def reset_setup_2(self):
        ##setup_2
        #timer_out
        self.fine_sel = ['0011']
        self.lut0 = ['00']
        self.lut1 = ['01']
        self.lut2 = ['10']
        self.lut3 = ['01']
        self.lut4 = ['11']
        self.lut5 = ['00']
        self.lut6 = ['10']
        self.lut7 = ['10']
        self.lut8 = ['00']
        self.lut9 = ['00']
        self.luta = ['00']
        self.lutb = ['01']
        self.lutc = ['11']
        self.lutd = ['00']
        self.lute = ['11']
        self.lutf = ['00']
        self.chnl_decode = [self.fine_sel , self.lut0 ,self.lut1 ,self.lut2, self.lut3 ,self.lut4 ,self.lut5 ,self.lut6 ,self.lut7 ,self.lut8 ,self.lut9 ,self.luta ,self.lutb ,self.lutc ,self.lutd ,self.lute ,self.lutf]
        self.setup_2 = self.chnl_decode
        self.setup_2_indictor = ['0']

    def reset_setup(self):
        self.reset_setup_0()
        self.reset_setup_1()
        self.reset_setup_2()
        self.setup = [self.setup_0, self.setup_1, self.setup_2]

    def reset_control_0(self):
        ##control_0
        #reset_control
        self.rst_ePLL = ['0']
        self.reset_jtag_in = ['0']
        self.event_reset_jtag_in = ['0']
        self.chnl_fifo_overflow_clear = ['0']
        self.debug_port_select =['0000']
        #control_0
        self.reset_control = [self.rst_ePLL , self.reset_jtag_in , self.event_reset_jtag_in , self.chnl_fifo_overflow_clear , self.debug_port_select]
        self.control_0 = self.reset_control
        self.control_0_indictor = ['0']

    def reset_control_1(self):
        ##control_1
        self.phase_clk160 = ['01000']
        self.phase_clk320_0 = ['0100']
        self.phase_clk320_1 = ['0000']
        self.phase_clk320_2 = ['0010']
        self.ePllRes = ['0010']
        self.ePllIcp = ['0100']
        self.ePllCap = ['10']
        self.ePLL_control = [self.phase_clk160 , self.phase_clk320_0 , self.phase_clk320_1 , self.phase_clk320_2 , self.ePllRes , self.ePllIcp , self.ePllCap, self.ePllRes , self.ePllIcp , self.ePllCap,self.ePllRes , self.ePllIcp , self.ePllCap]
        self.control_1 = self.ePLL_control
        self.control_1_indictor = ['0']

    def reset_conttrol(self):
        self.reset_control_0()
        self.reset_control_1()
        self.control = [self.control_0 , self.control_1]

    def init_status_0(self):
        self.instruction_error = ['']
        self.CRC = ['']
        self.status_0 = [self.instruction_error,self.CRC]

    def init_status_1(self):
        self.ePll_lock = ['']
        self.chnl_fifo_overflow = ['']
        self.status_1 = [self.ePll_lock,self.chnl_fifo_overflow]

    def reset_status(self):
        self.init_status_0()
        self.init_status_1()
        self.status = [self.status_0 , self.status_1]

    def reset_all_reg(self):
        trst_0(self.ser)
        trst_1(self.ser)
        self.reset_setup()
        self.reset_conttrol()
        self.reset_status()
        print("JTAG and All regs reset!")

    def update_setup_0(self):
        self.setup_0_bin_str = ''.join(self.setup_0_align)
        for s in self.setup_0:
            self.setup_0_bin_str = self.setup_0_bin_str + ''.join(s)
        self.setup_0_str=bin_to_hex(self.setup_0_bin_str)
        update_reg(0,'\x00'+self.setup_0_str,self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x12',self.ser)
        update_bit_length(115,self.ser)
        start_action(self.ser)
        print("setup0 updated to TDC: 0x"+format(int(self.setup_0_bin_str,2),'029X'))
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:19]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:115]
            self.setup_0_indictor[0] = '1' if readback == self.setup_0[0] else '0'
        else:
            print("Warning: setup0 readback blank! Please check UART connection.")

    def update_setup_1(self):
        self.setup_1_bin_str = ''.join(self.setup_1_align)
        for s in self.setup_1:
            self.setup_1_bin_str = self.setup_1_bin_str + ''.join(s)
        self.setup_1_str=bin_to_hex(self.setup_1_bin_str)
        update_reg(0,'\x00\x00\x00\x00'+self.setup_1_str,self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x03',self.ser)
        update_bit_length(94,self.ser)
        start_action(self.ser)
        print("setup1 updated to TDC: 0x"+format(int(self.setup_1_bin_str,2),'024X'))
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:16]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:94]
            self.setup_1_indictor[0] = '1' if readback == self.setup_1[0] else '0'
        else:
            print("Warning: setup1 readback blank! Please check UART connection.")

    def update_setup_2(self):
        self.setup_2_bin_str = ''.join(self.setup_2_align)
        for s in self.setup_2:
            self.setup_2_bin_str = self.setup_2_bin_str + ''.join(s)
        self.setup_2_str=bin_to_hex(self.setup_2_bin_str)
        update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+self.setup_2_str,self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x14',self.ser)
        update_bit_length(36,self.ser)
        start_action(self.ser)
        print("setup2 updated to TDC: 0x"+format(int(self.setup_2_bin_str,2),'09X'))
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:9]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:36]
            self.setup_2_indictor[0] = '1' if readback == self.setup_2[0] else '0'
        else:
            print("Warning: setup2 readback blank! Please check UART connection.")

    def update_control_0(self):
        self.control_0_bin_str = ''.join(self.control_0_align)
        for s in self.control_0:
            self.control_0_bin_str = self.control_0_bin_str + ''.join(s)
        self.control_0_str=bin_to_hex(self.control_0_bin_str)
        update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+self.control_0_str,self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x05',self.ser)
        update_bit_length(8,self.ser)
        start_action(self.ser)
        print("control_0 updated to TDC: 0x"+format(int(self.control_0_bin_str,2),'02X'))
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:5]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:8]
            self.control_0_indictor[0] = '1' if readback == self.control_0[0] else '0'
        else:
            print("Warning: control0 readback blank! Please check UART connection.")

    def update_control_1(self):
        self.control_1_bin_str = ''.join(self.control_1_align)
        for s in self.control_1:
            self.control_1_bin_str = self.control_1_bin_str + ''.join(s)
        self.control_1_str=bin_to_hex(self.control_1_bin_str)
        update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'+self.control_1_str,self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x06',self.ser)
        update_bit_length(47,self.ser)
        start_action(self.ser)
        print("control_1 updated to TDC: 0x"+format(int(self.control_1_bin_str,2),'012X'))
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:10]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:47]
            self.control_1_indictor[0] = '1' if readback == self.control_1[0] else '0'
        else:
            print("Warning: control1 readback blank! Please check UART connection.")

    def read_status_0(self):
        update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x17',self.ser)
        update_bit_length(33,self.ser)
        start_action(self.ser)
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:9]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:33]
            self.instruction_error[0] = readback[0]
            self.CRC[0] = readback[1:33]
            print("status_0 read back: 0x"+format(int(readback,2),'09X'))
        else:
            print("Warning: status0 readback blank! Please check UART connection.")

    def read_status_1(self):
        update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',self.ser)
        update_config_period(0,self.ser)
        update_JTAG_inst('\x18',self.ser)
        update_bit_length(25,self.ser)
        start_action(self.ser)
        readback = ''
        for byte in get_update_reg(3,self.ser)[4:8]:
            readback+=format(ord(byte),'b').zfill(8)
        if len(readback)>0:
            readback = readback[0:25]
            self.ePll_lock[0] = readback[0]
            self.chnl_fifo_overflow[0] = readback[1:25]
            print("status_1 read back: 0x"+format(int(readback,2),'07X'))
        else:
            print("Warning: status1 readback blank! Please check UART connection.")

    def list_to_string(self,var):
        string_temp = ''
        for s in self.__dict__[var]:
            string_temp=string_temp+''.join(s)
        return string_temp

    def set_ePLL_phase(self,clk_160_phase,clk_320_phase):
        self.phase_clk160[0]=format(clk_160_phase%32,'b').zfill(5)
        # TDC0.phase_clk160[0]=format(((clk_320_phase+4)*2-4)%32,'b').zfill(5)
        self.phase_clk320_0[0]=format((clk_320_phase+4)%16,'b').zfill(4)
        self.phase_clk320_1[0]=format(clk_320_phase%16,'b').zfill(4)
        self.update_control_1()

    def reselect_dline(self,correct_counter=1000):
        tmp_r = self.channel_enable_r[0]
        tmp_f = self.channel_enable_f[0]
        print('Phase clk160   = '+str(int(self.phase_clk160[0],2)))
        print('Phase clk320_0 = '+str(int(self.phase_clk320_0[0],2)))
        print('Phase clk320_1 = '+str(int(self.phase_clk320_1[0],2)))

        self.channel_enable_r[0] ='000000000000000000000000' # disable input to ensure 8b10b comma out
        self.channel_enable_f[0] ='000000000000000000000000'
        self.update_setup_0()
        tdc_master_reset_1(self.ser)
        tdc_master_reset_0(self.ser)
        update_input_deserial_para(self.ser,correct_counter_th=correct_counter) # correct_counter_th 10b, max 1022
        reselect_input_deserial(self.ser)
        time.sleep(1) # hold to ensure dline locked
        self.channel_enable_r[0] = tmp_r
        self.channel_enable_f[0] = tmp_f 
        self.update_setup_0()
        print("Reselect deline done!")

    def run_320M_data_rate(self):
        self.enable_high_speed[0] = '1'
        self.enable_legacy[0] = '0'

    def run_160M_data_rate(self):
        self.enable_high_speed[0] = '0'
        self.enable_legacy[0] = '0'

    def run_80M_data_rate(self):
        self.enable_legacy[0] = '1'

    def run_single_edge_mode(self):  # 24'b dataword = 5'b chnlID + 1'b0 + 1'b is_rising_edge + 17'b leading_edge
        self.channel_data_debug[0] = '0'
        self.enable_leading[0] = '1'
        self.enable_pair[0] = '0'

    def run_double_edge_mode(self):  # 40'b dataword = 5'b chnlID + 2'b10 + 17'b leading_edge + 16'b trailing_edge_LSB
        self.channel_data_debug[0] = '0'
        self.enable_leading[0] = '0'
        self.enable_pair[0] = '0'

    def run_pair_mode(self):  # 32'b dataword = 5'b chnlID + 2'b11 + 17'b leading_edge + 8'b width
        self.channel_data_debug[0] = '0'
        self.enable_leading[0] = '0'
        self.enable_pair[0] = '1'
        self.full_width_res[0] = '0'

    def run_pair_full_width_mode(self):  # 40'b dataword = 5'b chnlID + 2'b11 + 17'b leading_edge + 16'b width
        self.channel_data_debug[0] = '0'
        self.enable_leading[0] = '0'
        self.enable_pair[0] = '1'
        self.full_width_res[0] = '1'

    def run_debug_mode(self):  # 24'b dataword0 = 2'b00 + 5'b chnl_ID + 17'b time
                               # 24'b dataword1 = 2'b11 + 1'b edge_mode + 2'b hit_counter + 15'b drop_coarse + 4'b fineQ
        self.channel_data_debug[0] = '1'


    def run_idle_insert_mode(self, syn_packet_number):
        self.enable_insert[0] = '1'
        self.update_setup_0()
        self.syn_packet_number[0] = "{:0>12b}".format(syn_packet_number%4096)
        self.update_setup_1()

    def run_error_insert_mode(self):
        self.enable_error_packet[0] = '1'
        self.update_setup_0()

    def run_TDCID_mode(self):
        self.enable_TDC_ID[0] = '1'

    def config_TDCID(self, TDCID):
        self.TDC_ID[0] = "{:0>19b}".format(TDCID)
        self.update_setup_0()

    def disable_8b10b(self):
        self.enable_8b10b[0] = '0'
        self.update_setup_0()


    def config_pairing_timeout(self,time_out=40):
        self.combine_time_out_config[0] = "{:0>10b}".format(time_out%1024)
        self.update_setup_1()


    def run_triggerless_mode(self):
        self.enable_trigger[0] = '0'
        self.update_setup_0()
        tdc_triggerless_mode(self.ser)

    def run_trigger_mode(self):
        self.enable_trigger[0] = '1'
        self.enable_fake_hit[0] = '1'
        self.enable_direct_trigger[0] = '0'
        self.enable_direct_bunch_reset[0] = '0'
        self.enable_direct_event_reset[0] = '0'

    def set_rising_is_leading(self):
        self.rising_is_leading[0] = '111111111111111111111111'

    def set_falling_is_leading(self):
        self.rising_is_leading[0] = '000000000000000000000000'

    def enable_legacy_ttc(self):
        self.enable_new_ttc[0] = '0'
        self.update_setup_0()
        ttc_mode_select(self.ser, 0)
        update_ttc_delay(self.ser, 1)

    def single_trigger(self):
        enable_ttc_trigger(self.ser)
        single_TTC(self.ser)

    def event_reset(self):
        enable_ttc_event_reset(self.ser)
        single_TTC(self.ser)

    def single_BCR(self):
        enable_ttc_BCR(self.ser)
        single_TTC(self.ser)

    def master_reset(self):
        enable_ttc_master_reset(self.ser)
        single_TTC(self.ser)

    def reset_JTAG(self):
        trst_0(self.ser)
        trst_1(self.ser)

    def update_JTAG(self):
        self.update_setup_0()
        self.update_setup_1()
        self.update_setup_2()
        self.update_control_0()
        self.update_control_1()
        self.read_status_0()
        self.read_status_1()

    def set_FPGA_sample_rate(self):
        if self.enable_legacy[0] == '1':
            print("Set sample rate to 80Mbps!")
        elif self.enable_high_speed[0] == '1':
            tdc_high_speed(self.ser)
            print("Set sample rate to 320Mbps!")
        elif self.enable_high_speed[0] == '0':
            tdc_low_speed(self.ser)
            print("Set sample rate to 160Mbps!")

    def set_word_byte(self):
        if self.enable_TDC_ID[0] == '1':
            self.wordbyte = 3             # TDC_ID mode
            print("Running in TDC_ID mode, TDC_ID=0x"+
            format(int(self.TDC_ID[0],2),'05X'))
        elif self.channel_data_debug[0] == '1':
            self.wordbyte = 3             # debug mode
            print("Running in debug mode")
        elif self.enable_leading[0] == '1':
            self.wordbyte = 3             # single edge mode 
            print("Running in single edge mode")    
        elif self.enable_leading[0] == '0':
            if self.enable_pair[0] == '0': # double edge mode
                self.wordbyte = 5
                print("Running in double edge mode")
            elif self.enable_pair[0] == '1':
                if self.full_width_res[0] == '0': # pair mode
                    self.wordbyte = 4
                    print("Running in pair mode")
                    print("Width LSB = "+str(2**int(self.width_select[0],2)*0.78125)+'ns')
                else:                         # full width pair mode
                    self.wordbyte = 5
                    print("Running in full width pair mode")
                print("Pair time out = "+str(int(self.combine_time_out_config[0],2)*6.25)+
                'ns, Code=0x' + format(int(self.combine_time_out_config[0],2),'03X') +', LSB=6.25ns')
        update_data_length(self.ser, self.wordbyte)

    def set_trigger_type(self):
        if self.enable_trigger[0] == '0':  # triggerless mode
            tdc_triggerless_mode(self.ser)
            print("Running in triggerless mode")
        elif self.enable_trigger[0] == '1':  # triggered mode
            print("Running in triggered mode")
            if self.enable_fake_hit[0] == '1':
                print("Fake hit enabled, interval = "+
                str(int(self.fake_hit_time_interval[0],2))+
                ' BC, 0x'+format(int(self.fake_hit_time_interval[0],2),'03X'))
            else:
                print("Warning: Fake hit not enabled!")
            print("Trigger Matching Information:")
            print("Bunch Offset = 0x"+format(int(self.bunch_offset[0],2),'03X'))
            print("Event Offset = 0x"+format(int(self.event_offset[0],2),'03X'))
            print("Match Window = 0x"+format(int(self.match_window[0],2),'03X'))
            if self.enable_trigger_timeout[0] == '1':
                print("Trigger time out enabled")

    def show_channel_info(self):
        print("Rising is leading: 0x"+format(int(self.rising_is_leading[0],2),'06X'))
        print([i for i in range(24) if self.rising_is_leading[0][i]=='1'])
        print("Channel enable R : 0x"+format(int(self.channel_enable_r[0],2),'06X'))
        print([i for i in range(24) if self.rising_is_leading[0][i]=='1'])
        print("Channel enable F : 0x"+format(int(self.channel_enable_f[0],2),'06X'))
        print([i for i in range(24) if self.rising_is_leading[0][i]=='1'])

    def show_packet_info(self):
        if self.enable_8b10b[0] == '1':
            print("8b10b encoding enabled")
        else:
            print("8b10b encoding not enabled")
        if self.enable_insert[0] == '1':
            print("Idle packet insert enabled with maximum interval = "+
            str(int(self.channel_enable_f[0],2))+" packets")
        else:
            print("Idle packet insert not enabled")
        if self.enable_error_packet[0] == '1':
            if self.enable_trigger[0] == '1':
                print("Warning: Error packet cannot be inserted in triggered mode!")
            else:
                print("Error packet inserted")

    def show_TTC_info(self):
        ttc_str = ''
        ttc_str += 'New' if self.enable_new_ttc[0] == '1' else 'Legacy'
        ttc_str += ' TTC enabled for '
        ttc_str += 'Master_reset ' if self.enable_master_reset_code[0] == '1' else ''
        ttc_str += 'BC_reset ' if self.auto_roll_over[0] == '0' \
        and self.enable_direct_bunch_reset[0] == '0' else ''
        ttc_str += 'Trigger ' if self.enable_direct_trigger[0] == '0' else ''
        ttc_str += 'Event_reset' if self.enable_direct_event_reset[0] == '0' else ''
        print(ttc_str)

    def show_BCR_info(self):
        bcr_str = ''
        bcr_str += 'BCR from '
        if self.auto_roll_over[0] == '1':
            bcr_str += 'internal ' 
        else:
            if self.enable_direct_bunch_reset[0] == '0':
                bcr_str += 'TTC ' 
        bcr_str += 'with roll_over = 0x'+format(int(self.roll_over[0],2),'03X')+' BC '
        bcr_str += 'and delay = 0x'+format(int(self.coarse_count_offset[0],2),'03X') \
        +' BC' if self.bypass_bcr_distribution[0] == '0' else 'and no delay'
        print(bcr_str)

    def update_periodic_hit(self):
        update_hit_width(self.ser,self.hit_width)  # width_time = width*6.25 ns, minimum 6.25ns
        update_inv_hit(self.ser,self.hit_inverse)
        update_hit_delay(self.ser,self.hit_delay)
        update_hit_interval(self.ser,self.hit_interval)   # hit rate = 160MHz/interval
        update_hit_mask_hit(self.ser,self.hit_enable)
        print("Periodic hit set!")
        print("Width="+str(self.hit_width*6.25)+"ns, interval=" +
        str(self.hit_interval)+", rate="+str(160.0/self.hit_interval)+
        "MHz, delay="+str(self.hit_delay)+", inverse="+self.hit_inverse)
        print("Hit enabled for channel:")
        print([23-i for i in range(24) if (format(ord(self.hit_enable[0]),'08b')+
        format(ord(self.hit_enable[1]),'08b')+format(ord(self.hit_enable[2]),'08b'))[i]=='1'])

    def DAQ_init(self):
        print("//////DAQ initialization starts!//////")
        self.reset_JTAG()
        self.update_JTAG()
        self.set_FPGA_sample_rate()
        self.reselect_dline()
        self.set_word_byte()
        self.set_trigger_type()
        self.show_channel_info()
        self.show_packet_info()
        self.show_TTC_info()
        self.show_BCR_info()
        print("//////DAQ initialization done!//////")
        
        




        




        


    

