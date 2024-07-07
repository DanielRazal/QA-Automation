from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Open Google site
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
time.sleep(3)

# First Check title
titleName = "DEMOQA"

try:
    assert driver.title == titleName
    correctPage = True
except AssertionError:
    correctPage = False
    
if correctPage == True:
    userName = driver.find_element(By.ID,'userName')
    # userName.clear()
    userName.send_keys('Daniel')
    email = driver.find_element(By.ID,'userEmail')
    # email.clear()
    email.send_keys('mr.danielrazal@gmail.com')
    currentAddress = driver.find_element(By.ID,'currentAddress')
    # currentAddress.clear()
    currentAddress.send_keys('blabla')
    permanentAddress = driver.find_element(By.ID,'permanentAddress')
    # permanentAddress.clear()
    permanentAddress.send_keys('blabla')
    login = driver.find_element(By.ID,'submit')
    login.click()
else: 
    with open('rundev.log',"w") as f:
        f.write(f"Not the correct title {driver.title}")
        
        
    
time.sleep(3)

driver.close()