## This will be the file that takes the GUI values and saves them with their addresses ##
 ## Have the current values be the indicies!
from operator import itemgetter
import xml.etree.ElementTree as ET

register = []
add_and_reg = []
plop = []

# EPCLK EXAMPLE: function(what general button it is under {ex: EPCLK}, what item under that {ex: which EPCLK}, sub
# elements of one register, the index chosen from GUI)


def function(tab, val, var, value_start):
    # EPCLK
    if tab == 4:
        # choose the certain EPCLK
        if val in range(0, 29):
            address = hex(108 + 2 * val)
            # EPCLK_CHNCNTRH
            if var in range(0, 3):
                binary = bin(int(value_start)).replace('0b', '')
                if var > 0:
                    x = binary[::-1]  # this reverses an array
                    while len(x) < 3:
                        x += '0'
                    binary = x[::-1]
                register.append(binary)
                if len(register) > 2:
                    hex_val = hex(int("".join(register), 2))
                    name = 'EPCLK%iCHNCNTRH' % val
                    # add_and_reg.append([address, "".join(register), hex_val])
                    # add_and_reg.append([address, name, hex_val])
                    add_and_reg.append([address, hex_val])
                    del register[:]

            # EPCLK_CHNCNTRL
            if var in range(3, 6):
                address = hex(108 + 2 * val + 1)
                binary = bin(int(value_start)).replace('0b', '')
                if var == 4:
                    x = binary[::-1]
                    while len(x) < 2:
                        x += '0'
                    binary = x[::-1]
                else:
                    x = binary[::-1]
                    while len(x) < 3:
                        x += '0'
                    binary = x[::-1]
                register.append(binary)
                if len(register) > 2:
                    hex_val = hex(int("".join(register), 2))
                    name = 'EPCLK%iCHNCNTRL' % val
                    # add_and_reg.append([address, "".join(register), hex_val])
                    # add_and_reg.append([address, name, hex_val])
                    add_and_reg.append([address, hex_val])
                    del register[:]


    #EQUALIZER
    if tab == 6:
        if var < 2:
            address = '0x37'
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]  # this reverses an array
            while len(x) < 2:
                x += '0'
            binary = x[::-1]
            register.append(binary)
            if len(register) > 1:
                hex_val = hex(int("".join(register), 2))
                name = 'EQ Config'
                add_and_reg.append([address, "".join(register), hex_val])
                # add_and_reg.append([address, name, hex_val])
                # add_and_reg.append([address, hex_val])
                del register[:]

        else:
            address = '0x38'
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]  # this reverses an array
            while len(x) < 2:
                x += '0'
            binary = x[::-1]
            register.append(binary)
            if len(register) > 3:
                hex_val = hex(int("".join(register), 2))
                name = 'EQ Res'
                add_and_reg.append([address, "".join(register), hex_val])
                # add_and_reg.append([address, name, hex_val])
                # add_and_reg.append([address, hex_val])
                del register[:]

    #EPRX
    if tab == 1:
        if var in range(0, 6):
            address = hex(196 + val)
            binary = bin(int(value_start)).replace('0b', '')
            if var > 3:
                x = binary[::-1]  # this reverses an array
                while len(x) < 2:
                    x += '0'
                binary = x[::-1]
            register.append(binary)
            if len(register) > 5:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), hex_val])
                del register[:]
        if var == 6:
            address = hex(196 + val)
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]  # this reverses an array
            while len(x) < 2:
                x += '0'
            binary = x[::-1]
            register.append(binary)
            hex_val = hex(int("".join(register), 2))
            add_and_reg.append([address, "".join(register), hex_val])
            del register[:]

        # Channel looping --
        beginning = 7
        ending = 12
        inc = 0
        for i in range(0, 4):
            if var in range(beginning, ending):
                address = hex(196 + 4*val + 8 + inc)
                binary = bin(int(value_start)).replace('0b', '')
                if var == beginning:
                    x = binary[::-1]  # this reverses an array
                    while len(x) < 4:
                        x += '0'
                    binary = x[::-1]
                register.append(binary)
                if len(register) > 4:
                    hex_val = hex(int("".join(register), 2))
                    add_and_reg.append([address, "".join(register), hex_val])
                    # add_and_reg.append([address, hex_val])
                    del register[:]
            beginning += 5
            ending += 5
            inc += 1

        #EC chn cntr
        if var in range(27, 34):
            address = hex(225 + val)
            binary = bin(int(value_start)).replace('0b', '')
            if var == 27:
                x = binary[::-1]  # this reverses an array
                while len(x) < 4:
                    x += '0'
                binary = x[::-1]
            register.append(binary)
            if len(register) > 4:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), hex_val])
                # add_and_reg.append([address, hex_val])
                del register[:]

    #PS CLK
    if tab == 5:
        #PS_Config & Delay
        if var in range(0, 4):
            address = hex(92 + 3*val)
            print(address)
            binary = bin(int(value_start)).replace('0b', '')
            if var == 0:
                binary = value_start
                x = binary[::-1]
                while len(x) < 8:
                    x += '0'
                binary = x[::-1]
                register.append(binary[0])
                add_and_reg.append([hex(93 + 3*val), binary, len(binary), hex(int(binary, 2))])
            if var == 1:
                register.append(binary)
            if var in range(2, 4):
                x = binary[::-1]
                while len(x) < 3:
                    x += '0'
                binary = x[::-1]
                register.append(binary)
            if len(register) > 3:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                print(val)
                del register[:]

        if var > 3:
            address = hex(94 + 3*val)
            binary = bin(int(value_start)).replace('0b', '')
            # x = binary[::-1]
            if var == 5:
                x = binary[::-1]
                while len(x) < 2:
                    x += '0'
                binary = x[::-1]
                register.append(binary)
            else:
                x = binary[::-1]
                while len(x) < 3:
                    x += '0'
                binary = x[::-1]
                register.append(binary)
            if len(register) > 2:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]

    # #EPTX -- Importing function!
    if tab == 0:
        #datarate register
        if var == 0:
            address = hex(167)
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]
            while len(x) < 2:
                x += '0'
            binary = x[::-1]
            register.append(binary)
            if len(register) > 3:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]
        #EPTX Control
        if var in (31, 26, 27, 6, 12, 18, 24):
            address = hex(168)
            binary = bin(int(value_start)).replace('0b', '')
            if var == 31:
                x = binary[::-1]
                while len(x) < 2:
                    x += '0'
                binary = x[::-1]
            register.append(binary)
            if len(register) > 6:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]
        #EPTX10Enable
        if var in (2, 8, 14, 20):
            address = 0
            if val in (0, 1):
                address = hex(169)
            if val in (2, 3):
                address = hex(170)
            binary = bin(int(value_start)).replace('0b', '')
            register.append(binary)
            if len(register) > 7:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]

        #EPTXExChnCntr
        if var in (28, 29, 30):
            address = hex(171)
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]
            if var == 29:
                while len(x) < 2:
                    x += '0'
                binary = x[::-1]
            if var in (28, 30):
                while len(x) < 3:
                    x += '0'
                binary = x[::-1]
            register.append(binary)
            if len(register) > 2:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]
        #EPTX__ChnCntr -- currently working on this!
        # if var in (3, 4, 5, 9, 10, 11, 15, 16, 17, 21, 22, 23):
        if var in (3, 4, 5, 9, 10, 11):
            address = 0
            #channel 0 in each group
            if var in range(3, 6):
                address = hex(172 + 4*val)
            if var in range(9, 12):
                address = hex(172 + 4*val + 1)
            binary = bin(int(value_start)).replace('0b', '')
            x = binary[::-1]
            if var in (3, 5, 9, 11):
                while len(x) < 3:
                    x += '0'
                binary = x[::-1]
            if var in (4, 10):
                while len(x) < 2:
                    x += '0'
                binary = x[::-1]
            register.append(binary)
            if len(register) > 2:
                hex_val = hex(int("".join(register), 2))
                add_and_reg.append([address, "".join(register), len("".join(register)), hex_val])
                del register[:]









