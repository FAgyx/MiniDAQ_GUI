from TDC_config_low_level_function import *

def ASD_config(ser,length,content):
    trst_1(ser)
    update_reg(0, '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', ser)
    update_reg(1, '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', ser)
    update_reg(2, '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', ser)
    update_reg(3, '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x09',ser)
    update_bit_length(length,ser)
    reg_num = length//128
    write_point=0
    for i in range(0,reg_num+1):
        if i == 0 :
            length_seg = length % 128
            str_temp = '\x00' * (15 - length_seg // 8) + content[0:length_seg//8+1]

            update_reg(reg_num-i, str_temp, ser)
            write_point = length_seg//8+1
        else:
            str_temp =  content[write_point:write_point+16]
            #print(reg_num-i)
            #print(str_to_hex(str_temp,'_'))
            update_reg(reg_num-i, str_temp, ser)
            write_point = write_point+16
    start_action(ser)


# verificate ID code
def verificate_ID_CODE(ser):
    ID_ref = b'\xfa\xde\xc0\x01'
    # ID_ref = '\x84\x70\xda\xce'
    trst_1(ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x11',ser)
    update_bit_length(32,ser)
    start_action(ser)
    chip_ID=get_update_reg(3,ser)[4:8]
    chip_ID_hex=str_to_hex(chip_ID,'_')
    chip_ID_bin=str_to_bin(chip_ID,'')
    if ID_ref != chip_ID:
        print('Chip ID check error')
        return False
    else:
        print('Chip ID check pass')
        return True

## verificate setup0
def verificate_setup0(ser):
    verificate_pass=True
    # verificate setup0 default
    setup0_default_ref=b'\x04\x2f\xff\xff\xff\xff\xff\xff\xff\xff\xff\x55\x54\x82\x00'
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x12',ser)
    update_bit_length(115,ser)
    start_action(ser)
    setup0_default=get_update_reg(3,ser)[4:19]
    setup0_default_hex=str_to_hex(setup0_default,'_')
    setup0_default_bin=str_to_bin(setup0_default,'')
    if setup0_default_ref != setup0_default:
        print('setup0 default check error')
        verificate_pass = False
    else:
        print('setup0 default check pass')
    # verificate setup0 0
    setup0_0_ref=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    setup0_0=get_update_reg(3,ser)[4:19]
    setup0_0_hex=str_to_hex(setup0_0,'_')
    setup0_0_bin=str_to_bin(setup0_0,'')
    if setup0_0_ref != setup0_0:
        print('setup0 0 check error')
        verificate_pass = False
    else:
        print('setup0 0 check pass')
    # verificate setup0 1
    setup0_1_ref=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0'
    start_action(ser)
    setup0_1=get_update_reg(3,ser)[4:19]
    setup0_1_hex=str_to_hex(setup0_1,'_')
    setup0_1_bin=str_to_bin(setup0_1,'')
    if setup0_1_ref != setup0_1:
        print('setup0 1 check error')
        verificate_pass = False
    else:
        print('setup0 1 check pass')
    return verificate_pass

## verificate setup1
def verificate_setup1(ser):
    verificate_pass = True
    # verificate setup1 default
    setup1_default_ref=b'\x0a\x04\x03\xff\xff\xfc\x00\x3e\x70\x00\x00\x7c'
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x03',ser)
    update_bit_length(94,ser)
    start_action(ser)
    setup1_default=get_update_reg(3,ser)[4:16]
    setup1_default_hex=str_to_hex(setup1_default,'_')
    setup1_default_bin=str_to_bin(setup1_default,'')
    if setup1_default_ref != setup1_default:
        print('setup1 default check error')
        verificate_pass = False
    else:
        print('setup1 default check pass')
    # verificate setup1 0
    setup1_0_ref=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    setup1_0=get_update_reg(3,ser)[4:16]
    setup1_0_hex=str_to_hex(setup1_0,'_')
    setup1_0_bin=str_to_bin(setup1_0,'')
    if setup1_0_ref != setup1_0:
        print('setup1 0 check error')
        verificate_pass = False
    else:
        print('setup1 0 check pass')
    # verificate setup1 1
    setup1_1_ref=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc'
    start_action(ser)
    setup1_1=get_update_reg(3,ser)[4:16]
    setup1_1_hex=str_to_hex(setup1_1,'_')
    setup1_1_bin=str_to_bin(setup1_1,'')
    if setup1_1_ref != setup1_1:
        print('setup1 1 check error')
        verificate_pass = False
    else:
        print('setup1 1 check pass')
    return verificate_pass

## verificate setup2
def verificate_setup2(ser):
    verificate_pass = True
    # verificate setup2 default
    setup2_default_ref=b'\x31\x9c\xa0\x1c\xc0'
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x14',ser)
    update_bit_length(36,ser)
    start_action(ser)
    setup2_default=get_update_reg(3,ser)[4:9]
    setup2_default_hex=str_to_hex(setup2_default,'_')
    setup2_default_bin=str_to_bin(setup2_default,'')
    if setup2_default_ref != setup2_default:
        print('setup2 default check error')
        verificate_pass = False
    else:
        print('setup2 default check pass')
    # verificate setup2 0
    setup2_0_ref=b'\x00\x00\x00\x00\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    setup2_0=get_update_reg(3,ser)[4:9]
    setup2_0_hex=str_to_hex(setup2_0,'_')
    setup2_0_bin=str_to_bin(setup2_0,'')
    if setup2_0_ref != setup2_0:
        print('setup2 0 check error')
        verificate_pass = False
    else:
        print('setup2 0 check pass')
    # verificate setup2 1
    setup2_1_ref=b'\xff\xff\xff\xff\xf0'
    start_action(ser)
    setup2_1=get_update_reg(3,ser)[4:9]
    setup2_1_hex=str_to_hex(setup2_1,'_')
    setup2_1_bin=str_to_bin(setup2_1,'')
    if setup2_1_ref != setup2_1:
        print('setup2 1 check error')
        verificate_pass = False
    else:
        print('setup2 1 check pass')
    return verificate_pass

## verificate control0
def verificate_control0(ser):
    verificate_pass = True
    # verificate control0 default
    control0_default_ref=b'\x00'
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x05',ser)
    update_bit_length(8,ser)
    start_action(ser)
    control0_default=get_update_reg(3,ser)[4:5]
    control0_default_hex=str_to_hex(control0_default,'_')
    control0_default_bin=str_to_bin(control0_default,'')
    if control0_default_ref != control0_default:
        print('control0 default check error')
        verificate_pass = False
    else:
        print('control0 default check pass')
    # verificate control0 0
    control0_0_ref=b'\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    control0_0=get_update_reg(3,ser)[4:5]
    control0_0_hex=str_to_hex(control0_0,'_')
    control0_0_bin=str_to_bin(control0_0,'')
    if control0_0_ref != control0_0:
        print('control0 0 check error')
        verificate_pass = False
    else:
        print('control0 0 check pass')
    # verificate control0 1
    control0_1_ref=b'\xff'
    start_action(ser)
    control0_1=get_update_reg(3,ser)[4:5]
    control0_1_hex=str_to_hex(control0_1,'_')
    control0_1_bin=str_to_bin(control0_1,'')
    if control0_1_ref != control0_1:
        print('control0 1 check error')
        verificate_pass = False
    else:
        print('control0 1 check pass')
    return verificate_pass

## verificate control1
def verificate_control1(ser):
    verificate_pass = True
    # verificate control1 default
    control1_default_ref=b'\x02\x01\x12\x44\x91\x24'
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x06',ser)
    update_bit_length(47,ser)
    start_action(ser)
    control1_default=get_update_reg(3,ser)[4:10]
    control1_default_hex=str_to_hex(control1_default,'_')
    control1_default_bin=str_to_bin(control1_default,'')
    if control1_default_ref != control1_default:
        print('control1 default check error')
        verificate_pass = False
    else:
        print('control1 default check pass')
    # verificate control1 0
    control1_0_ref=b'\x00\x00\x00\x00\x00\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    control1_0=get_update_reg(3,ser)[4:10]
    control1_0_hex=str_to_hex(control1_0,'_')
    control1_0_bin=str_to_bin(control1_0,'')
    if control1_0_ref != control1_0:
        print('control1 0 check error')
        verificate_pass = False
    else:
        print('control1 0 check pass')
    # verificate control1 1
    control1_1_ref=b'\xff\xff\xff\xff\xff\xfe'
    start_action(ser)
    control1_1=get_update_reg(3,ser)[4:10]
    control1_1_hex=str_to_hex(control1_1,'_')
    control1_1_bin=str_to_bin(control1_1,'')
    if control1_1_ref != control1_1:
        print('control1 1 check error')
        verificate_pass = False
    else:
        print('control1 1 check pass')
    return verificate_pass

## verificate spi 300bit
def verificate_spi(ser):
    verificate_pass = True
    #spi_default_ref='\x04\x2f\xff\xff\xff\xff\xff\xff\xff\xff\xf0\xaa\xaa\x82\x01\x40\x80\x7f\xff\xff\x80\x07\xce\x00\x00\x0f\x98\x02\x94\x6a\x6a\x34\xf4\x12\x51\x6e\x7a\x77\xe0\x02\x10\x80\x92'
    spi_default_ref=b'\x04\x2f\xff\xff\xff\xff\xff\xff\xff\xff\xf0\xaa\xaa\x82\x01\x40\x80\x7f\xff\xff\x80\x07\xce\x00\x00\x0f\x98\xce\x50\x0e\x60\x00\x10\x08\x92\x24\x89\x20'
    trst_1(ser)
    trst_0(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_bit_length(300,ser)
    start_action(ser)
    spi_default=get_update_reg(3,ser)[4:]+get_update_reg(2,ser)[4:]+get_update_reg(1,ser)[4:10]
    if spi_default != spi_default_ref:
        print('spi default check error!!!!!!!!!!!!!!!!!!!')
        verificate_pass = False
    else:
        print('spi default check pass')

    spi_0_ref=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    update_reg(0,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(1,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(2,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    update_reg(3,'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff',ser)
    start_action(ser)
    spi_0=get_update_reg(3,ser)[4:]+get_update_reg(2,ser)[4:]+get_update_reg(1,ser)[4:10]
    if spi_0_ref != spi_0:
        print('spi 0 check error!!!!!!!!!!!!!!!!!!!')
        verificate_pass = False
    else:
        print('spi 0 check pass')
    spi_1_ref=b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0'
    start_action(ser)
    spi_1=get_update_reg(3,ser)[4:]+get_update_reg(2,ser)[4:]+get_update_reg(1,ser)[4:10]
    if spi_1_ref != spi_1:
        print('spi 1 check error!!!!!!!!!!!!!!!!!!!')
        verificate_pass = False
    else:
        print('spi 1 check pass')
    return verificate_pass


## get status0 values
def get_status0(ser):
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x17',ser)
    update_bit_length(33,ser)
    start_action(ser)
    status0_default=get_update_reg(3,ser)[4:9]
    status0_default_hex=str_to_hex(status0_default,'_')
    status0_default_bin=str_to_bin(status0_default,'')[0:33]
    print(status0_default_bin)


def get_status1(ser):
    trst_0(ser)
    trst_1(ser)
    update_reg(0,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(1,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(2,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_reg(3,'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',ser)
    update_config_period(10,ser)
    update_JTAG_inst('\x18',ser)
    update_bit_length(25,ser)
    start_action(ser)
    status1_default=get_update_reg(3,ser)[4:9]
    status1_default_hex=str_to_hex(status1_default,'_')
    status1_default_bin=str_to_bin(status1_default,'')[0:25]
    print(status1_default_bin)
    
def verificate_all(ser):
    print("//////JTAG verification starts!//////")
    veri_result = [False,False,False,False,False,False,False]
    veri_result[0] = verificate_setup0(ser)
    veri_result[1] = verificate_setup1(ser)
    veri_result[2] = verificate_setup2(ser)
    veri_result[3] = verificate_control0(ser)
    veri_result[4] = verificate_control1(ser)
    veri_result[5] = verificate_ID_CODE(ser)
    veri_result[6] = verificate_spi(ser)
    if veri_result ==[True,True,True,True,True,True,True]:
        print("//////All JTAG verification passed!//////")
    else:
        print("//////JTAG verification failed!//////")

