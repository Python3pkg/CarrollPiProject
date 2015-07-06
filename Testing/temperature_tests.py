import unittest

from CarrollPiProject.Temperature import Temperature as temp


class TestMethods(unittest.TestCase):

    def test_init_function(self):
        try:
            temp_test = temp()
        except:
            print("Temperature sensor not found")

    def test_read_temp_raw(self):
        pass

    def test_read_temp_celsius(self):
        pass

    def test_read_temp_fahrenheit(self):
        pass


if __name__ == '__main__':
    unittest.main()
