## This will be the file that takes the GUI values and saves them with their addresses ##
 ## Have the current values be the indicies!

register = []
add_and_reg = []
plop = 2

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
        # #CH 0
        # if var in range(7, 12):
        #     address = hex(196 + 4*val + 8)
        #     binary = bin(int(value_start)).replace('0b', '')
        #     if var == 7:
        #         x = binary[::-1]  # this reverses an array
        #         while len(x) < 4:
        #             x += '0'
        #             binary = x[::-1]
        #     register.append(binary)
        #     if len(register) > 4:
        #         hex_val = hex(int("".join(register), 2))
        #         add_and_reg.append([address, "".join(register), hex_val])
        #         del register[:]
        # #CH 1
        # if var in range(12, 17):
        #     address = hex(196 + 4*val + 8 + 1)
        #     binary = bin(int(value_start)).replace('0b', '')
        #     if var == 12:
        #         x = binary[::-1]  # this reverses an array
        #         while len(x) < 4:
        #             x += '0'
        #             binary = x[::-1]
        #     register.append(binary)
        #     if len(register) > 4:
        #         hex_val = hex(int("".join(register), 2))
        #         add_and_reg.append([address, "".join(register), hex_val])
        #         del register[:]

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
                    # add_and_reg.append([address, "".join(register), hex_val])
                    add_and_reg.append([address, hex_val])
                    del register[:]
            beginning += 5
            ending += 5
            inc += 1




def post_function():
    # print(add_and_reg)
    del add_and_reg[:]


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




print(add_and_reg)
