from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")

if not FB_EMAIL or not FB_PASSWORD:
    raise ValueError("FB_EMAIL and FB_PASSWORD environment variables must be set.")

driver = webdriver.Chrome()
driver.get("https://tinder.com")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Click Login
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Log in")]')))
login_button.click()

# Click More options
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"More options")]'))).click()

# Select Facebook login option
fb_login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button//div[contains(text(),"Log in with Facebook")]')))
fb_login_btn.click()

# Switch to Facebook login window
base_window = driver.window_handles[0]
wait.until(lambda d: len(d.window_handles) > 1)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Facebook login
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(FB_EMAIL)
driver.find_element(By.ID, "pass").send_keys(FB_PASSWORD + Keys.ENTER)

# Back to Tinder
driver.switch_to.window(base_window)

# Allow location
try:
    allow_location_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Allow")]')))
    allow_location_button.click()
except TimeoutException:
    pass

# Disable notifications
try:
    notifications_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not interested")]')))
    notifications_button.click()
except TimeoutException:
    pass

# Accept cookies
try:
    cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"I accept")]')))
    cookies_button.click()
except TimeoutException:
    pass

# Swipe right (like)
for n in range(100):
    sleep(3)
    try:
        like_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Like"]')))
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.itsAMatch a')))
            match_popup.click()
        except TimeoutException:
            pass
    except TimeoutException:
        pass

driver.quit()
