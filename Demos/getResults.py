#!/user/bin/python
# -*- coding: utf-8 -*-

import serial
import time

import Temperature
import DissolvedOxygen
import Website

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
