'''
Mini Project #1 (Selenium)
// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter password as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_
'''

import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_app_vwo():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_add_tab = driver.find_element(By.NAME,"username")
    email_add_tab.send_keys("admin@admin.com")
    pass_tab =driver.find_element(By.NAME,"password")
    pass_tab.send_keys("admin")
    sign_in_button = driver.find_element(By.ID,"js-login-btn")
    sign_in_button.click()

    time.sleep(5)

    error_message = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_message.text)
    assert "Your email, password, IP address or location did not match" == error_message.text


