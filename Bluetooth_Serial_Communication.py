# This program sends a flag to a bluetooth module so that it starts
# recoding a video

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM") #select port to connect to 

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))

    #flag = input("send flag to openMV: ")
    #serialInst.write(flag.encode('utf-8'))
    #if flag == 'exit':
     #   exit()
    #if flag == '1':
     #   serialInst.write(flag.encode('utf-8'))
      #  flag = 0



