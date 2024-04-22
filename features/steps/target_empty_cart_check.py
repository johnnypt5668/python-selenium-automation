from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify cart is empty')
def verify_cart_is_empty(context):
    actual_text=context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'Your cart is empty' in actual_text, f"Expected text {actual_text} not on page"