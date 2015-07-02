#!/user/bin/python
# -*- coding: utf-8 -*-

from CarrollPiProject import Temperature as temp
from CarrollPiProject.DissolvedOxygen import dissolved_oxygen

tempSensor = temp()
do_sensor = dissolved_oxygen()

do_sensor.turnOnLED()

while True:
    do_sensor.pass_temperature(tempSensor.read_temp_celsius())

    print(tempSensor.read_temp_celsius(), tempSensor.read_temp_fahrenheit(), dissolved_oxygen.get_data(), "North Carroll")
