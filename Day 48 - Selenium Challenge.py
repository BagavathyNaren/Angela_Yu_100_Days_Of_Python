from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.maximize_window()


first_name = driver.find_element(By.XPATH,"//input[@name='fName']").send_keys('John',Keys.RETURN)

last_name = driver.find_element(By.XPATH,"//input[@name='lName']").send_keys('Doe',Keys.RETURN)

email_address = driver.find_element(By.XPATH,"//input[@name='email']").send_keys('john.doe@example.com',Keys.RETURN)    


sign_up_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.close()