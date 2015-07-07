import unittest

from CarrollPiProject.Website import Website as site


class TestMethods(unittest.TestCase):
    def test_init_function(self):
        try:
            website = site("Test", "Username", "Password")
            print("Logged in successfully")
        except:
            print("Login failed: future problem no login yet")

    def test_send_data_to_website(self):
        website = site("Test", "ncscienceresearch", "nch12345")
        response = website.send_data_to_website('0','0','0')
        if response != True:
            print("Error: " + str(response))
        else:
            print("Test Successful!")

if __name__ == '__main__':
    unittest.main()
