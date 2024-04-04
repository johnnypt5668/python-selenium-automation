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
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")

#Email field
driver.find_element(By.ID, "ap_email")

#Continue button
driver.find_element(By.ID, "continue")

#Conditions of use link
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

#Privacy Notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

#Need Help link
driver.find_element(By.XPATH, "//*[text()='Need help?']")

#Forgot your Password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

#Create new account button
driver.find_element(By.ID, "createAccountSubmit")

#New To Amazon text(in place of Other issues with sign in link, does not appear on page)
driver.find_element(By.XPATH, "//*[text()='New to Amazon?']")

#Find by CSS Selector
driver.find_element(By.CSS_SELECTOR, "select.nav-search-dropdown")
driver.find_element(By.CSS_SELECTOR, ".nav-search-dropdown")
driver.find_element(By.CSS_SELECTOR, "#searchDropdownBox")
driver.find_element(By.CSS_SELECTOR, "[title='Search in']")
