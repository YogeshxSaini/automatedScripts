from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

android_user_agents = [
    "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.2.2; Nexus 4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.3; Galaxy S4 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.2; HTC One Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; Nexus 5 Build/LRX21O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1; Moto G Build/LPBS23.13-56-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Pixel Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ2A.190405.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.4; Moto X Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; Galaxy S5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; OnePlus 3T Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0.0; Galaxy S8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Samsung Galaxy Note 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OnePlus 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36"
]

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()

# Use a random Android user agent
chrome_options.add_argument(f"user-agent={random.choice(android_user_agents)}")

# Other Chrome options...
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")

# Number of times to perform the process
total_loops = 3000

# Create a loop to perform the process
for loop_count in range(1, total_loops + 1):
    query = "svip3patti"

    # Initialize the Chrome driver with custom options
    driver = webdriver.Chrome(options=chrome_options)

    # Use Google to search for the query
    search_url = f"https://www.google.co.in/search?q={query}"
    driver.get(search_url)

    # Measure the start time
    start_time = time.time()

    # Wait for a few seconds to allow the page to load
    time.sleep(0.20)

    result_title = "SVIP 3 Patti - Download Now and Get ₹501 Bonus"

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
        if time.time() - start_time > 10:
            break

    # Check if the loop was skipped due to timeout
    if time.time() - start_time > 10:
        driver.quit()
        continue

    # Click on the search result link
    result_link.click()

    # Print success if the result is found and clicked
    if found_result:
        print("Success - Result found and clicked")

    # Close the browser window
    driver.quit()
    remaining_loops = total_loops - loop_count
    print(f"Remaining loops: {remaining_loops}")

