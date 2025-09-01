
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file
RENTING_FORM_LINK = os.getenv("RENTING_FORM_LINK")  # Your Google Form link
RENTING_FORM_SHORT_LINK = os.getenv("RENTING_FORM_SHORT_LINK")  #
ZILLOW_CLONE_WEBSITE = os.getenv("ZILLOW_CLONE_WEBSITE")  # Your Zillow clone website link

# Part 1 - Scrape the links, addresses, and prices of the rental properties

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Use our Zillow-Clone website (instead of Zillow.com)
if not ZILLOW_CLONE_WEBSITE:
    raise ValueError("ZILLOW_CLONE_WEBSITE environment variable is not set.")
response = requests.get(ZILLOW_CLONE_WEBSITE, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
# Python list comprehension (covered in Day 26)
all_links = [link["href"] for link in all_link_elements] 
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

# Create a list of all the prices on the page using a CSS Selector
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)


# Part 2 - Fill in the Google Form using Selenium

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Create WebDriverWait instance with 10 second timeout
wait = WebDriverWait(driver, 10)

for n in range(len(all_links)):
    # TODO: Add fill in the link to your own Google Form
    driver.get(str(RENTING_FORM_SHORT_LINK))
    
    try:
        # Wait for form elements to be present and interactable
        address = wait.until(EC.element_to_be_clickable((By.XPATH, 
             "//span[contains(.,'the address of the property?')]/following::input[1]")))
        
        price = wait.until(EC.element_to_be_clickable((By.XPATH,
            "//span[contains(.,'the price per month?')]/following::input[1]")))
        
        link = wait.until(EC.element_to_be_clickable((By.XPATH,
            "//span[contains(.,'the link to the property?')]/following::input[1]")))
        
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,
            "//span[text()='Submit']")))
        
        # Fill in the form fields
        address.send_keys(all_addresses[n])
        price.send_keys(all_prices[n])
        link.send_keys(str(all_links[n]))
        
        # Click submit button
        submit_button.click()
        
        # Wait for form submission to complete before proceeding to next iteration
        time.sleep(2)
        
    except Exception as e:
        print(f"Error processing form {n+1}: {e}")
        continue

# Close the driver when done
driver.quit()