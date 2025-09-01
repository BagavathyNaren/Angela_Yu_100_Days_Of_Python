from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC

import os

load_dotenv()

FB_EMAIL = os.getenv("FB_EMAIL")  # Replace with your Facebook email
FB_PASSWORD = os.getenv("FB_PASSWORD")  # Replace with your Facebook password

if FB_EMAIL is None or FB_PASSWORD is None:
    raise ValueError("FB_EMAIL and FB_PASSWORD environment variables must be set.")


driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

driver.maximize_window()

sleep(10)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

# # Click More options
# wait = WebDriverWait(driver, 20)

# wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"More options")]'))).click()

try:
    more_options_button = driver.find_element(By.XPATH, value='//button[contains(text(),"More options")]')
    more_options_button.click()
except:
    print("More options button not found, continuing...")
    sleep(10)
    fb_login = driver.find_element(By.XPATH, value="//*[text()='Log in with Facebook']")
    fb_login.click()

sleep(8)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(7)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 3 second delay between likes.
    sleep(3)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()