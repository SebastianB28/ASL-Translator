import serial
import keyboard
from serial.serialutil import Timeout
import serial.tools.list_ports

portsList = serial.tools.list_ports.comports()
connectedPorts = []

for element in portsList:
    connectedPorts.append(element.device)

print("Connected COM ports: " + str(connectedPorts))

serialBus = serial.Serial(
    port="com3",
    baudrate=9600,
)

while not keyboard.is_pressed('q'):
    if serialBus.in_waiting:
        data = serialBus.readline()
        data = data.decode('utf').strip()
        data = data.split(',')
        print(len(data))



serialBus.close()