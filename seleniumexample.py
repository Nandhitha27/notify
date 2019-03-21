import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
import time
 
driver = webdriver.Chrome()
driver.get('https://www.facebook.com')

driver.execute_script("window.open('');")
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")
time.sleep(3)

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[2])
driver.get("http://gmail.com")
time.sleep(3)


