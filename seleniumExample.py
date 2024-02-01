from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

# Path to your Chrome WebDriver executable
webdriver_path = 'C:/Windows/System32/chromedriver.exe'


# Set up the Chrome WebDriver with the path
service = Service(webdriver_path)
driver = Chrome(service=service)

# Open the website
url = 'https://www.example.com'  # Replace with your desired URL
driver.get(url)

# Get the title of the page and print it
title = driver.title
print(f"Title of the page: {title}")

# Close the browser window
driver.quit()
