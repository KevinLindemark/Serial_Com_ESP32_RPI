from machine import UART
from time import sleep
from random import randint
uart = UART(1, 115200) # 1st argument: UART number: Hardware UART #1

# Read
#print(uart.read()) # Read as much as possible using

while True:
    randiddy = randint(0, 99)
    print(f"hello random number is: {str(randiddy)}")
    # Write
    uart.write(f"hello random number is: {str(randiddy)}")
    sleep(1)