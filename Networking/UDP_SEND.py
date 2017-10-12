# G.Çetin, 12.10.2017
# modified from https://wiki.python.org/moin/UdpCommunication#UDP_Communication

import socket
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

for i in range(100):
    MESSAGE = str(math.sin(i*180/math.pi))
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

