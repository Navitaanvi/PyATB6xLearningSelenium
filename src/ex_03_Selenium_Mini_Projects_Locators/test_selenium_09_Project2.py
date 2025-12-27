'''Project 1 - Automating by using the Selenium Python.
1.	Navigate to the URL -https:// katalon-demo-cura.herokuapp.com
2.	Find the Make appointment Button
3.	Click on the Make appointment Button
4.	Next Page will be loaded
5.	Find and Enter the details Username and Password and Click on the Login Button
6.	Verify error message
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_project_1_katalon_negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    user_name = driver.find_element(By.NAME,"username")
    user_name.send_keys("navita")
    user_password = driver.find_element(By.ID,"txt-password")
    user_password.send_keys("Password")
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(5)

    error_message_p_tag = driver.find_element(By.CLASS_NAME,"text-danger")
    print(error_message_p_tag.text)

    assert "Login failed! Please ensure the username and password are valid." == error_message_p_tag


    driver.quit()

