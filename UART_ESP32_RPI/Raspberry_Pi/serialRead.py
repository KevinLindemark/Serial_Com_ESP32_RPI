import time
import serial
import datetime

# Remember to disable login shell and enable serial hardware:
"""sudo raspi-config

From the menu select interfacing options > serial
and when you are asked whether you would like the login shell
to be available over serial, select no. You will then be asked whether
you would like the serial hardware to be enabled, select yes."""

ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

while 1:
    y=datetime.datetime.now()
    x=ser.readline().strip()
    if x  != b'':
        print(x," datetime is: ",y)