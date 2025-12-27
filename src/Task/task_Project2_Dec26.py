'''
https://www.idrive360.com/enterprise/account?upgradenow=true
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_idrive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    email_tab = driver.find_element(By.ID,"username")
    email_tab.send_keys("augtest_040823@idrive.com")
    pass_tab = driver.find_element(By.ID,"password")
    pass_tab.send_keys("123456")
    sign_in_button = driver.find_element(By.ID,"frm-btn")
    sign_in_button.click()
    time.sleep(20)

    error_message = driver.find_element(By.CLASS_NAME,"id-warning-btn-drk id-tkn-btn")
    print(error_message.text)
    assert "Upgrade Now!" == error_message.text
    driver.quit()

