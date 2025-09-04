from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from dotenv import load_dotenv  

load_dotenv()

# Constants for promised internet speeds
PROMISED_DOWN = 150
PROMISED_UP = 150
TWITTER_PHONE = os.getenv("TWITTER_EMAIL")
TWITER_PASSWORD = os.getenv("TWITTER_PASSWORD")
if TWITTER_PHONE is None or TWITER_PASSWORD is None:
    raise ValueError("TWITTER_PHONE and TWITER_PASSWORD environment variables must be set.")

class InternetSpeedTwitterBot():
          
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_option)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 30)  # 30 second timeout for explicit waits

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        
        # Wait for and click the start button
        self.button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label*='start speed test']"))
        )
        self.button.click()
        
        # Wait for speed test to complete and results to be visible
        sleep(45)  # Keeping sleep for the speed test itself as it takes time
        
        # Wait for download speed result to be visible
        self.down = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class*='download-speed']"))
        ).text
        
        # Wait for upload speed result to be visible
        self.up = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class*='upload-speed']"))
        ).text
        
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(url="https://x.com/i/flow/login")
        
        # Wait for and fill username/phone input
        self.phone_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='username']"))
        )
        self.phone_input.click()
        self.phone_input.send_keys(TWITTER_PHONE, Keys.ENTER)
        
        # Wait for password field to be visible
        self.pass_input = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        self.pass_input.send_keys(TWITER_PASSWORD, Keys.ENTER)
        
        # Wait for post input field to be clickable
        self.post_input = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Post text']"))
        )
        
        self.post_input.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up"
                                  f" when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        
        # Wait for tweet button to be clickable
        self.post = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']"))
        )
        self.post.click()
        
        # Wait briefly to ensure tweet is posted
        sleep(3)

interspeed = InternetSpeedTwitterBot()
interspeed.get_internet_speed()
if float(interspeed.down) < PROMISED_DOWN or float(interspeed.up) < PROMISED_UP:
     interspeed.tweet_at_provider()