import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
from POMTest_Demo.AddtoCart import addtocart1
from POMTest_Demo.Register import Register

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/CACC/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Register(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in")

        reg = Register(driver)
        reg.enter_email("zxymilsy@gmail.com")
        reg.enter_details1("Xinyang", "Zheng", "32 Denver Cres", "zxymilsy@gmail.com", "6476768277")
        reg.enter_details2("Python", "China", "1969", "April", "7")
        reg.enter_password("yanG2019", "yanG2019")
        reg.submit()

        AddtoCart = addtocart1(driver)
        AddtoCart.Practice_site()
        AddtoCart.addtoCart()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/CACC/Desktop/htmlreport"),verbosity = 2)
