import time


def str_to_hex(s,interval):
    s_r = ''
    s = s.decode('latin_1')
    for x in range(0, len(s)):
        s_raw="{:0>2x}".format(ord(s[x]))
        s_r = s_r + interval + s_raw
    return s_r


def str_to_bin(s,interval):
    s_r = ''
    s = s.decode('latin_1')
    for x in range(0, len(s)):
        s_raw="{:0>8b}".format(ord(s[x]))
        s_r = s_r + interval + s_raw
    return s_r



def bin_to_hex_8bit(s):
    if len(s)  !=8 :
        print("Error the length of string is not 8")
        return ''
    hex_raw_str=hex(int(s,2))
    if len(hex_raw_str) == 3:
        return('0'+hex_raw_str[2])
    else:
        return(hex_raw_str[2:])

def bin_to_hex(s):
    if len(s) % 8 !=0 :
        print("Error the length of string is not 8N")
        return ''
    s_r = ''
    for x in range(0,len(s) // 8):
        s_r = s_r + chr(int(s[x*8:x*8+8],2))
    return s_r
def update_reg_str(reg_num, reg_content):
    if reg_num < 0 or reg_num > 3:
        print("Error the reg_num is not in 0-3")
        return ''
    if len(reg_content) != 16:
        print("Error the length of reg_content is not 16")
        return ''
    content_str = '\x00'+'\x1f\x2f\x30\x40\x50'
    s = chr(6 * 16 + reg_num)
    content_str = content_str + s
    content_str = content_str + '\x70\x80'
    k = 9
    for x in range(0, 16):
        byte_content = ord(reg_content[x])
        high_4bit = byte_content // 16
        low_4bit = byte_content % 16
        content_str = content_str + (chr(k*16+high_4bit))
        k = k+1
        if k == 16:
            k = 1
        content_str = content_str + (chr(k*16+low_4bit))
        k = k+1
        if k == 16:
            k = 1
    content_str = content_str + '\x0f'
    return content_str


def update_reg(reg_num, reg_content, serial_port):
    s = update_reg_str(reg_num, reg_content)
    if len(s) != 0:
        serial_port.write(s.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    return len(s)


def start_action_str():
    content_str = '\x00\x1f\x2f\x30\x40\x50\x60\x70\x81\x0f'
    return content_str


def start_action(serial_port):
    s0 = '\x00\x1f\x2f\x30\x40\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    s1 = '\x00\x1f\x2f\x30\x40\x50\x60\x70\x81\x0f'
    serial_port.write(s1.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    s2 = '\x00\x1f\x2f\x30\x40\x50\x60\x70\x80\x0f'
    serial_port.write(s2.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def update_config_period_str(config_period):
    if (config_period > 4095) or (config_period < 0):
        print("Error the config_period is not in 0-4095")
        return ''
    content_str = '\x00'+'\x1f\x2f\x30\x41\x50'
    config_period_4bit_0 = config_period%16
    config_period = config_period//16
    config_period_4bit_1 = config_period%16
    config_period = config_period//16
    config_period_4bit_2 = config_period%16
    content_str = content_str+chr(6*16+0)
    content_str = content_str+chr(7*16+0)
    content_str = content_str+chr(8*16+10)
    content_str = content_str+'\x0f'
    return content_str


def update_config_period(config_period, serial_port):
    s = update_config_period_str(config_period)
    if len(s) != 0:
        serial_port.write(s.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    return len(s)


def update_bit_length_str(bit_length):
    if (bit_length > 512) or (bit_length < 1):
        print("Error the bit_length is not in 1-512")
        return ''
    bit_length_1=bit_length-1
    content_str = '\x00'+'\x1f\x2f\x30\x42\x50'
    bit_length_4bit_0 = bit_length_1%16
    bit_length_1 = bit_length_1//16
    bit_length_4bit_1 = bit_length_1%16
    bit_length_1 = bit_length_1//16
    bit_length_4bit_2 = bit_length_1%16
    content_str = content_str+chr(6*16+bit_length_4bit_2)
    content_str = content_str+chr(7*16+bit_length_4bit_1)
    content_str = content_str+chr(8*16+bit_length_4bit_0)
    content_str = content_str+'\x0f'
    return content_str


def update_bit_length(bit_length, serial_port):
    s = update_bit_length_str(bit_length)
    if len(s) != 0:
        serial_port.write(s.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    return len(s)


def update_JTAG_inst_str(JTAG_inst):
    if (len(JTAG_inst) != 1):
        print("Error the length of JTAG_inst is not 5bit")
        return ''
    content_str = '\x00'+'\x1f\x2f\x30\x43\x50\x60'
    byte_content = ord(JTAG_inst)
    high_4bit = byte_content // 16
    low_4bit = byte_content % 16
    content_str = content_str+chr(7*16+high_4bit)
    content_str = content_str+chr(8*16+low_4bit)
    content_str = content_str+'\x0f'
    return content_str


def update_JTAG_inst(JTAG_inst, serial_port):
    s = update_JTAG_inst_str(JTAG_inst)
    if len(s) != 0:
        serial_port.write(s.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    return len(s)


def trst_0(serial_port):
    s0 = '\x00\x1f\x2f\x30\x44\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def trst_1(serial_port):
    s1 = '\x00\x1f\x2f\x30\x44\x50\x60\x70\x81\x0f'
    serial_port.write(s1.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def get_update_reg(reg_num, serial_port):
    content_str = '\x00'+'\x1f\x2f\x31'
    content_str = content_str+chr(4*16+reg_num)
    content_str = content_str+'\x50\x60\x70\x80'+'\x0f'
    serial_port.write(content_str.encode('latin_1'))
    config_reg_content = serial_port.read(20)
    serial_port.reset_input_buffer()
    return config_reg_content

def get_ePLLconfig_reg(serial_port):
    content_str = '\x00' + '\x1f\x2f\x31\x43\x50\x60\x70\x80'+'\x0f'
    serial_port.write(content_str.encode('latin_1'))
    config_reg_content = str_to_bin(serial_port.read(20),'')[32:59]
    serial_port.reset_input_buffer()
    ePLLconfig_reg = {}
    ePllCapA = config_reg_content[25:27]
    ePLLconfig_reg['ePllCapA'] = ePllCapA
    ePllIcpA = config_reg_content[21:25]
    ePLLconfig_reg['ePllIcpA'] = ePllIcpA
    ePllResA = config_reg_content[17:21]
    ePLLconfig_reg['ePllResA'] = ePllResA
    phase_clk320_2 = config_reg_content[13:17]
    ePLLconfig_reg['phase_clk320_2'] = phase_clk320_2
    phase_clk320_1 = config_reg_content[9:13]
    ePLLconfig_reg['phase_clk320_1'] = phase_clk320_1
    phase_clk320_0 = config_reg_content[5:9]
    ePLLconfig_reg['phase_clk320_0'] = phase_clk320_0
    phase_clk160 = config_reg_content[0:5]
    ePLLconfig_reg['phase_clk160'] = phase_clk160
    return ePLLconfig_reg


def get_line_lock_status(serial_port):
    content_str = '\x00' + '\x1f\x2f\x31\x45\x50\x60\x70\x80'+'\x0f'
    serial_port.write(content_str.encode('latin_1'))
    config_reg_content = str_to_bin(serial_port.read(20),'')
    serial_port.reset_input_buffer()
    line_lock_status = {}
    edge_select_1 = config_reg_content[159]
    line_lock_status['edge_select_1'] = edge_select_1
    edge_select_0 = config_reg_content[158]
    line_lock_status['edge_select_0'] = edge_select_0
    locked_1 = config_reg_content[157]
    line_lock_status['locked_1'] = locked_1
    locked_0 = config_reg_content[156]
    line_lock_status['locked_0'] = locked_0
    return line_lock_status


# def get_fifo_reg(serial_port):
#     content_str = '\x00'+'\x1f\x2f\x31'
#     reg_num = 8
#     content_str = content_str+chr(4*16+reg_num)
#     content_str = content_str+'\x50\x60\x70\x80'+'\x0f'
#     serial_port.write(content_str.encode('latin_1'))
#     config_reg_content = serial_port.read(20)
#     serial_port.reset_input_buffer()
#     return config_reg_content


# def reset_fifo(serial_port):
#     s0 = '\x00\x1f\x2f\x30\x48\x50\x60\x70\x81\x0f'
#     serial_port.write(s0.encode('latin_1'))
#     serial_port.flush()
#     time.sleep(0.01)
#     return 1


# def enable_fifo(serial_port):
#     s0 = '\x00\x1f\x2f\x30\x48\x50\x60\x70\x80\x0f'
#     serial_port.write(s0.encode('latin_1'))
#     serial_port.flush()
#     time.sleep(0.01)
#     return 1


def tdc_master_reset_1(serial_port):
    s0 = '\x00\x1f\x2f\x30\x49\x50\x60\x70\x81\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def tdc_master_reset_0(serial_port):
    s0 = '\x00\x1f\x2f\x30\x49\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def tdc_high_speed(serial_port):
    s0 = '\x00\x1f\x2f\x30\x4a\x50\x60\x70\x81\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def tdc_low_speed(serial_port):
    s0 = '\x00\x1f\x2f\x30\x4a\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def update_data_length_str(bit_length):
    if (bit_length > 5) or (bit_length < 3):
        print("Error the bit_length is not in 3-5")
        return ''
    content_str = '\x00'+'\x1f\x2f\x30\x4b\x50\x60\x70'
    content_str = content_str+chr(8*16+bit_length)
    content_str = content_str+'\x0f'
    return content_str


def update_data_length(serial_port,bit_length):
    s = update_data_length_str(bit_length)
    if len(s) != 0:
        serial_port.write(s.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    return len(s)


def tdc_trigger_mode(serial_port):
    s0 = '\x00\x1f\x2f\x30\x4c\x50\x60\x70\x81\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def tdc_triggerless_mode(serial_port):
    s0 = '\x00\x1f\x2f\x30\x4c\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1

def reselect_input_deserial(serial_port):
    s0 = '\x00\x1f\x2f\x30\x4d\x50\x60\x70\x81\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    s0 = '\x00\x1f\x2f\x30\x4d\x50\x60\x70\x80\x0f'
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 1


def update_input_deserial_para_str(correct_value_0='\x01\x93',correct_value_1='\x01\xF0',correct_counter_th=1000):
    content_str = '\x00' + '\x1f\x2f\x30\x40\x50\x64'
    content_str = content_str + '\x70\x80\x90\xa0\xb0\xc0\xd0\xe0\xf0\x10\x20\x30\x40\x50\x60\x70\x80\x90\xa0\xb0\xc0\xd0\xe0\xf0\x10\x20'
    content_str = content_str + chr(3*16+ord(correct_value_0[0]))
    byte_content = ord(correct_value_0[1])
    high_4bit = byte_content // 16
    content_str = content_str + chr(4 * 16 + high_4bit)
    low_4bit = byte_content % 16
    content_str = content_str + chr(5 * 16 + low_4bit)
    byte_content_1 = ord(correct_value_1[0])
    byte_content_2 = ord(correct_value_1[1])
    content_str = content_str + chr(6*16 + byte_content_1*4 + byte_content_2//64)
    content_str = content_str + chr(7*16 + (byte_content_2 - byte_content_2//64*64) // 4)
    content_str = content_str + chr(8*16 + byte_content_2 % 4 * 4 + correct_counter_th // 256)
    content_str = content_str + chr(9*16 + (correct_counter_th - correct_counter_th // 256 * 256) // 16)
    content_str = content_str + chr(10*16 + correct_counter_th % 16) + '\x0f'
    return content_str


def update_input_deserial_para(serial_port,correct_value_0='\x01\x93',correct_value_1='\x01\xF0',correct_counter_th=1000):
    s0= update_input_deserial_para_str(correct_value_0,correct_value_1,correct_counter_th)
    serial_port.write(s0.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(s0)


def update_hit_width(serial_port, width):
    content_str = '\x00' + '\x1f\x2f\x32\x40\x50'
    content_str = content_str + chr(6*16 + width//256)
    content_str = content_str + chr(7 * 16 + (width - width // 256 * 256)//16)
    content_str = content_str + chr(8 * 16 + width % 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)


def update_inv_hit(serial_port, inv):
    if inv == '0':
        content_str = '\x00' + '\x1f\x2f\x32\x42\x50\x60\x70\x81\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    else:
        content_str = '\x00' + '\x1f\x2f\x32\x42\x50\x60\x70\x80\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)


def update_hit_delay(serial_port,delay):
    if delay == 0:
        content_str = '\x00' + '\x1f\x2f\x32\x45\x50\x60\x70\x80\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    else:
        content_str = '\x00' + '\x1f\x2f\x32\x45\x50\x60\x70\x81\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)


def update_hit_mask_hit(serial_port,hit_mask):
    byte_content_0 = ord(hit_mask[0])
    byte_content_1 = ord(hit_mask[1])
    byte_content_2 = ord(hit_mask[2])
    content_str = '\x00' + '\x1f\x2f\x32\x44\x50'
    content_str = content_str + chr(6*16+byte_content_0//16)
    content_str = content_str + chr(7 * 16 + byte_content_0 % 16)
    content_str = content_str + chr(8 * 16 + byte_content_1 // 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    content_str = '\x00' + '\x1f\x2f\x32\x43\x50'
    content_str = content_str + chr(6*16+byte_content_1 % 16)
    content_str = content_str + chr(7 * 16 + byte_content_2 // 16)
    content_str = content_str + chr(8 * 16 + byte_content_2 % 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return 2*len(content_str)


def start_single_hit(serial_port):
    content_str = '\x00' + '\x1f\x2f\x32\x47\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    content_str = '\x00' + '\x1f\x2f\x32\x47\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)


def hit_start(serial_port):
    content_str = '\x00' + '\x1f\x2f\x32\x41\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)


def hit_stop(serial_port):
    content_str = '\x00' + '\x1f\x2f\x32\x41\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)


def update_hit_interval(serial_port, hit_interval):
    content_str = '\x00' + '\x1f\x2f\x32\x46\x50'
    content_str = content_str + chr(6*16 + hit_interval//256)
    content_str = content_str + chr(7 * 16 + (hit_interval - hit_interval // 256 * 256)//16)
    content_str = content_str + chr(8 * 16 + hit_interval % 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)


def ttc_mode_select(serial_port, new_ttc):
    if new_ttc == 1:
        content_str = '\x00' + '\x1f\x2f\x33\x45\x50\x60\x70\x81\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    else:
        content_str = '\x00' + '\x1f\x2f\x33\x45\x50\x60\x70\x80\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)


def update_ttc_delay(serial_port,delay):
    if delay == 0:
        content_str = '\x00' + '\x1f\x2f\x33\x47\x50\x60\x70\x80\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)
    else:
        content_str = '\x00' + '\x1f\x2f\x33\x47\x50\x60\x70\x81\x0f'
        serial_port.write(content_str.encode('latin_1'))
        serial_port.flush()
        time.sleep(0.01)




def update_new_ttc_code(serial_port,  new_ttc_code):
    content_str = '\x00' + '\x1f\x2f\x33\x46\x50\x60\x70'
    content_str = content_str + chr(16*8 + ord(new_ttc_code)) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)

def enable_ttc_trigger(serial_port):
    content_str = '\x00' + '\x1f\x2f\x33\x41\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x42\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x43\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x44\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)


def enable_ttc_BCR(serial_port):
    content_str = '\x00' + '\x1f\x2f\x33\x41\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x42\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x43\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x44\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)


def enable_ttc_event_reset(serial_port):
    content_str = '\x00' + '\x1f\x2f\x33\x41\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x42\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x43\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x44\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)

def enable_ttc_master_reset(serial_port):
    content_str = '\x00' + '\x1f\x2f\x33\x41\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x42\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x43\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x44\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)

def single_TTC(serial_port):
    content_str = '\x00' + '\x1f\x2f\x33\x40\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    content_str = '\x00' + '\x1f\x2f\x33\x40\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()

def update_bcr_roll_over(serial_port,roll_over):
    content_str = '\x00' + '\x1f\x2f\x34\x40\x50'
    content_str = content_str + chr(6 * 16 + roll_over // 256)
    content_str = content_str + chr(7 * 16 + (roll_over - roll_over // 256 * 256) // 16)
    content_str = content_str + chr(8 * 16 + roll_over % 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)

# def enable_bcr(serial_port):
#     content_str = '\x00' + '\x1f\x2f\x34\x41\x50\x60\x70\x81\x0f'
#     serial_port.write(content_str.encode('latin_1'))
#     serial_port.flush()
#     time.sleep(0.01)
#     return len(content_str)


# def disable_bcr(serial_port):
#     content_str = '\x00' + '\x1f\x2f\x34\x41\x50\x60\x70\x80\x0f'
#     serial_port.write(content_str.encode('latin_1'))
#     serial_port.flush()
#     time.sleep(0.01)
#     return len(content_str)


def update_ttc_interval(serial_port,interval):
    content_str = '\x00' + '\x1f\x2f\x34\x42\x50'
    content_str = content_str + chr(6 * 16 + interval // 256)
    content_str = content_str + chr(7 * 16 + (interval - interval // 256 * 256) // 16)
    content_str = content_str + chr(8 * 16 + interval % 16) + '\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)

def start_ttc(serial_port):
    content_str = '\x00' + '\x1f\x2f\x34\x43\x50\x60\x70\x81\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)

def stop_ttc(serial_port):
    content_str = '\x00' + '\x1f\x2f\x34\x43\x50\x60\x70\x80\x0f'
    serial_port.write(content_str.encode('latin_1'))
    serial_port.flush()
    time.sleep(0.01)
    return len(content_str)