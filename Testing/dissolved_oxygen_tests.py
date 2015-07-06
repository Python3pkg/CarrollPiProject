import unittest

from CarrollPiProject.DissolvedOxygen import dissolved_oxygen as do


class TestMethods(unittest.TestCase):

    def test_init_function(self):
        try:
            do_sensor = do()
        except:
            print("Dissolved Oxygen sensor not found")

    def test_turn_on_lights(self):
        pass

    def test_pass_temperature(self):
        pass

    def test_get_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
