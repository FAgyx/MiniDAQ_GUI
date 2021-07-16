import xml.etree.ElementTree as xml
import sys, os, subprocess
# import gbt_vldb

DEBUG = True
ADDRESS_TABLE_TOP = './registers.xml'
nodes = []

# gbt = gbt_vldb.GBTx()
TOP_NODE_NAME = "LPGBT"

class Node:
    name = ''
    vhdlname = ''
    address = 0x0
    real_address = 0x0
    permission = ''
    mask = 0x0
    lsb_pos = 0x0
    isModule = False
    parent = None
    level = 0
    mode = None

    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getVhdlName(self):
        return self.name.replace(TOP_NODE_NAME + '.', '').replace('.', '_')

    def output(self):
        print('Name:',self.name)
        print('Address:','{0:#010x}'.format(self.address))
        print('Permission:',self.permission)
        print('Mask:',self.mask)
        print('LSB:',self.lsb_pos)
        print('Module:',self.isModule)
        print('Parent:',self.parent.name)

def main():

    parseXML()
    print('Example:')
    # random_node = nodes[1]
    # random_node.output()
    # i=0
    # for node in nodes:
    #     print(i)
    #     if (i>0):
    #         node.output()
    #     i=i+1

    # print("  whattt  ")
    writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 0x3)
    print("output")
    getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE").output()

    print(" ")
    print("FRESH VALUE")

    writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 0x1)
    print("output")
    getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE").output()
    # writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX1DATARATE"), 0x3)
    # writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12ENABLE"), 0x2)

    #print (gbt.gbtx_read_register(320))
    #print str(random_node.__class__.__name__)
    #print 'Node:',random_node.name
    #print 'Parent:',random_node.parent.name
    #kids = []
    #getAllChildren(random_node, kids)
    #print len(kids), kids.name

def parseXML(filename = None, num_of_oh = None):
    if filename == None:
        filename = ADDRESS_TABLE_TOP
    print('Parsing',filename,'...')
    tree = xml.parse(filename)
    root = tree.getroot()[0]
    vars = {}
    makeTree(root,'',0x0,nodes,None,vars,False,num_of_oh)

def makeTree(node,baseName,baseAddress,nodes,parentNode,vars,isGenerated,num_of_oh=None):

    if (isGenerated == None or isGenerated == False) and node.get('generate') is not None and node.get('generate') == 'true':
        if (node.get('generate_idx_var') == 'OH_IDX' and num_of_oh is not None):
            generateSize = num_of_oh
        else:
            generateSize = parseInt(node.get('generate_size'))
        # generateSize = parseInt(node.get('generate_size'))
        generateAddressStep = parseInt(node.get('generate_address_step'))
        generateIdxVar = node.get('generate_idx_var')
        for i in range(0, generateSize):
            vars[generateIdxVar] = i
            #print('generate base_addr = ' + hex(baseAddress + generateAddressStep * i) + ' for node ' + node.get('id'))
            makeTree(node, baseName, baseAddress + generateAddressStep * i, nodes, parentNode, vars, True)
        return
    newNode = Node()
    name = baseName
    if baseName != '': name += '.'
    name += node.get('id')
    name = substituteVars(name, vars)
    newNode.name = name
    address = baseAddress
    if node.get('address') is not None:
        address = baseAddress + parseInt(eval(node.get('address')))
    newNode.address = address
    newNode.real_address = address
    newNode.permission = node.get('permission')
    newNode.mask = parseInt(node.get('mask'))
    newNode.lsb_pos = mask_to_lsb(newNode.mask)
    newNode.isModule = node.get('fw_is_module') is not None and node.get('fw_is_module') == 'true'
    if node.get('mode') is not None:
        newNode.mode = node.get('mode')
    nodes.append(newNode)
    if parentNode is not None:
        parentNode.addChild(newNode)
        newNode.parent = parentNode
        newNode.level = parentNode.level+1
    for child in node:
        makeTree(child,name,address,nodes,newNode,vars,False,num_of_oh)

def getAllChildren(node,kids=[]):
    if node.children==[]:
        kids.append(node)
        return kids
    else:
        for child in node.children:
            getAllChildren(child,kids)

def getNode(nodeName):
    thisnode = next(
        (node for node in nodes if node.name == nodeName),None
    )

    if (thisnode == None):
        print(nodeName)
    return thisnode

def getNodebyID(number):
    return nodes[number]

def getNodeFromAddress(nodeAddress):
    return next((node for node in nodes if node.real_address == nodeAddress),None)

def getNodesContaining(nodeString):
    nodelist = [node for node in nodes if nodeString in node.name]
    if len(nodelist): return nodelist
    else: return None

#returns *readable* registers
def getRegsContaining(nodeString):
    nodelist = [node for node in nodes if nodeString in node.name and node.permission is not None and 'r' in node.permission]
    if len(nodelist): return nodelist
    else: return None


