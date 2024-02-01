from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Path to your Chrome WebDriver executable
webdriver_path = 'C:/Windows/System32/chromedriver.exe'

# Set up the Chrome WebDriver with the path
service = Service(webdriver_path)
driver = Chrome(service=service)

# Open Google
url = 'https://www.google.com'
driver.get(url)

# Find the search bar element by name and send a search query
search_query = 'your search query'  # Replace with your desired search query
search_bar = driver.find_element('name', 'q')
search_bar.send_keys(search_query)

# Press Enter to perform the search
search_bar.send_keys(Keys.RETURN)

# Wait for a while to see the results (you may need to adjust the time depending on your internet speed)
driver.implicitly_wait(5)

# Print the title of the search results page
title = driver.title
print(f"Title of the search results page: {title}")

# Close the browser window
driver.quit()