def post_function():
    plop = sorted(add_and_reg, key=itemgetter(0))
    print(plop)

    # using element tree
    # from xml.dom import minidom
    #
    # root = ET.Element("RegisterID")
    #
    # for element in plop:
    #     print(element[0])
    #     print(type(element[0]))
    #     add = ET.SubElement(root, "l")
    #     add.text = " %s : %s " % (element[0], element[1])
    #
    # xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    # with open("Newest_Database.xml", "w") as f:
    #     f.write(xmlstr)
############################################################################
    # #using minidom
    # from xml.dom import minidom
    #
    # root = minidom.Document()
    # xml = root.createElement('root')
    # root.appendChild(xml)
    #
    # for user in plop:
    #     productChild = root.createElement(str(user[0]))
    #
    #     productChild.setAttribute('val', user[3])
    #     xml.appendChild(productChild)
    #
    # xml_str = root.toprettyxml(indent="\t")
    #
    # save_path_file = "%s.xml" % plop[0][0]
    #
    # with open(save_path_file, "w") as f:
    #     f.write(xml_str)
    #
    del add_and_reg[:]
############################################################################3


# function(4, 2, 0, '0')  # invert
# function(4, 2, 1, '4')  # drive strength
# function(4, 2, 2, '3')  # frequency
# #
# function(4, 2, 3, '0')  # PE strength
# function(4, 2, 4, '0')  # PE mode
# function(4, 2, 5, '0')  # PE width
#
# function(4, 3, 0, '0')
# function(4, 3, 1, '0')
# function(4, 3, 2, '0')
#
# function(4, 3, 3, '5')
# function(4, 3, 4, '0')
# function(4, 3, 5, '1')

# function(6, 0, 0, '1')
# function(6, 0, 1, '1')
#
# function(6, 0, 2, '0')
# function(6, 0, 3, '0')
# function(6, 0, 4, '0')
# function(6, 0, 5, '0')

# function(1, 0, 0, 1)
# function(1, 0, 1, 1)
# function(1, 0, 2, 1)
# function(1, 0, 3, 1)
# function(1, 0, 4, 1)
# function(1, 0, 5, 1)

# function(1, 0, 7, 1)
# function(1, 0, 8, 1)
# function(1, 0, 9, 1)
# function(1, 0, 10, 1)
# function(1, 0, 11, 1)
#
# function(1, 0, 12, 1)
# function(1, 0, 13, 1)
# function(1, 0, 14, 1)
# function(1, 0, 15, 1)
# function(1, 0, 16, 1)
