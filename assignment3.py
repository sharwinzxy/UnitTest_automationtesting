import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
#html report generated from libary root(unitTest file must saved to c:/venv)
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
                    executable_path="/Users/CACC/downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_register(self):
        self.driver.get("http://demo.automationtesting.in/Register.html")
        self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("xinyang")
        self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("zheng")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]").send_keys(
            "32 Denver Cres. Toronto")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys(
            "sharwinzxy@gmail.com")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("6476768277")
        self.driver.find_element_by_xpath("//label[1]//input[1]").click()
        self.driver.find_element_by_xpath("//input[@id='checkbox2']").click()
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'English')]").click()
        element1 = self.driver.find_element_by_xpath("//select[@id='Skills']")
        drp = Select(element1)
        drp.select_by_visible_text("Python")

        element2 = self.driver.find_element_by_xpath("//select[@id='countries']")
        drp1 = Select(element2)
        drp1.select_by_visible_text("China")

        element4 = self.driver.find_element_by_xpath("//select[@id='yearbox']")
        drp3 = Select(element4)
        drp3.select_by_visible_text("1969")

        element5 = self.driver.find_element_by_xpath("//select[@placeholder='Month']")
        drp4 = Select(element5)
        drp4.select_by_visible_text("April")

        element6 = self.driver.find_element_by_xpath("//select[@id='daybox']")
        drp5 = Select(element6)
        drp5.select_by_visible_text("7")

        self.driver.find_element_by_xpath("//input[@id='firstpassword']").send_keys("yanG2019")
        self.driver.find_element_by_xpath("//input[@id='secondpassword']").send_keys("yanG2019")

        self.driver.find_element_by_xpath("//button[@id='submitbtn']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath(" //a[contains(text(),'Practice Site')]").click()
        time.sleep(5)

        self.driver.find_element_by_xpath(
            "//li[contains(@class,'post-163 product type-product status-publish has-post-thumbnail product_cat-html product_tag-html has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author first instock sale downloadable taxable shipping-taxable purchasable product-type-simple')]//a[contains(@class,'button product_type_simple add_to_cart_button ajax_add_to_cart')][contains(text(),'Add to basket')]").click()
        self.driver.find_element_by_xpath("//a[contains(@class,'added_to_cart wc-forward')]").click()
        self.driver.find_element_by_xpath("//a[contains(@class,'checkout-button button alt wc-forward')]").click()


    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == '__main__':
   unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/CACC/Desktop/htmlreport"),verbosity = 2)

