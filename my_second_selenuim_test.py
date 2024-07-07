from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Open Google site
driver.get('https://demo.applitools.com/')
driver.maximize_window()
time.sleep(5)


# First Check title
titleName = "ACME Demo App by Applitools"
try:
    assert driver.title == titleName
    correctPage = True
except AssertionError:
    correctPage = False
    
if correctPage == True:
    u = driver.find_element(By.ID,'username')
    u.send_keys('admin')
    p = driver.find_element(By.ID,'password')
    p.send_keys('admin')
    rm = driver.find_element(By.XPATH,'/html/body/div/div/form/div[3]/div[1]/label/input')
    rm.click()
    login = driver.find_element(By.ID,'log-in')
    login.click()
else: 
    with open('rundev.log',"w") as f:
        f.write(f"Not the correct title {driver.title}")
    
time.sleep(5)

driver.close()