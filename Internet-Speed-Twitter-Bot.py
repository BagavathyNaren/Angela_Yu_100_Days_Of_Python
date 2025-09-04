import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome()
        self.twitter_email = os.getenv("TWITTER_EMAIL")
        self.twitter_password = os.getenv("TWITTER_PASSWORD")
        if self.twitter_email is None or self.twitter_password is None:
            raise ValueError("TWITTER_EMAIL and TWITTER_PASSWORD environment variables must be set.")
        self.promised_down = int(os.getenv("PROMISED_DOWN", 150))
        self.promised_up = int(os.getenv("PROMISED_UP", 10))


def get_internet_speed():
    bot = InternetSpeedTwitterBot()
    bot.driver.get("https://www.speedtest.net/")
    sleep(5)
    
    try:
        agree_button = bot.driver.find_element(By.XPATH, '//button[text()="Agree"]')
        agree_button.click()
    except NoSuchElementException:
        print("Agree button not found, continuing...")

    go_button = bot.driver.find_element(By.CLASS_NAME, "start-text")
    go_button.click()

    sleep(60)  # Wait for the test to complete

    bot.down = float(bot.driver.find_element(By.CLASS_NAME, "download-speed").text)
    bot.up = float(bot.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    print(f"Download Speed: {bot.down} Mbps")
    print(f"Upload Speed: {bot.up} Mbps")

    return bot.down, bot.up

def tweet_at_provider():
    bot = InternetSpeedTwitterBot()
    bot.driver.get("https://twitter.com/login")
    sleep(5)

    email_input = bot.driver.find_element(By.NAME, "text")
    email_input.send_keys(bot.twitter_email)
    email_input.send_keys(Keys.ENTER)

    sleep(3)
    
    password_input = bot.driver.find_element(By.NAME, "password")
    password_input.send_keys(bot.twitter_password)
    password_input.send_keys(Keys.ENTER)

    sleep(5)

    tweet_text = f"Hey Internet Provider, why is my internet speed {bot.down} down/{bot.up} up when I pay for {bot.promised_down} down/{bot.promised_up} up?"
    
    tweet_box = bot.driver.find_element(By.XPATH, '//div[@aria-label="Tweet text"]')
    tweet_box.send_keys(tweet_text)

    tweet_button = bot.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
    tweet_button.click()

    print("Tweet sent successfully!")


Get_Internet_Speed = get_internet_speed()
Tweet_At_Provider = tweet_at_provider()