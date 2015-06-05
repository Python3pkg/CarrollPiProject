def turnOnLED(ser):
    """Turns on the LED for debugging

    Args: \n
    :param ser: the serial object \n
    :type ser: str \n
    """
    ser.write("L,1<CR>")


def passTemperature(ser, temp):
    """Passes the temperature to the DO sensor for a more accurate reading

    Args: \n
    :param ser: the serial object \n
    :type ser: str \n
    :param temp: the temperature in Celsius \n
    :type temp: str \n
    """
    ser.write("T," + str(temp) + "<CR>")


def requestData(ser):
    """Sends a request for Dissolved Oxygen data

    Args: \n
    :param ser: the serial object \n
    :type ser: str \n
    """
    ser.write("C")