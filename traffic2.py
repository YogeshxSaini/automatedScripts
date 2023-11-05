from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure the Chrome options to open in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Create a loop to perform the process 1000 times
for _ in range(1000):
    query = "rummy modern"

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Use Google to search for the query
    search_url = f"https://www.google.com/search?q={query}"
    driver.get(search_url)

    # Wait for a few seconds to allow the page to load
    time.sleep(1)

    result_title = "Rummy Modern - Download and Get Rs.1500 Real Cash"

    while True:
        try:
            # Find the search result link with the specified title
            result_link = driver.find_element(By.PARTIAL_LINK_TEXT, result_title)
            break  # If found, exit the loop
        except:
            # If the result is not found, scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

    # Click on the search result link
    result_link.click()

    # Close the browser window
    driver.quit()
