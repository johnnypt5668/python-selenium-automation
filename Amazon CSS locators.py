from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon-logo")

#create account text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#your name text box
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

#email text box
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

#password text box
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

#password instruction text
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content and [class*='Passwords']")

#reenter password text box
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

#Create new account button(Continue)
driver.find_element(By.CSS_SELECTOR, "input#continue")

#Condition of use link
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

#Privacy notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")

#Already have account sign in link
driver.find_element(By.CSS_SELECTOR, "a[href*='openid.return_to']")