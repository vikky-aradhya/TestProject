from time import sleep
import unittest
from Scripts import Register
from Scripts import Login
from Locator import Basepage


class Registeruser(unittest.TestCase):
    @classmethod
    def setUpClass(cls,browsertorun):
        cls.driver=Basepage.Browser("chrome","http://newtours.demoaut.com/")

    def test_1_Register(self):
        Register.Register_new_user(self.driver)
        sleep(5)
    
    def test_2_Login(self):
        Login.Login_user(self.driver)
        sleep(5)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        

if __name__ == "__main__":
    unittest.main()