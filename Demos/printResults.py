#!/user/bin/python
# -*- coding: utf-8 -*-

import serial

from Temperature import Temperature as temp
from DissolvedOxygen import dissolved_oxygen

tempSensor = temp()
ser = serial.Serial('/dev/ttyAMA0', 38400)
do_sensor = dissolved_oxygen(ser)

do_sensor.turnOnLED()

while True:
    do_sensor.passTemperature(tempSensor.read_temp_celsius())
    do_sensor.requestData()

    line = ""

    data = ser.read()
    while (data != '\r'):
        line = line + data
        data = ser.read()

    print(tempSensor.read_temp_celsius(), tempSensor.read_temp_fahrenheit(), line, "North Carroll")
