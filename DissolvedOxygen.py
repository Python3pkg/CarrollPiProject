class dissolved_oxygen:
    ser = ""

    def __init__(self, ser):
        self.ser = ser

    def turnOnLED(self):
        """Turns on the LED for debugging

        Args: \n
        :param ser: the serial object \n
        :type ser: str \n
        """
        self.ser.write("L,1<CR>")

    def passTemperature(self, temp):
        """Passes the temperature to the DO sensor for a more accurate reading

        Args: \n
        :param ser: the serial object \n
        :type ser: str \n
        :param temp: the temperature in Celsius \n
        :type temp: str \n
        """
        self.ser.write("T," + str(temp) + "<CR>")

    def requestData(self):
        """Sends a request for Dissolved Oxygen data

        Args: \n
        :param ser: the serial object \n
        :type ser: str \n
        """
        self.ser.write("C")
