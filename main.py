from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 
import time


# def test_text_box(driver):
#     try:
#         userName = driver.find_element(By.ID,'userName')
#         userName.clear()
#         userName.send_keys('Daniel')
#         email = driver.find_element(By.ID,'userEmail')
#         email.clear()
#         email.send_keys('mr.danielrazal@gmail.com')
#         currentAddress = driver.find_element(By.ID,'currentAddress')
#         currentAddress.clear()
#         currentAddress.send_keys('blabla')
#         permanentAddress = driver.find_element(By.ID,'permanentAddress')
#         permanentAddress.clear()
#         permanentAddress.send_keys('blabla')
        
#         # submit
#         submit = driver.find_element(By.ID, "submit")
#         driver.execute_script("arguments[0].scrollIntoView(true);", submit)
#         submit.click()
        
#     except Exception as e:
#         print(e)


# def test_checkbox(driver):
#     home = driver.find_element(By.ID, "tree-node-home")
#     driver.execute_script("arguments[0].scrollIntoView(true);", home)
#     home.click()
    
# def test_radio(driver):
#     yesradio = driver.find_element(By.ID, "yesRadio")
#     driver.execute_script("arguments[0].scrollIntoView(true);", yesradio)
#     driver.execute_script("arguments[0].click();", yesradio)


def test_radio(driver):
    radio = driver.find_element(By.XPATH , '//*[@id="q26"]/table/tbody/tr[1]/td/label')
    radio.click()

def test_checkBox(driver):
    checkBox = driver.find_element(By.XPATH , '//*[@id="q15"]/table/tbody/tr[6]/td/label')
    checkBox.click()

def test_select_dropDown(driver):
    select = Select(driver.find_element(By.ID,'RESULT_RadioButton-9'))
    # select.select_by_visible_text("Evening")
    # select.select_by_value("Radio-0")
    select.select_by_index(2)
    
def test_user_details(driver):
    firstName = driver.find_element(By.ID , 'RESULT_TextField-1')
    firstName.clear()
    firstName.send_keys('Daniel')
    lastName = driver.find_element(By.ID , 'RESULT_TextField-2')
    lastName.clear()
    lastName.send_keys('Razal')
    phone = driver.find_element(By.ID , 'RESULT_TextField-3')
    phone.clear()
    phone.send_keys('0502242268')
    country = driver.find_element(By.ID , 'RESULT_TextField-4')
    country.clear()
    country.send_keys('Israel')
    city = driver.find_element(By.ID , 'RESULT_TextField-5')
    city.clear()
    city.send_keys('Or Yehuda')
    email = driver.find_element(By.ID , 'RESULT_TextField-6')
    email.clear()
    email.send_keys('mr.danielrazal@gmail.com')

def test_table(driver):
    table = driver.find_element(By.ID, 'table1')
    head = table.find_element(By.TAG_NAME, 'thead')
    headrow = head.find_element(By.TAG_NAME, 'tr')
    headrows = headrow.find_elements(By.TAG_NAME, 'th')
    
    for row in headrows:
        print(row.text)
        
    body = table.find_element(By.TAG_NAME, 'tbody')
    bodyrows = body.find_elements(By.TAG_NAME, 'tr')

    for row in bodyrows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            print(cell.text)

        
def test_table_two(driver):
    table = driver.find_element(By.ID, 'table2')
    thead = table.find_element(By.TAG_NAME, 'thead')
    tr = thead.find_element(By.TAG_NAME, 'tr')
    th = tr.find_elements(By.TAG_NAME, 'th')
    
    for t in th:
        print(t.text)
    
    body = table.find_element(By.TAG_NAME, 'tbody')
    trs = body.find_elements(By.TAG_NAME, 'tr')
    
    for tr in trs:
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for td in tds:
            print(td.text)
    
    
    
    
    
    
    
    
    
    
    
    # table = driver.find_element(By.ID, 'table2')
    # head = table.find_element(By.TAG_NAME, 'thead')
    # headrow = head.find_element(By.TAG_NAME, 'tr')
    # headrows = headrow.find_elements(By.TAG_NAME, 'th')
    
    # for row in headrows:
    #     print(row.text)
        
    # body = table.find_element(By.TAG_NAME, 'tbody')
    # bodyrows = body.find_elements(By.TAG_NAME, 'tr')

    # for row in bodyrows:
    #     cells = row.find_elements(By.TAG_NAME, 'td')
    #     for cell in cells:
    #         print(cell.text)
    
    
if __name__ == '__main__':
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
    # driver.maximize_window()
    # # test_text_box(driver)
    # time.sleep(3)
    # test_user_details(driver)
    # test_radio(driver)
    # test_checkBox(driver)
    # test_select_dropDown(driver)
    time.sleep(3)
    
    driver.get('https://the-internet.herokuapp.com/tables')
    # test_table(driver)
    test_table_two(driver)
    time.sleep(3)

    # Second Test Check-Box
    # driver.get('https://demoqa.com/checkbox')
    # test_checkbox(driver)
         
    
    # Third Test RaddioButton
    # driver.get('https://demoqa.com/radio-button')
    # test_radio(driver)
    
    # time.sleep(5)
    # driver.close()

    
    # call test functions
    
    
    
    # driver.get('https://www.demoblaze.com/')
    
    # categories = driver.find_elements(By.ID,"itemc")
    # for category in categories:
    #     print(category.text)
