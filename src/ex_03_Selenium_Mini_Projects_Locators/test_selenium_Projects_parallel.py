import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_project_1_katalon_positive():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    user_name = driver.find_element(By.NAME,"username")
    user_name.send_keys("John Doe")
    user_password = driver.find_element(By.ID,"txt-password")
    user_password.send_keys("ThisIsNotAPassword")
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    print("current URL is",driver.current_url)
    assert "https://katalon-demo-cura.herokuapp.com/#appointment"==driver.current_url
    time.sleep(10)

def test_project_1_katalon_negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_element.click()
    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("navita")
    user_password = driver.find_element(By.ID, "txt-password")
    user_password.send_keys("Password")
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(5)

    error_message_p_tag = driver.find_element(By.CLASS_NAME, "text-danger")
    print(error_message_p_tag.text)

    assert "Login failed! Please ensure the username and password are valid." == error_message_p_tag.text

    time.sleep(10)
    driver.quit()

