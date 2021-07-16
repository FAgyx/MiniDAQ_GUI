#This file gets the xml saved files and performs writeReg() for each of the registers 
# it is read into the GUI when the Init GUI function is implemented 

from rw_reg_dongle_what_on_the_earth import writeReg,getNode
from rw_reg_dongle_what_on_the_earth import *
from time import sleep
import sys
import xml.etree.ElementTree as ET

#readback = 0

def ePortTX_writeReg(): 
	parseXML()
	tree_ePortTX = ET.parse('LpGBT_transfer.xml')
	# tree_ePortTX = ET.parse('LpGBT_auto_saved.xml')
	root = tree_ePortTX.getroot()

################## EportTX write registers ######################################
	# data rate
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), root[0][0][0].text)  # G0 data rate
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX1DATARATE"), root[0][1][0].text)  # G1 data rate
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX2DATARATE"), root[0][2][0].text)  # G2 data rate
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX3DATARATE"), root[0][3][0].text)  # G3 data rate

	# mirror enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0MIRRORENABLE"), root[0][0][1].text)  # G0 mirror enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX1MIRRORENABLE"), root[0][1][1].text)  # G1 mirror enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX2MIRRORENABLE"), root[0][2][1].text)  # G2 mirror enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX3MIRRORENABLE"), root[0][3][1].text)  # G3 mirror enable

	############################### GROUP 0 ####################################
	# group 0 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00ENABLE"), root[0][0][2][0].text)  # channel 0 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX01ENABLE"), root[0][0][3][0].text)  # channel 1 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX02ENABLE"), root[0][0][4][0].text)  # channel 2 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX03ENABLE"), root[0][0][5][0].text)  # channel 3 enable

	# group 0 channel invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00INVERT"), root[0][0][2][1].text)  # channel 0 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX01INVERT"), root[0][0][3][1].text)  # channel 1 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX02INVERT"), root[0][0][4][1].text)  # channel 2 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX03INVERT"), root[0][0][5][1].text)  # channel 3 invert

	# group 0 channel PE Width - don't know what the PE width register is called!
	# writeReg(getNode('LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX00PEWIDTH'), root[0][0][2][2].text)  # channel 0 PE width

	# group 0 channel PE strength - don't know register

	# group 0 Drive Strength - don't know the register
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX6DRIVESTRENGTH"), root[0][0][2][4].text) # channel 0 drive strength

	# group 0 PE mode - don't know register
	############################ GROUP 1 ######################################
	# group 1 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX10ENABLE"), root[0][1][2][0].text)  # channel 0 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX11ENABLE"), root[0][1][3][0].text)  # channel 1 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12ENABLE"), root[0][1][4][0].text)  # channel 2 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX13ENABLE"), root[0][1][5][0].text)  # channel 3 enable

	# group 1 channel invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX10INVERT"), root[0][1][2][1].text)  # channel 0 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX11INVERT"), root[0][1][3][1].text)  # channel 1 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12INVERT"), root[0][1][4][1].text)  # channel 2 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX13INVERT"), root[0][1][5][1].text)  # channel 3 invert

	# group 1 channel PE Width - don't know what the PE width register is called!

	# group 1 channel PE strength - don't know register

	# group 1 Drive Strength - don't know the register

	# group 1 PE mode - don't know register

	################################ GROUP 2 ###################################
	# group 2 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX20ENABLE"), root[0][2][2][0].text)  # channel 0 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX21ENABLE"), root[0][2][3][0].text)  # channel 1 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX22ENABLE"), root[0][2][4][0].text)  # channel 2 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX23ENABLE"), root[0][2][5][0].text)  # channel 3 enable

	# group 2 channel invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX20INVERT"), root[0][2][2][1].text)  # channel 0 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX21INVERT"), root[0][2][3][1].text)  # channel 1 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX22INVERT"), root[0][2][4][1].text)  # channel 2 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX23INVERT"), root[0][2][5][1].text)  # channel 3 invert

	# group 2 channel PE Width - don't know what the PE width register is called!

	# group 2 channel PE strength - don't know register

	# group 2 Drive Strength - don't know the register

	# group 2 PE mode - don't know register

	################################# GROUP 3 ###################################
	# group 3 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX30ENABLE"), root[0][3][2][0].text)  # channel 0 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX31ENABLE"), root[0][3][3][0].text)  # channel 1 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX32ENABLE"), root[0][3][4][0].text)  # channel 2 enable
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX33ENABLE"), root[0][3][5][0].text)  # channel 3 enable

	# group 3 channel invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX30INVERT"), root[0][3][2][1].text)  # channel 0 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX31INVERT"), root[0][3][3][1].text)  # channel 1 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX32INVERT"), root[0][3][4][1].text)  # channel 2 invert
	writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX33INVERT"), root[0][3][5][1].text)  # channel 3 invert

	# group 3 channel PE Width - don't know what the PE width register is called!

	# group 3 channel PE strength - don't know register

	# group 3 Drive Strength - don't know the register

	# group 3 PE mode - don't know register

