#!/usr/bin/python3
import serial


def concentration(message, index1, index2):
    a = int(message[index1], 16)
    a = a * 256
    b = int(message[index2], 16)
    return a + b


with serial.Serial("/dev/ttyACM0", 9600, timeout=50) as ser:
    message = list(range(28))
    while True:
        read_byte = hex(ser.read()[0])
        message.append(read_byte)
        message.pop(0)
        if message[0] == '0x42' and message[1] == '0x4d':
            pm1_0_standard = concentration(message, 4, 5)
            pm2_5_standard = concentration(message, 6, 7)
            pm10_standard = concentration(message, 8, 9)
            pm1_0_atmospheric = concentration(message, 10, 11)
            pm2_5_atmospheric = concentration(message, 12, 13)
            concentration_unit_atmospheric = concentration(message, 14, 15)
            print(pm1_0_standard," ", pm2_5_standard," ", pm10_standard, " ", pm1_0_atmospheric, " ", pm2_5_atmospheric, " ", concentration_unit_atmospheric, "μg/m3")
