from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv  
load_dotenv()  # Load environment variables from .env file  

SIMILAR_ACCOUNT = "buzzfeedtasty" # Change this to an account of your choice
USERNAME = os.getenv("INSTAGRAM_USERNAME")  # Your Instagram username
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")  # Your Instagram password


class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)  # 15 second timeout for explicit waits

    # Avoid bot-like behaviour and try not to run your script too often.
    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        
        # Wait for page to load and check for cookie warning
        time.sleep(2)  # Brief initial sleep for page load
        
        # Check and handle cookie warning with explicit wait
        decline_cookies_xpath = "//button[contains(text(), 'Decline') or contains(text(), 'Reject') or contains(text(), 'Not Now')]"
        try:
            cookie_warning = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, decline_cookies_xpath))
            )
            cookie_warning.click()
            time.sleep(1)
        except:
            print("No cookie warning found or could not dismiss it")

        # Wait for and fill username field
        username = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        username.send_keys(USERNAME)
        
        # Wait for and fill password field
        password = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        # Handle save login prompt
        try:
            save_login_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Not now') or contains(text(), 'Not Now')]"))
            )
            save_login_prompt.click()
            time.sleep(1)
        except:
            print("No save login prompt found")

        # Handle notifications prompt
        try:
            notifications_prompt = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now') or contains(text(), 'Not now')]"))
            )
            notifications_prompt.click()
            time.sleep(1)
        except:
            print("No notifications prompt found")

    def find_followers(self):
        time.sleep(3)
        # Will bring up the followers of an account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

         # Handle save login prompt
        try:
            click_followers_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'followers')]"))
            )
            click_followers_button.click()
            time.sleep(1)
        except:
            print("No followers button found")

        
        # Wait for followers modal to appear
        time.sleep(5)
        
        # The xpath of the modal will change over time. Update yours accordingly.
        modal_xpath = "//div[@role='dialog']//div[@class]"
        try:
            modal = self.wait.until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )
            
            for i in range(5):
                # Scroll the modal to load more followers
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)
        except:
            print("Could not find followers modal. XPath might need updating.")
            # Alternative modal selector
            try:
                modal_alt = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'overflow: hidden')]"))
                )
                for i in range(5):
                    self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal_alt)
                    time.sleep(2)
            except:
                print("Alternative modal selector also failed.")

    def follow(self):
        # Wait for follow buttons to be present
        try:
            all_buttons = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button'))
            )
            
            # Filter for follow buttons (look for buttons containing "Follow" text)
            follow_buttons = [btn for btn in all_buttons if btn.text == "Follow"]
            
            if not follow_buttons:
                print("No follow buttons found. Trying alternative selector...")
                follow_buttons = self.driver.find_elements(By.XPATH, "//button[div/div/div[text()='Follow']]")
            
            print(f"Found {len(follow_buttons)} follow buttons")
            
            for button in follow_buttons:
                try:
                    if button.is_displayed() and button.is_enabled():
                        # Scroll button into view before clicking
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                        time.sleep(0.5)
                        
                        button.click()
                        time.sleep(1.5)  # Wait between follows to avoid detection
                        
                except ElementClickInterceptedException:
                    try:
                        # Handle the unfollow dialog if it appears
                        cancel_button = self.wait.until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cancel')]"))
                        )
                        cancel_button.click()
                        time.sleep(1)
                    except:
                        print("Could not find cancel button")
                        continue
                except Exception as e:
                    print(f"Error clicking button: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error finding follow buttons: {e}")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()