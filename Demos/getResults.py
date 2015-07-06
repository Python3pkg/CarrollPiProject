#!/user/bin/python
# -*- coding: utf-8 -*-

from CarrollPiProject.Temperature import Temperature as temp
from CarrollPiProject.DissolvedOxygen import dissolved_oxygen
from CarrollPiProject.Website import Website

tempSensor = temp()
do_sensor = dissolved_oxygen()
website = Website("North Carroll", "username", "password")

do_sensor.turn_on_lights()

while True:
    do_sensor.pass_temperature(tempSensor.read_temp_celsius())

    website.send_data_to_website(tempSensor.read_temp_celsius(), tempSensor.read_temp_fahrenheit(),
                              do_sensor.get_data())
