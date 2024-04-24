from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Target homepage is open')
def open_target_homepage(context):
    context.driver.get('https://www.target.com/')

TOP_LOGIN = (By.CSS_SELECTOR, "a['data-test='@web/AccountLink']")
SIDE_LOGIN = (By.CSS_SELECTOR, "a['data-test='accountNav-signIn']")

#@when('Click on login on top and on side')
#def target_login(context):
    #context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    #context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@when('Click on header login')
def header_login(context):
    context.app.header.click_login()




@then('Verify sign in page is open')
def verify_sign_in(context):
    sign_in_text=context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in sign_in_text, f"Expected text {sign_in_text} is not on page."