import keyboard
import serial
import time
import os

from serial.serialutil import Timeout

capturedLetter = input("Enter the letter you wish to capture: ")

parent_dir = "letterDirectory/rawData/"

path = os.path.join(parent_dir,capturedLetter)

lastTime = time.time()
currentTime = None
elapsedTime = None

try:
    os.mkdir(path)
except:
    print("Unable to create folder (ALREADY EXISTS)")
else:
    print("Folder successfully created")

file_count = len(os.listdir(path)) + 1

serialBus = serial.Serial(
    port="com6",
    baudrate=9600,
    timeout=1
)

while not keyboard.is_pressed('q'):
    currentTime = time.time()
    elapsedTime = currentTime - lastTime

    data = serialBus.readline()

    if  elapsedTime > 0.3:
        if keyboard.is_pressed('r'):
            filename = path + "/" + capturedLetter + str(file_count) + ".txt"
            print(filename)
            #time.sleep(.01)

            file_count = file_count + 1
            output = data.decode('utf').strip()
            print(output)

            packet = open(filename, "w+")
            packet.write(output)
            packet.close()

            lastTime = currentTime

    print(data)



serialBus.close()