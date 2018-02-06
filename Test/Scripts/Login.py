from time import sleep
from Locator import Locators

    
def Login_user(object1):
    driver = object1
    driver.find_element_by_xpath(Locators.signin).click()
    sleep(5)
    driver.find_element_by_name(Locators.loginusername).send_keys("admin1")
    driver.find_element_by_name(Locators.loginpwd).send_keys("admin1")
    sleep(3)
    driver.find_element_by_name(Locators.loginsubmit).click()
    
