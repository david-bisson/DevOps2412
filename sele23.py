import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculate_tip(browser):
    # Open the Tip Calculator page using the reference path
    browser.get("C:/Users/davidbi/Downloads/tip_calc/tip_calc/index.html")

    # Find and interact with the elements on the page
    bill_input = browser.find_element(By.ID, "billamt")
    bill_input.clear()
    bill_input.send_keys("100")

    service_dropdown = Select(browser.find_element(By.ID, "serviceQual"))
    service_dropdown.select_by_value("0.2")  # Choosing 20% - Good

    people_input = browser.find_element(By.ID, "peopleamt")
    people_input.clear()
    people_input.send_keys("4")

    music_quality_input = browser.find_element(By.ID, "musicQuality")
    music_quality_input.clear()
    music_quality_input.send_keys("5")

    calculate_button = browser.find_element(By.ID, "calculate")
    calculate_button.click()

    # Wait for the result to be calculated (adjust the sleep time if needed)
    sleep(2)

    # Get the calculated tip value
    tip_value = browser.find_element(By.ID, "tip").text
    assert tip_value == "25"  # Replace with the expected tip value