########################## ePortRX write registers #####################################
	# Data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX0DATARATE"), root[1][0][0].text)  # G0 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX1DATARATE"), root[1][1][0].text)  # G1 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX2DATARATE"), root[1][2][0].text)  # G2 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX3DATARATE"), root[1][3][0].text)  # G3 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX4DATARATE"), root[1][4][0].text)  # G4 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX5DATARATE"), root[1][5][0].text)  # G5 data rate
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX6DATARATE"), root[1][6][0].text)  # G6 data rate

	# Tracking mode - not sure which of the two methods is accurate
	## taking the 0x0, 0x1, etc method
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX0TRACKMODE"), root[1][0][1].text)  # G0 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX1TRACKMODE"), root[1][1][1].text)  # G1 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX2TRACKMODE"), root[1][2][1].text)  # G2 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX3TRACKMODE"), root[1][3][1].text)  # G3 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX4TRACKMODE"), root[1][4][1].text)  # G4 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX5TRACKMODE"), root[1][5][1].text)  # G5 track mode
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX6TRACKMODE"), root[1][6][1].text)  # G6 track mode

	## taking the 0, 1, etc method
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX0TRACKMODE"), root[1][0][1].text[2])  # G0 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX1TRACKMODE"), root[1][1][1].text[2])  # G1 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX2TRACKMODE"), root[1][2][1].text[2])  # G2 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX3TRACKMODE"), root[1][3][1].text[2])  # G3 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX4TRACKMODE"), root[1][4][1].text[2])  # G4 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX5TRACKMODE"), root[1][5][1].text[2])  # G5 track mode
	# writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX6TRACKMODE"), root[1][6][1].text[2])  # G6 track mode


	################## GROUP 0 #########################
	# group 0 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX00ENABLE"), root[1][0][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX01ENABLE"), root[1][0][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX02ENABLE"), root[1][0][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX03ENABLE"), root[1][0][5][0].text)  # channel 3

	# group 0 channel phase

	# group 0 invert

	# group 0 AC bias

	#group 0 Term

	#group 0 Equilzation

	################## GROUP 1 #########################
	#group 1 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX10ENABLE"), root[1][1][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX11ENABLE"), root[1][1][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX12ENABLE"), root[1][1][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX13ENABLE"), root[1][1][5][0].text)  # channel 3

	# group 1 channel phase

	# group 1 invert

	# group 1 AC bias

	# group 1 Term

	# group 1 Equilzation

	################## GROUP 2 #########################
	#group 2 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX20ENABLE"), root[1][2][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX21ENABLE"), root[1][2][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX22ENABLE"), root[1][2][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX23ENABLE"), root[1][2][5][0].text)  # channel 3

	# group 2 channel phase

	# group 2 invert

	# group 2 AC bias

	# group 2 Term

	# group 2 Equilzation

	################## GROUP 3 #########################
	#group 3 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX30ENABLE"), root[1][3][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX31ENABLE"), root[1][3][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX32ENABLE"), root[1][3][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX33ENABLE"), root[1][3][5][0].text)  # channel 3

	# group 3 channel phase

	# group 3 invert

	# group 3 AC bias

	# group 3 Term

	# group 3 Equilzation

	################## GROUP 4 #########################
	#group 4 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX40ENABLE"), root[1][4][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX41ENABLE"), root[1][4][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX42ENABLE"), root[1][4][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX43ENABLE"), root[1][4][5][0].text)  # channel 3

	# group 4 channel phase

	# group 4 invert

	# group 4 AC bias

	# group 4 Term

	# group 4 Equilzation

	################## GROUP 5 #########################
	#group 5 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX50ENABLE"), root[1][5][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX51ENABLE"), root[1][5][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX52ENABLE"), root[1][5][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX53ENABLE"), root[1][5][5][0].text)  # channel 3

	# group 5 channel phase

	# group 5 invert

	# group 5 AC bias

	# group 5 Term

	# group 5 Equilzation

	################## GROUP 6 #########################
	#group 6 channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX60ENABLE"), root[1][6][2][0].text)  # channel 0
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX61ENABLE"), root[1][6][3][0].text)  # channel 1
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX62ENABLE"), root[1][6][4][0].text)  # channel 2
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRX63ENABLE"), root[1][6][5][0].text)  # channel 3

	# group 6 channel phase

	# group 6 invert

	# group 6 AC bias

	# group 6 Term

	# group 6 Equilzation

	################## EC CHANNEL ######################
	#EC channel enable
	writeReg(getNode("LPGBT.RWF.EPORTRX.EPRXECENABLE"), root[1][7][0].text)


























	# print(int(root[0][0].text))
	# print(root[0][0].text + "good")
	# print(hex(int(root[0][0].text[:-1])))
	# a = hex(int(root[0][0].text))
	# b = a[1:-1]
	# print(b)
	# if b == 0x0: 
	# 	print("all good")
	# if a == '0x0': 
	# 	print("Okay")
	# if int(a, 0): 
	# 	print("nice")
		# [:-1]
	# print(hex(root[0][0].text))

	#data rate for every group 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), hex(int(root[0][0].text)))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 0x6)

	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 6)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), hex(int(a,16)))

	a = '0x1'
	# writeReg(2, a)
	# print("Cat")
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), int(root[0][0].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 6)
	############## print(root[0][0][0].text)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), a)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), root[0][0][0].text)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), root[1][0].text)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 1)

