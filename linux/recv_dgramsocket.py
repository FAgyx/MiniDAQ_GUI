#!/usr/bin/env python
import socket
import binascii
import sys

from time import sleep
from target_info import *


UDP_IP = "192.168.0.16"
UDP_PORT = 6008

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_NO_CHECK,1)
sock.bind((UDP_IP,UDP_PORT))

dfile=open("test.dat","w");

#sock.settimeout(5)
while True:
	#receive response
	print >>sys.stderr, 'waiting for response'
	data, server = sock.recvfrom(4096)
	print >>sys.stderr, 'received:\n' + binascii.hexlify(data)
	dfile.write("---------\n")
	dfile.write(binascii.hexlify(data))
	dfile.write("\n")


#print >>sys.stderr, 'closing socket\n--=====================--\n'
#sock.close()




