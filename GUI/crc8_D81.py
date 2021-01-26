# ////////////////////////////////////////////////////////////////////////////////
# // Copyright (C) 1999-2008 Easics NV.
# // This source file may be used and distributed without restriction
# // provided that this copyright statement is not removed from the file
# // and that any derivative work contains the original copyright notice
# // and the associated disclaimer.
# //
# // THIS SOURCE FILE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS
# // OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
# // WARRANTIES OF MERCHANTIBILITY AND FITNESS FOR A PARTICULAR PURPOSE.
# //
# // Purpose : synthesizable CRC function
# //   * polynomial: x^8 + x^5 + x^3 + x^2 + x^1 + 1
# //   * data width: 81
# //
# // Info : tools@easics.be
# //        http://www.easics.com
# ////////////////////////////////////////////////////////////////////////////////
def crc8_D81(Data):
    c = [0,0,0,0,0,0,0,0]
    newcrc = [0,0,0,0,0,0,0,0]
    d = [int(Data[80-i]) for i in range(len(Data))]
    newcrc[7] = d[79] ^ d[77] ^ d[72] ^ d[70] ^ d[69] ^ d[67] ^ d[64] ^ d[63] ^ d[61] ^ d[59] ^ d[58] ^ d[54] ^ d[53] ^ d[51] ^ d[50] ^ d[49] ^ d[46] ^ d[45] ^ d[44] ^ d[42] ^ d[38] ^ d[37] ^ d[36] ^ d[35] ^ d[33] ^ d[32] ^ d[31] ^ d[30] ^ d[27] ^ d[25] ^ d[24] ^ d[23] ^ d[22] ^ d[21] ^ d[15] ^ d[12] ^ d[11] ^ d[10] ^ d[9] ^ d[8] ^ d[7] ^ d[5] ^ d[3] ^ d[0] ^ c[4] ^ c[6]
    newcrc[6] = d[80] ^ d[79] ^ d[78] ^ d[77] ^ d[73] ^ d[72] ^ d[71] ^ d[69] ^ d[68] ^ d[67] ^ d[65] ^ d[63] ^ d[62] ^ d[61] ^ d[60] ^ d[58] ^ d[55] ^ d[53] ^ d[52] ^ d[49] ^ d[47] ^ d[44] ^ d[43] ^ d[42] ^ d[39] ^ d[35] ^ d[34] ^ d[30] ^ d[28] ^ d[27] ^ d[26] ^ d[21] ^ d[16] ^ d[15] ^ d[13] ^ d[7] ^ d[6] ^ d[5] ^ d[4] ^ d[3] ^ d[1] ^ d[0] ^ c[0] ^ c[4] ^ c[5] ^ c[6] ^ c[7]
    newcrc[5] = d[80] ^ d[78] ^ d[77] ^ d[74] ^ d[73] ^ d[68] ^ d[67] ^ d[66] ^ d[62] ^ d[58] ^ d[56] ^ d[51] ^ d[49] ^ d[48] ^ d[46] ^ d[43] ^ d[42] ^ d[40] ^ d[38] ^ d[37] ^ d[33] ^ d[32] ^ d[30] ^ d[29] ^ d[28] ^ d[25] ^ d[24] ^ d[23] ^ d[21] ^ d[17] ^ d[16] ^ d[15] ^ d[14] ^ d[12] ^ d[11] ^ d[10] ^ d[9] ^ d[6] ^ d[4] ^ d[3] ^ d[2] ^ d[1] ^ d[0] ^ c[0] ^ c[1] ^ c[4] ^ c[5] ^ c[7]
    newcrc[4] = d[78] ^ d[77] ^ d[75] ^ d[74] ^ d[72] ^ d[70] ^ d[68] ^ d[64] ^ d[61] ^ d[58] ^ d[57] ^ d[54] ^ d[53] ^ d[52] ^ d[51] ^ d[47] ^ d[46] ^ d[45] ^ d[43] ^ d[42] ^ d[41] ^ d[39] ^ d[37] ^ d[36] ^ d[35] ^ d[34] ^ d[32] ^ d[29] ^ d[27] ^ d[26] ^ d[23] ^ d[21] ^ d[18] ^ d[17] ^ d[16] ^ d[13] ^ d[9] ^ d[8] ^ d[4] ^ d[2] ^ d[1] ^ d[0] ^ c[1] ^ c[2] ^ c[4] ^ c[5]
    newcrc[3] = d[79] ^ d[78] ^ d[76] ^ d[75] ^ d[73] ^ d[71] ^ d[69] ^ d[65] ^ d[62] ^ d[59] ^ d[58] ^ d[55] ^ d[54] ^ d[53] ^ d[52] ^ d[48] ^ d[47] ^ d[46] ^ d[44] ^ d[43] ^ d[42] ^ d[40] ^ d[38] ^ d[37] ^ d[36] ^ d[35] ^ d[33] ^ d[30] ^ d[28] ^ d[27] ^ d[24] ^ d[22] ^ d[19] ^ d[18] ^ d[17] ^ d[14] ^ d[10] ^ d[9] ^ d[5] ^ d[3] ^ d[2] ^ d[1] ^ c[0] ^ c[2] ^ c[3] ^ c[5] ^ c[6]
    newcrc[2] = d[80] ^ d[76] ^ d[74] ^ d[69] ^ d[67] ^ d[66] ^ d[64] ^ d[61] ^ d[60] ^ d[58] ^ d[56] ^ d[55] ^ d[51] ^ d[50] ^ d[48] ^ d[47] ^ d[46] ^ d[43] ^ d[42] ^ d[41] ^ d[39] ^ d[35] ^ d[34] ^ d[33] ^ d[32] ^ d[30] ^ d[29] ^ d[28] ^ d[27] ^ d[24] ^ d[22] ^ d[21] ^ d[20] ^ d[19] ^ d[18] ^ d[12] ^ d[9] ^ d[8] ^ d[7] ^ d[6] ^ d[5] ^ d[4] ^ d[2] ^ d[0] ^ c[1] ^ c[3] ^ c[7]
    newcrc[1] = d[77] ^ d[75] ^ d[70] ^ d[68] ^ d[67] ^ d[65] ^ d[62] ^ d[61] ^ d[59] ^ d[57] ^ d[56] ^ d[52] ^ d[51] ^ d[49] ^ d[48] ^ d[47] ^ d[44] ^ d[43] ^ d[42] ^ d[40] ^ d[36] ^ d[35] ^ d[34] ^ d[33] ^ d[31] ^ d[30] ^ d[29] ^ d[28] ^ d[25] ^ d[23] ^ d[22] ^ d[21] ^ d[20] ^ d[19] ^ d[13] ^ d[10] ^ d[9] ^ d[8] ^ d[7] ^ d[6] ^ d[5] ^ d[3] ^ d[1] ^ c[2] ^ c[4]
    newcrc[0] = d[78] ^ d[76] ^ d[71] ^ d[69] ^ d[68] ^ d[66] ^ d[63] ^ d[62] ^ d[60] ^ d[58] ^ d[57] ^ d[53] ^ d[52] ^ d[50] ^ d[49] ^ d[48] ^ d[45] ^ d[44] ^ d[43] ^ d[41] ^ d[37] ^ d[36] ^ d[35] ^ d[34] ^ d[32] ^ d[31] ^ d[30] ^ d[29] ^ d[26] ^ d[24] ^ d[23] ^ d[22] ^ d[21] ^ d[20] ^ d[14] ^ d[11] ^ d[10] ^ d[9] ^ d[8] ^ d[7] ^ d[6] ^ d[4] ^ d[2] ^ c[3] ^ c[5]
    newcrc_bin = ''
    for b in newcrc:
        newcrc_bin += str(b)
    return newcrc_bin


def crc_cal(TDC_inst):
    setup_0_bin_str = ''
    for s in TDC_inst.setup_0:
        setup_0_bin_str = setup_0_bin_str + ''.join(s)
    setup_1_bin_str = ''
    for s in TDC_inst.setup_1:
        setup_1_bin_str = setup_1_bin_str + ''.join(s)
    setup_2_bin_str = ''
    for s in TDC_inst.setup_2:
        setup_2_bin_str = setup_2_bin_str + ''.join(s)
    control_0_bin_str = ''
    for s in TDC_inst.control_0:
        control_0_bin_str = control_0_bin_str + ''.join(s)
    control_1_bin_str = ''
    for s in TDC_inst.control_1:
        control_1_bin_str = control_1_bin_str + ''.join(s)
    total_reg = control_0_bin_str + control_1_bin_str + setup_2_bin_str + setup_1_bin_str + setup_0_bin_str
    CRC_out_bin_str = crc8_D81(24*'0'+total_reg[0:57])+crc8_D81(total_reg[57:138])+crc8_D81(total_reg[138:219])+crc8_D81(total_reg[219:300])
    CRC_out_hex_str = format(int(CRC_out_bin_str, 2), '08X')
    return CRC_out_hex_str