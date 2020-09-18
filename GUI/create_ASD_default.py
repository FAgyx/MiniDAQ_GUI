import xml.etree.ElementTree as ET
from xml.dom import minidom

def generateXML(fileName):
	configuration = ET.Element('configuration')

	#ASD0 
	ASD0 = ET.SubElement(configuration, 'ASD0')


	#channel modes 
	channel_0_mode = ET.SubElement(ASD0, 'channel_0_mode')
	channel_0_mode.text = '00'
	channel_1_mode = ET.SubElement(ASD0, 'channel_1_mode')
	channel_1_mode.text = '00'
	channel_2_mode = ET.SubElement(ASD0, 'channel_2_mode')
	channel_2_mode.text = '00'
	channel_3_mode = ET.SubElement(ASD0, 'channel_3_mode')
	channel_3_mode.text = '00'
	channel_4_mode = ET.SubElement(ASD0, 'channel_4_mode')
	channel_4_mode.text = '00'
	channel_5_mode = ET.SubElement(ASD0, 'channel_5_mode')
	channel_5_mode.text = '00'
	channel_6_mode = ET.SubElement(ASD0, 'channel_6_mode')
	channel_6_mode.text = '00'
	channel_7_mode = ET.SubElement(ASD0, 'channel_7_mode')
	channel_7_mode.text = '00'

	#chip mode
	chip_mode = ET.SubElement(ASD0, 'chip_mode')
	chip_mode.text = '0'

	#deadtime 
	deadtime = ET.SubElement(ASD0, 'deadtime')
	deadtime.text = '111'

	#int_gate 
	int_gate = ET.SubElement(ASD0, 'int_gate')
	int_gate.text = '0100'

	#rundown_curr 
	rundown_curr = ET.SubElement(ASD0, 'rundown_curr')
	rundown_curr.text = '010'

	#hyst 
	hyst = ET.SubElement(ASD0, 'hyst')
	hyst.text = '1110'

	#wilk_thr
	wilk_thr = ET.SubElement(ASD0, 'wilk_thr')
	wilk_thr.text = '010'

	#main_thr 
	main_thr = ET.SubElement(ASD0, 'main_thr')
	main_thr.text = '01100110'

	#ASD1 
	ASD1 = ET.SubElement(configuration, 'ASD1')

	#channel modes 
	channel_0_mode = ET.SubElement(ASD1, 'channel_0_mode')
	channel_0_mode.text = '00'
	channel_1_mode = ET.SubElement(ASD1, 'channel_1_mode')
	channel_1_mode.text = '00'
	channel_2_mode = ET.SubElement(ASD1, 'channel_2_mode')
	channel_2_mode.text = '00'
	channel_3_mode = ET.SubElement(ASD1, 'channel_3_mode')
	channel_3_mode.text = '00'
	channel_4_mode = ET.SubElement(ASD1, 'channel_4_mode')
	channel_4_mode.text = '00'
	channel_5_mode = ET.SubElement(ASD1, 'channel_5_mode')
	channel_5_mode.text = '00'
	channel_6_mode = ET.SubElement(ASD1, 'channel_6_mode')
	channel_6_mode.text = '00'
	channel_7_mode = ET.SubElement(ASD1, 'channel_7_mode')
	channel_7_mode.text = '00'

	#chip mode
	chip_mode = ET.SubElement(ASD1, 'chip_mode')
	chip_mode.text = '0'

	#deadtime 
	deadtime = ET.SubElement(ASD1, 'deadtime')
	deadtime.text = '111'

	#int_gate 
	int_gate = ET.SubElement(ASD1, 'int_gate')
	int_gate.text = '0100'

	#rundown_curr 
	rundown_curr = ET.SubElement(ASD1, 'rundown_curr')
	rundown_curr.text = '010'

	#hyst 
	hyst = ET.SubElement(ASD1, 'hyst')
	hyst.text = '1110'

	#wilk_thr
	wilk_thr = ET.SubElement(ASD1, 'wilk_thr')
	wilk_thr.text = '010'

	#main_thr 
	main_thr = ET.SubElement(ASD1, 'main_thr')
	main_thr.text = '01100110'

	#ASD2 
	ASD2 = ET.SubElement(configuration, 'ASD2')

	#channel modes 
	channel_0_mode = ET.SubElement(ASD2, 'channel_0_mode')
	channel_0_mode.text = '00'
	channel_1_mode = ET.SubElement(ASD2, 'channel_1_mode')
	channel_1_mode.text = '00'
	channel_2_mode = ET.SubElement(ASD2, 'channel_2_mode')
	channel_2_mode.text = '00'
	channel_3_mode = ET.SubElement(ASD2, 'channel_3_mode')
	channel_3_mode.text = '00'
	channel_4_mode = ET.SubElement(ASD2, 'channel_4_mode')
	channel_4_mode.text = '00'
	channel_5_mode = ET.SubElement(ASD2, 'channel_5_mode')
	channel_5_mode.text = '00'
	channel_6_mode = ET.SubElement(ASD2, 'channel_6_mode')
	channel_6_mode.text = '00'
	channel_7_mode = ET.SubElement(ASD2, 'channel_7_mode')
	channel_7_mode.text = '00'

	#chip mode
	chip_mode = ET.SubElement(ASD2, 'chip_mode')
	chip_mode.text = '0'

	#deadtime 
	deadtime = ET.SubElement(ASD2, 'deadtime')
	deadtime.text = '111'

	#int_gate 
	int_gate = ET.SubElement(ASD2, 'int_gate')
	int_gate.text = '0100'

	#rundown_curr 
	rundown_curr = ET.SubElement(ASD2, 'rundown_curr')
	rundown_curr.text = '010'

	#hyst 
	hyst = ET.SubElement(ASD2, 'hyst')
	hyst.text = '1110'

	#wilk_thr
	wilk_thr = ET.SubElement(ASD2, 'wilk_thr')
	wilk_thr.text = '010'

	#main_thr 
	main_thr = ET.SubElement(ASD2, 'main_thr')
	main_thr.text = '01100110'


		#create a new XML file with correct indentations
	xmlstr = minidom.parseString(ET.tostring(configuration)).toprettyxml(indent="	")
	with open(fileName, "w") as f:
		f.write(xmlstr)

if __name__ == "__main__":
	generateXML("ASD_default.xml")