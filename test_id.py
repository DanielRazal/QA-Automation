from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

"""
driver.get('https://demo.applitools.com/')
time.sleep(3)

driver.maximize_window()
un = driver.find_element(By.ID,'username')
un.send_keys('admin')
ps = driver.find_element(By.ID,'password')
ps.send_keys('admin')

rm = driver.find_element(By.XPATH,'/html/body/div/div/form/div[3]/div[1]/label/input')
rm.click()

login = driver.find_element(By.ID,'log-in')
login.click()

login_name = driver.find_element(By.CLASS_NAME,'logged-user-name')
print(login_name.text)

time.sleep(5)
driver.close()


driver.get('https://toolsqa.com/selenium-webdriver/selenium-checkbox/')
driver.maximize_window()
time.sleep(3)

# link = driver.find_element(By.LINK_TEXT,'How to Run Your First Selenium Test Script')
part_link = driver.find_element(By.PARTIAL_LINK_TEXT,'Architecture')
part_link.click()
time.sleep(10)
driver.close()
"""

# like try catch

x = 'Jack Gomez'

assert(x == 'Jack Gomez')