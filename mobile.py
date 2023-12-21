from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--private")  # Incognito mode
firefox_options.add_argument("--headless")  # Run in background

# Create a Firefox profile with the desired user agent
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36")

firefox_options.profile = profile  # Set the profile using the correct attribute

# Number of times to perform the process
total_loops = 1000

# Create a loop to perform the process 1000 times
for loop_count in range(1, total_loops + 1):
    query = "rummy modern"

    # Initialize the Firefox driver with custom options
    driver = webdriver.Firefox(options=firefox_options)

    # Use Google to search for the query
    search_url = f"https://www.google.co.in/search?q={query}"
    driver.get(search_url)

    # Measure the start time
    start_time = time.time()
    
    # Wait for a few seconds to allow the page to load
    time.sleep(0.20)

    result_title = "Rummy Modern - Download and Get Rs.1500 Real Cash"

    while True:
        try:
            # Wait until the search result link with the specified title is clickable
            result_link = WebDriverWait(driver, 0).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, result_title))
            )
            break  # If found and clickable, exit the loop
        except:
            # If the result is not found or not clickable, scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Check if more than 5 seconds have passed; if so, skip to the next loop
        if time.time() - start_time > 5:
            print("Skipping to the next loop due to timeout")
            break
        
    # Check if the loop was skipped due to timeout
    if time.time() - start_time > 5:
        driver.quit()
        continue
    
    # Click on the search result link
    result_link.click()

    # Close the browser window
    driver.quit()
    remaining_loops = total_loops - loop_count
    print(f"Remaining loops: {remaining_loops}")
