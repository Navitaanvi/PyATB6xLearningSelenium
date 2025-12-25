from selenium import webdriver
import allure
import pytest

@allure.title("Print the page source of the page")
def test_selenium():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_as_html = driver.page_source
    print(driver.title)
    print(driver.current_url)
    assert "CURA Healthcare Service" in page_source_as_html
    driver.quit()


