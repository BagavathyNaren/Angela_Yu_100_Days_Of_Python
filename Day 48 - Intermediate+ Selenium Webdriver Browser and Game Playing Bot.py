# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# # Keep Chrome Browser Open After Program Finishes 

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

 
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# #driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")   
# #driver.get("https://www.python.org/")  


# driver.maximize_window()

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is: {price_dollar.text}.{price_cent.text}")



# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#search_bar.send_keys("Python")
#search_bar.submit()

# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#button.click()
# python_documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(python_documentation_link.text)


# bug_link = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)


# upcoming_events_xpath = "//*[text()='Upcoming Events']//following-sibling::ul/li"

# upcoming_events = driver.find_elements(By.XPATH, upcoming_events_xpath)
# print(f"No of upcoming events: {len(upcoming_events)}")

# upcoming_events_dictionary = {}

# for event in upcoming_events:
#     event_count = int(upcoming_events.index(event)+1)
#     print("Event Count: "+str(event_count))
#     event_dates_xpath = f'(//*[text()="Upcoming Events"]//following-sibling::ul/li/time)[{event_count}]'
#     event_names_xpath = f'(//*[text()="Upcoming Events"]//following-sibling::ul/li/a)[{event_count}]'
#     event_date = driver.find_element(By.XPATH, event_dates_xpath).text
#     event_name = driver.find_element(By.XPATH, event_names_xpath).text
#     upcoming_events_dictionary[int(upcoming_events.index(event))] = {"date": event_date, "name": event_name}

    
# print(upcoming_events_dictionary)

# future_python_events = {i: {
#     "date": driver.find_element(By.XPATH, f'(//*[text()="Upcoming Events"]//following-sibling::ul/li/time)[{i+1}]').text,
#     "name": driver.find_element(By.XPATH, f'(//*[text()="Upcoming Events"]//following-sibling::ul/li/a)[{i+1}]').text
# } for i in range(len(upcoming_events))

# }

# print(future_python_events)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(f"Number of articles: {article_count.text}")
# #article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# print(f"All portals link text: {all_portals.text}")
# #all_portals.click()

# search = driver.find_element(By.NAME, "search")
# print(f"Search bar placeholder: {search.get_attribute('placeholder')}")
# search.send_keys("Python",Keys.RETURN)

# driver.close()

#driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)  # more loading
except NoSuchElementException:
    print("Language selection not found")

# Wait for everything to settle
sleep(2)

# Find the big cookie to click
cookie = driver.find_element(by=By.ID, value="bigCookie")

# Get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]

# Set timers
wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            # Extract number from text like "123 cookies"
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 5 minutes
    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break