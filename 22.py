from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the Tip Calculator page using the reference path
driver.get("C:/Users/davidbi/Downloads/tip_calc/tip_calc/index.html")

# Find and interact with the elements on the page
bill_input = driver.find_element(By.ID, "billamt")
bill_input.clear()
bill_input.send_keys("100")

service_dropdown = Select(driver.find_element(By.ID, "serviceQual"))
service_dropdown.select_by_value("0.2")  # Choosing 20% - Good

people_input = driver.find_element(By.ID, "peopleamt")
people_input.clear()
people_input.send_keys("4")

music_quality_input = driver.find_element(By.ID, "musicQuality")
music_quality_input.clear()
music_quality_input.send_keys("5")

calculate_button = driver.find_element(By.ID, "calculate")
calculate_button.click()

# Wait for the result to be calculated (adjust the sleep time if needed)
sleep(2)

# Get the calculated tip value
tip_value = driver.find_element(By.ID, "tip").text
print("Calculated Tip:", tip_value)

# Close the browser window
driver.quit()