# ePortTX_writeReg()
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), int(root[0][0].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), int(root[0][0].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX1DATARATE"), int(root[1][0].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX2DATARATE"), int(root[2][0].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX3DATARATE"), int(root[3][0].text))
	# # writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0DATARATE"), 1)

	# #mirror enable for every group 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX0MIRRORENABLE"), int(root[0][1].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX1MIRRORENABLE"), int(root[1][1].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX2MIRRORENABLE"), int(root[2][1].text))
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX3MIRRORENABLE"), int(root[3][1].text))

	# # #group 0 channel enable
	# #writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00ENABLE"), 0x1) #channel 0 in group 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00ENABLE"), int(root[0][2][0].text)) #channel 0 in group 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX01ENABLE"), int(root[0][3][0].text)) #channel 1 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX02ENABLE"), int(root[0][4][0].text)) #channel 2 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX03ENABLE"), int(root[0][5][0].text)) #channel 3 in group 0

	# #group 1 channel enable 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX10ENABLE"), int(root[1][2][0].text)) #channel 0 in group 1 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX11ENABLE"), int(root[1][3][0].text)) #channel 1 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12ENABLE"), int(root[1][4][0].text)) #channel 2 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX13ENABLE"), int(root[1][5][0].text)) #channel 3 in group 1

	# #group 2 channel enable 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX20ENABLE"), int(root[2][2][0].text)) #channel 0 in group 2 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX21ENABLE"), int(root[2][3][0].text)) #channel 1 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX22ENABLE"), int(root[2][4][0].text)) #channel 2 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX23ENABLE"), int(root[2][5][0].text)) #channel 3 in group 2

	# #group 3 channel enable 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX30ENABLE"), int(root[3][2][0].text)) #channel 0 in group 3 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX31ENABLE"), int(root[3][3][0].text)) #channel 1 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX32ENABLE"), int(root[3][4][0].text)) #channel 2 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX33ENABLE"), int(root[3][5][0].text)) #channel 3 in group 3


	# #group 0 channel invert
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00INVERT"), int(root[0][2][1].text)) #channel 0 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX01INVERT"), int(root[0][3][1].text)) #channel 1 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX02INVERT"), int(root[0][4][1].text)) #channel 2 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX03INVERT"), int(root[0][5][1].text)) #channel 3 in group 0

	# #group 1 channel invert
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX10INVERT"), int(root[1][2][1].text)) #channel 0 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX11INVERT"), int(root[1][3][1].text)) #channel 1 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12INVERT"), int(root[1][4][1].text)) #channel 2 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX13INVERT"), int(root[1][5][1].text)) #channel 3 in group 1

	# #group 2 channel invert
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX20INVERT"), int(root[2][2][1].text)) #channel 0 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX21INVERT"), int(root[2][3][1].text)) #channel 1 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX22INVERT"), int(root[2][4][1].text)) #channel 2 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX23INVERT"), int(root[2][5][1].text)) #channel 3 in group 2

	# #group 3 channel invert
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX30INVERT"), int(root[3][2][1].text)) #channel 0 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX31INVERT"), int(root[3][3][1].text)) #channel 1 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX32INVERT"), int(root[3][4][1].text)) #channel 2 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX33INVERT"), int(root[3][5][1].text)) #channel 3 in group 3

	# #group 0 PE width 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX00PREEMPHASISWIDTH"), int(root[0][2][2].text)) #channel 0 in group 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX01PREEMPHASISWIDTH"), int(root[0][3][2].text)) #channel 1 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX02PREEMPHASISWIDTH"), int(root[0][4][2].text)) #channel 2 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX03PREEMPHASISWIDTH"), int(root[0][5][2].text)) #channel 3 in group 0

	# #group 1 PE width 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX10PREEMPHASISWIDTH"), int(root[1][2][2].text)) #channel 0 in group 1 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX11PREEMPHASISWIDTH"), int(root[1][3][2].text)) #channel 1 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX12PREEMPHASISWIDTH"), int(root[1][4][2].text)) #channel 2 in group 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX13PREEMPHASISWIDTH"), int(root[1][5][2].text)) #channel 3 in group 1

	# #group 2 PE width 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX20PREEMPHASISWIDTH"), int(root[2][2][2].text)) #channel 0 in group 2 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX21PREEMPHASISWIDTH"), int(root[2][3][2].text)) #channel 1 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX22PREEMPHASISWIDTH"), int(root[2][4][2].text)) #channel 2 in group 2
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX23PREEMPHASISWIDTH"), int(root[2][5][2].text)) #channel 3 in group 2

	# #group 3 PE width 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX30PREEMPHASISWIDTH"), int(root[3][2][2].text)) #channel 0 in group 3 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX31PREEMPHASISWIDTH"), int(root[3][3][2].text)) #channel 1 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX32PREEMPHASISWIDTH"), int(root[3][4][2].text)) #channel 2 in group 3
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX33PREEMPHASISWIDTH"), int(root[3][5][2].text)) #channel 3 in group 3

	#group 0 PE strength  (????????????????????? QUESTIONS HERE ???????????????????????)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX${TX_CHN_IDX}PREEMPHASISSTRENGTH"), int(root[0][2][3].text)) #channel 0 in group 0
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX0PREEMPHASISSTRENGTH"), int(root[0][2][3].text))	#Channel 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX1PREEMPHASISSTRENGTH"), int(root[0][3][3].text))	#channel 1 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX2PREEMPHASISSTRENGTH"), int(root[0][4][3].text))	#channel 2 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX3PREEMPHASISSTRENGTH"), int(root[0][5][3].text))   #channel 3 

	#group 0 Drive Strength   (?????????????????????????? QUESTIONS HERE ???????????????????)
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX01DRIVESTRENGTH"), int(root[0][2][4].text))	#Channel 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX1DRIVESTRENGTH"), int(root[0][3][4].text))	#channel 1 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX2DRIVESTRENGTH"), int(root[0][4][4].text))	#channel 2 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX3DRIVESTRENGTH"), int(root[0][5][4].text)) #channel 3 

	#group 0 PE mode   (?????????????????????? QUESTIONS HERE ????????????????????? )
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTXCHNCONT.EPTX_0_2PEMODE"), int(root[0][2][5].text))	#Channel 0 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX1PREEMPHASISMODE"), int(root[0][3][5].text))	#Channel 1
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX2PREEMPHASISMODE"), int(root[0][4][5].text))	#Channel 2 
	# writeReg(getNode("LPGBT.RWF.EPORTTX.EPTX_CHN_CONTROL.EPTX3PREEMPHASISMODE"), int(root[0][5][5].text))	#Channel 3 


	# writeReg(getNode("LPGBT.RWF.CALIBRATION.FAMAXHEADERFOUNDCOUNTAFTERNF"), 0xA)
	# writeReg(getNode("LPGBT.RWF.CALIBRATION.FAMAXHEADERFOUNDCOUNTAFTERNF"), 10)
	# print(int('0xA', 16))