from selenium import webdriver
import time

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--private")  # Incognito mode
firefox_options.add_argument("--headless")  # Run in background

# Create a loop to perform the process 1000 times
for _ in range(1000):
    query = "rummy modern"
    website = "rummymodern.club"

    # Initialize the Firefox driver
    driver = webdriver.Firefox(options=firefox_options)

    # Use Google to search for the query
    search_url = f"https://www.google.com/search?q={query}"
    driver.get(search_url)

    # Wait for a few seconds to allow the page to load
    time.sleep(2)

    # Open the result with the specified website
    result_url = f"https://{website}"
    driver.get(result_url)

    # Close the browser window
    driver.quit()

    # Add a delay before the next iteration (if needed)
    time.sleep(1)  # Adjust as necessary
