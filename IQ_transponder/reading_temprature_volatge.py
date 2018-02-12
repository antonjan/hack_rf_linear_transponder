#!/usr/bin/python3

import smbus
import time

slope = 9.821148E-4      # constants used in mapping temperature
intercept = 7.064956E1

deltasig = [0x68,0x69,0x6a,0x06b,0x6c,0x6d,0x6e,0x6f]           # device addresses
config_byte = 0x1c          # continuous mode, 18-bit resolution, gain = 1.

bus = smbus.SMBus(1)
bus.write_byte(deltasig[0],config_byte) # configure the adc

while True:
    time.sleep(1)
    mcpdata = bus.read_i2c_block_data(deltasig[0],config_byte,4)
    conversionresults = mcpdata[2] + (mcpdata[1] << 8) + (mcpdata[0] << 16)

    conversionresults &= 0x1ffff     # lop off the sign ADC's sign extension
    if mcpdata[0] & 0x80:            # if the data was negative 
        conversionresults -= 0x20000     #     subtract off the sign extension bit

    temperature = conversionresults * slope + intercept
    print('Conversion results =',hex(conversionresults), 'config-byte:',hex(mcpdata[3]))
