from time import sleep
from Locator import Locators
from Locator import Basepage

    
def Register_new_user(object1):
    driver = object1
    driver.find_element_by_xpath(Locators.Register).click()
    sleep(5)
    driver.find_element_by_name(Locators.firstname).send_keys("keerthi")
    driver.find_element_by_name(Locators.lastname).send_keys("NK")
    driver.find_element_by_name(Locators.phone).send_keys("1234567890")
    driver.find_element_by_name(Locators.email).send_keys("keerthi@gmail.com")
    sleep(3)
    driver.find_element_by_name(Locators.address).send_keys("nagarbhavi")
    driver.find_element_by_name(Locators.city).send_keys("Bangalore")
    driver.find_element_by_name(Locators.state).send_keys("Karnataka")
    driver.find_element_by_name(Locators.pin).send_keys("566566")
    sleep(3)
    Basepage.selectbytext(driver.find_element_by_name(Locators.selectcountry), "INDIA ")
    driver.find_element_by_name(Locators.username).send_keys("admin1")
    driver.find_element_by_name(Locators.pwd).send_keys("admin1")
    driver.find_element_by_name(Locators.confirmpwd).send_keys("admin1")
    sleep(2)
    driver.find_element_by_name(Locators.submitregister).click()
