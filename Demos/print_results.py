#!/user/bin/python
# -*- coding: utf-8 -*-

from CarrollPiProject.Temperature import Temperature as temp
from CarrollPiProject.DissolvedOxygen import dissolved_oxygen


def test():
    tempSensor = temp()
    do_sensor = dissolved_oxygen()

    do_sensor.turn_on_lights()

    while True:
        do_sensor.pass_temperature(tempSensor.read_temp_celsius())

        print(tempSensor.read_temp_celsius(), tempSensor.read_temp_fahrenheit(), do_sensor.get_data(), "North Carroll")
