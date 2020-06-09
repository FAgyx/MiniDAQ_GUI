HPTDC_INSTLENGTH = 5
A3P250_INSTLENGTH = 8
CSM_INSTLENGTH = 6
TTCRX_INSTLENGTH = 4
GOL_INSTLENGTH = 5
XC2V2000_INSTLENGTH = 6
PROM_INSTLENGTH = 16

INSTR_LENGTH_ALL = HPTDC_INSTLENGTH + A3P250_INSTLENGTH + CSM_INSTLENGTH\
    + TTCRX_INSTLENGTH + GOL_INSTLENGTH + XC2V2000_INSTLENGTH + PROM_INSTLENGTH

# for bypass

# PROMID = XCF08PID;
#             PROMINSTLENGTH = 16;



HPTDC_BYPASS = format(0x0F,'b').zfill(HPTDC_INSTLENGTH)
A3P250_BYPASS = format(0xFF,'b').zfill(A3P250_INSTLENGTH)
CSM_BYPASS = format(0x3F,'b').zfill(CSM_INSTLENGTH)
TTCRX_BYPASS = format(0xF,'b').zfill(TTCRX_INSTLENGTH)
GOL_BYPASS = format(0x1F,'b').zfill(GOL_INSTLENGTH)
XC2V2000_BYPASS = format(0x3F,'b').zfill(XC2V2000_INSTLENGTH)
PROM_BYPASS = format(0xFFFF,'b').zfill(PROM_INSTLENGTH)


INSTR_BYPASS_ALL = PROM_BYPASS + XC2V2000_BYPASS + GOL_BYPASS\
    + TTCRX_BYPASS + CSM_BYPASS + A3P250_BYPASS+ HPTDC_BYPASS

SIR_ALL_BYPASS = format(int(INSTR_BYPASS_ALL,2),'x').zfill\
    (len(INSTR_BYPASS_ALL)/4+int((len(INSTR_BYPASS_ALL)%4!=0)))
SMASK_ALL_BYPASS = format(int(len(INSTR_BYPASS_ALL)*'1',2),'x').zfill\
    (len(INSTR_BYPASS_ALL)/4+int((len(INSTR_BYPASS_ALL)%4!=0)))
print('TDI:'+INSTR_BYPASS_ALL)
print('SIR_BYPASS  = '+SIR_ALL_BYPASS)
print('SMASK_BYPASS= '+SMASK_ALL_BYPASS)



HPTDC_IDCODE = format(0x11,'b').zfill(HPTDC_INSTLENGTH)
A3P250_IDCODE = format(0x70,'b').zfill(A3P250_INSTLENGTH)
CSM_IDCODE = format(0x09,'b').zfill(CSM_INSTLENGTH)
TTCRX_IDCODE = format(0x1,'b').zfill(TTCRX_INSTLENGTH)
GOL_IDCODE = format(0x01,'b').zfill(GOL_INSTLENGTH)
XC2V2000_IDCODE = format(0x09,'b').zfill(XC2V2000_INSTLENGTH)
PROM_IDCODE = format(0xFE,'b').zfill(PROM_INSTLENGTH)

INSTR_IDCODE_ALL = PROM_IDCODE + XC2V2000_IDCODE + GOL_IDCODE\
    + TTCRX_IDCODE + CSM_IDCODE + A3P250_IDCODE+ HPTDC_IDCODE

SIR_ALL_IDCODE = format(int(INSTR_IDCODE_ALL,2),'x').zfill\
    (len(INSTR_IDCODE_ALL)/4+int((len(INSTR_IDCODE_ALL)%4!=0)))
SMASK_ALL_IDCODE = format(int(len(INSTR_IDCODE_ALL)*'1',2),'x').zfill\
    (len(INSTR_IDCODE_ALL)/4+int((len(INSTR_IDCODE_ALL)%4!=0)))
print('SIR_IDCODE  = '+SIR_ALL_IDCODE)
print('SMASK_IDCODE= '+SMASK_ALL_IDCODE)