#!/user/bin/python
# -*- coding: utf-8 -*-

import serial
import time

from CarrollPiProject import Website, DissolvedOxygen, Temperature

tempSensor = Temperature.getSensor()

ser = serial.Serial('/dev/ttyAMA0', 38400)

DissolvedOxygen.turnOnLED(ser)

Temperature.prepSystemForTemp()

while True:
    DissolvedOxygen.passTemperature(ser, Temperature.read_temp_Celsius(tempSensor))
    DissolvedOxygen.requestData(ser)

    line = ""

    while True:
        data = ser.read()
        if (data == '\r'):
            Website.sendDataToWebsite(Temperature.read_temp_Celsius(tempSensor),
                                      Temperature.read_temp_Fahrenheit(tempSensor), line, "North Carroll",
                                      "username", "password")

            line = ""
            break
        else:
            line = line + data

    time.sleep(3600 * 6)
