import os
import time
import glob


def prepSystemForTemp():
    """Sends commands to system to ready the probe"""
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')


def getSensor():
    """Returns the folder the temperature is stored in"""
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    return device_folder + '/w1_slave'


def read_temp_raw(tempSensorFolder):
    """Returns the raw temperature, not in human readable form

    Args: \n
    :param tempSensorFolder: the folder where the temperature sensor is stored \n
    :type tempSensorFolder: str \n
    """
    f = open(tempSensorFolder, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp_Celsius(tempSensorFolder):
    """Returns the temperature in celsius

    Args: \n
    :param tempSensorFolder: the folder where the temperature sensor is stored \n
    :type tempSensorFolder: str \n
    """
    lines = read_temp_raw(tempSensorFolder)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(tempSensorFolder)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        return float(temp_string) / 1000.0


def read_temp_Fahrenheit(tempSensorFolder):
    """Returns the temperature in fahrenheit

    Args: \n
    :param tempSensorFolder: the folder where the temperature sensor is stored \n
    :type tempSensorFolder: str \n
    """
    temp_f = read_temp_Celsius(tempSensorFolder) * 9.0 / 5.0 + 32.0
    return str(temp_f)