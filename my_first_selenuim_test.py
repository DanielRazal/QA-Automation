from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google Site
driver.get('https://demo.guru99.com/test/newtours/#google_vignette')
driver.maximize_window()
g = driver.find_element(By.NAME,'userName')
x = driver.find_element(By.NAME,'password')
g.send_keys('admin')
x.send_keys('admin')
g.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()