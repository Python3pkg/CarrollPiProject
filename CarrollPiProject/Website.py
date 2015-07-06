import requests


class Website:
    school = ""
    username = ""
    password = ""

    def __init__(self, school, username, password):
        """
        Args: \n
        :param school: the location of the device \n
        :type school: str \n
        :param username: CarrollPiProject Username. \n
        :type username: str \n
        :param password: CarrollPiProject Password. \n
        :type password: str \n
        """

        self.school = school
        self.username = username
        self.password = password

    def send_data_to_website(self, celsius, fahrenheit, dissolvedOxygen):
        """Sends Dissoloved oxygen and Temperature data to the website API

        Args: \n
        :param celsius: the temperature in celsius \n
        :type celsius: str \n
        :param fahrenheit: the temperature in fahrenheit \n
        :type fahrenheit: str \n
        :param dissolvedOxygen: the dissolved oxygen \n
        :type dissolvedOxygen: str \n
        """
        body = {'celsius': celsius,
                'fahrenheit': fahrenheit,
                'dissolvedOxygen': dissolvedOxygen,
                'school': self.school,
                'username': self.username,
                'password': self.password}
        requests.post("http://www.carrollpiproject.com/dataApi", data=body)
