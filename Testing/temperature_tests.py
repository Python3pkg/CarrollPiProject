import unittest

from CarrollPiProject.Temperature import Temperature as temp

temp_test = temp()


class TestStringMethods(unittest.TestCase):
    def test_read_temp_raw(self):
        pass

    def test_read_temp_celsius(self):
        pass

    def test_read_temp_fahrenheit(self):
        pass


if __name__ == '__main__':
    unittest.main()