def readAddress(address):
    try:
        output = subprocess.check_output('mpeek '+str(address), stderr=subprocess.STDOUT , shell=True)
        value = ''.join(s for s in output if s.isalnum())
    except subprocess.CalledProcessError as e: value = parseError(int(str(e)[-1:]))
    return '{0:#010x}'.format(parseInt(str(value)))

def readRawAddress(raw_address):
    try:
        address = (parseInt(raw_address) << 2)+0x64000000
        return readAddress(address)
    except:
        return 'Error reading address. (rw_reg)'

def mpeek(address):
    return gbt.gbtx_read_register(address)

def mpoke(address,value):
    gbt.gbtx_write_register(address,value)

def readRegStr(reg):
    return '{0:#010x}'.format(readReg(reg))

def readReg(reg):

    address = reg.real_address

    if 'r' not in reg.permission:
        return 'No read permission!'

    # read
    value = mpeek (address)

    # Apply Mask
    if (reg.mask != 0):
        value = (reg.mask & value) >> reg.lsb_pos

    return value

def displayReg(reg,option=None):
    address = reg.real_address
    if 'r' not in reg.permission:
        return 'No read permission!'
    # mpeek
    value = mpeek(address)
    # Apply Mask
    if reg.mask is not None:
        shift_amount=0
        for bit in reversed('{0:b}'.format(reg.mask)):
            if bit=='0': shift_amount+=1
            else: break
        final_value = (parseInt(str(reg.mask))&parseInt(value)) >> shift_amount
    else: final_value = value
    final_int =  parseInt(str(final_value))

    if option=='hexbin': return hex(address).rstrip('L')+' '+reg.permission+'\t'+tabPad(reg.name,7)+'{0:#010x}'.format(final_int)+' = '+'{0:032b}'.format(final_int)
    else: return hex(address).rstrip('L')+' '+reg.permission+'\t'+tabPad(reg.name,7)+'{0:#010x}'.format(final_int)

def writeReg(reg, value, readback=0):
    print("New Register")
    try: address = reg.real_address
    except:
        print('Reg',reg,'not a Node')
        return
    if 'w' not in reg.permission:
        return 'No write permission!'

    if (readback):
        if (value!=readReg(reg)):
            print("Failed to read back register %s. Expect=0x%x Read=0x%x" % (reg.name, value, redReg(reg)))
    else:
        # Apply Mask if applicable
        if (reg.mask != 0):
            # print("This is the value: ", value)
            print("This is the value: %s " % value)
            value = int(value, 16) << reg.lsb_pos
            value = value & 0xff
            print(value)

            # print("This is the old way: ")

            # value = value << reg.lsb_pos
            # value = value & reg.mask
            # print(value)

            # # value = hex(int(value, 16))
            # # value = value << reg.lsb_pos
            # print("value initial: ",  value)
            # print("lsb position: ", reg.lsb_pos)
            # print("value mask: ", reg.mask)
            # # valueness = value & reg.mask
            # # print("new value: ", valueness)
            # # print("address: ", address)
            # # print("address: ", address)
            # # print("mask: ", reg.mask)

            # if 'r' in reg.permission:
            #     value_new = (value) | (10100111 & ~reg.mask)
            #
            # print(value_new)

            # if 'r' in reg.permission:
            #     value = (value) | (mpeek(address) & ~reg.mask)


        # # mpoke
        # mpoke (address, value)

def isValid(address):
    #try: subprocess.check_output('mpeek '+str(address), stderr=subprocess.STDOUT , shell=True)
    #except subprocess.CalledProcessError as e: return False
    return True


def completeReg(string):
    possibleNodes = []
    completions = []
    currentLevel = len([c for c in string if c=='.'])

    possibleNodes = [node for node in nodes if node.name.startswith(string) and node.level == currentLevel]
    if len(possibleNodes)==1:
        if possibleNodes[0].children == []: return [possibleNodes[0].name]
        for n in possibleNodes[0].children:
            completions.append(n.name)
    else:
        for n in possibleNodes:
            completions.append(n.name)
    return completions


def parseError(e):
    if e==1:
        return "Failed to parse address"
    if e==2:
        return "Bus error"
    else:
        return "Unknown error: "+str(e)

def parseInt(s):
    if s is None:
        return None
    string = str(s)
    if string.startswith('0x'):
        return int(string, 16)
    elif string.startswith('0b'):
        return int(string, 2)
    else:
        return int(string)


def substituteVars(string, vars):
    if string is None:
        return string
    ret = string
    for varKey in list(vars.keys()):
        ret = ret.replace('${' + varKey + '}', str(vars[varKey]))
    return ret

def tabPad(s,maxlen):
    return s+"\t"*((8*maxlen-len(s)-1)/8+1)


def mask_to_lsb(mask):
    if mask is None:
        return 0
    if (mask&0x1):
        return 0
    else:
        idx=1
        while (True):
            mask=mask>>1
            if (mask&0x1):
                return idx
            idx = idx+1


if __name__ == '__main__':
    main()
