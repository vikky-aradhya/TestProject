from selenium.webdriver.support.select import Select
from time import sleep
from selenium import webdriver
import os

#Select by Visiable text
def selectbytext(path,text):
    select = Select(path)
    select.select_by_visible_text(text)
    sleep(2)
 
#Browser

def Browser(BrowserName,url):
    dir1 = os.path.dirname(__file__)
    edge_path = dir1 + "\MicrosoftWebDriver.exe"
    if(BrowserName=="firefox"):
        driver= webdriver.Firefox("geckodriver.exe")
    elif(BrowserName=="chrome"):
        driver=webdriver.Chrome()
    elif(BrowserName=="ie"):
        driver=webdriver.Edge(edge_path)
    driver.maximize_window()
    driver.get(url)
    return driver
        
        
    