from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Target home page is open')
def open_target_home_page(context):
    context.driver.get('https://www.target.com/')
@when('Click on cart logo in top corner')
def click_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart?prehydrateClick=true']").click()

sleep(5)
@then('Verify cart is empty')
def verify_cart_is_empty(context):
    actual_text=context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_text, f"Expected text {actual_text} not on page"
sleep(5)