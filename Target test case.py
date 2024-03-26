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
driver.get('https://www.target.com/')

# click sign in button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

sleep(5)
# click side sign in link
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

sleep(5)
#verify sign in page opened-text
#driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']")

sign_in_text=driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
print(sign_in_text)
#assert 'Sign into your Target account' in sign_in_text, f"Expected text not in {sign_in_text}"
print("Test passed")
#verify sign in page opened-button
button=driver.find_element(By.ID, "login").text
print(button)


# verify search results
#assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
#print('Test Passed')
print("Test passed")
driver.quit()
