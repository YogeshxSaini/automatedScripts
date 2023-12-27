from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")  # Incognito mode
# chrome_options.add_argument("--headless")  # Run in background

# Create a Chrome profile with the desired user agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36")

# Number of times to perform the process
total_loops = 1000

# Create a loop to perform the process 1000 times
for loop_count in range(1, total_loops + 1):
    query = "svip3patti"

    # Initialize the Chrome driver with custom options
    driver = webdriver.Chrome(options=chrome_options)

    # Use Google to search for the query
    search_url = f"https://www.google.co.in/search?q={query}&start=10"
    driver.get(search_url)

    # Measure the start time
    start_time = time.time()

    # Wait for a few seconds to allow the page to load
    time.sleep(0.20)

    result_title = "SVIP 3 Patti Online - Play Online 3 Patti and Win Big"

    found_result = False

    while True:
        try:
            # Wait until the search result link with the specified title is clickable
            result_link = WebDriverWait(driver, 0).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, result_title))
            )
            found_result = True
            break  # If found and clickable, exit the loop
        except:
            # If the result is not found or not clickable, scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Check if more than 5 seconds have passed; if so, skip to the next loop
        if time.time() - start_time > 5:
            print("Initial search result not found. Trying another search URL.")
            break

    if not found_result:
        # Perform another search with a different URL
        alternate_search_url = f"https://www.google.co.in/search?q={query}&start=20"
        driver.get(alternate_search_url)

        while True:
            try:
                # Wait until the search result link with the specified title is clickable
                result_link = WebDriverWait(driver, 0).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, result_title))
                )
                found_result = True
                break  # If found and clickable, exit the loop
            except:
                # If the result is not found or not clickable, scroll down the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Check if more than 5 seconds have passed; if so, skip to the next loop
            if time.time() - start_time > 5:
                print("Alternate search result not found. Skipping to the next loop.")
                break

    # Check if the loop was skipped due to timeout
    if time.time() - start_time > 5:
        driver.quit()
        continue

    # Print a message based on whether the result was found on the first or second search URL
    if found_result and "start=10" in driver.current_url:
        print("Result found on the first search URL.")
    elif found_result and "start=20" in driver.current_url:
        print("Result found on the second search URL.")

    # Click on the search result link
    result_link.click()

    # Close the browser window
    driver.quit()
    remaining_loops = total_loops - loop_count
    print(f"Remaining loops: {remaining_loops}")

