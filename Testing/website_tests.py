import unittest

from CarrollPiProject.Website import Website as site


class TestMethods(unittest.TestCase):

    def test_init_function(self):
        try:
            website = site("Location", "Username", "Password")
            print("Logged in successfully")
        except:
            print("Login failed: future problem no login yet")

    def test_send_data_to_website(self):
        pass


if __name__ == '__main__':
    unittest.main()
