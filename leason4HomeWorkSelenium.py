import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    # Setup - create a Chrome WebDriver instance
    driver = webdriver.Chrome()
    yield driver  # Pass the WebDriver instance to the test function
    # Teardown - close the browser after the test
    driver.quit()


def test_ycombinator_title(driver):
    # Open the Y Combinator website
    driver.get("https://www.ycombinator.com/")

    # Get the title of the webpage
    title = driver.title

    # Check if the title is "Y Combinator"
    assert title == "Y Combinator", f"Title mismatch: Expected 'Y Combinator', but got '{title}'"


def test_dockerhub_title(driver):
    # Open the Docker Hub website
    driver.get("https://hub.docker.com")

    # Get the title of the webpage
    title = driver.title

    # Check if the title is correct
    expected_title = "Docker Hub Container Image Library | App Containerization"
    assert title == expected_title, f"Title mismatch: Expected '{expected_title}', but got '{title}'"

# Expected :'Docker Hub Container Image Library | App Containerization'
# Actual   :'Docker'
