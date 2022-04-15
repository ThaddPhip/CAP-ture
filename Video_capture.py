# Video Capture - By: isaias - Sat Mar 5 2022
# USE THIS WITH A USD CARD. Reset the camera after recording to see the file.
#
#

import sensor, image, pyb, time, machine, random
from pyb import UART

uart = UART(3, 115200, timeout_char=1000)

boolean = 0

fileName = "/Memory"
vidNum = 0
record_time = 120000 # 5 seconds in milliseconds (2min)

while 1:
    pyb.LED(3).off()
    boolean = uart.read() #reads from terminal

    if boolean: #when user enters 1 in terminal, begin recording for 10 seconds
        uart.write('Program Started.\n\r')
        sensor.reset()
        sensor.set_pixformat(sensor.RGB565)
        sensor.set_framesize(sensor.QVGA)
        sensor.skip_frames(time = 2000)
        clock = time.clock()

        #video file name updated
        fileName = fileName + str(vidNum) + ".bin"
        stream = image.ImageIO(fileName, "w")

        # Red LED on means we are capturing frames.
        pyb.LED(1).on()

        start = pyb.millis()
        while pyb.elapsed_millis(start) < record_time:
            clock.tick()
            img = sensor.snapshot()
            # Modify the image here...
            stream.write(img)
            print(clock.fps())

        stream.close()
        # Blue LED on means we are done.
        pyb.LED(1).off()
        pyb.LED(3).on()

        message = fileName + ' recorded as a file onto the SD card\n\r'
        #uart.write(message)

        vidNum = vidNum + 1
        fileName = "/Memory" # reseting the name
        uart.write('\n\r')
    Boolean = 0 #reseting the flag to wait for another response from app

    #if vidNum == 1:
    #    break
#uart.write('\n\r')

#machine.reset()

#Convert file from .bin to readable .mp4 file and transfer it back to terminal to be downloaded
#We're unsure if this can be done via UART. If not, what other ways make this possible?
