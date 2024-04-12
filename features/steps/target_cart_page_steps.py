from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify cart is empty')
def verify_cart_is_empty(context):
    actual_text=context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f"Expected {expected_text} but got {actual_text}."
@then('Verify item is in cart')
def verify_item_in_cart(context):
    item_in_cart=context.driver.find_element(By.XPATH, "//h2[text()='Order summary']").text
    order_summary='Order summary'
    assert order_summary == item_in_cart, f"Expected item in cart but got no item."