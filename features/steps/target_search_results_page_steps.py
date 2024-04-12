from selenium.webdriver.common.by import By
from behave import then
from time import sleep


SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
SELECT_ITEM = (By.XPATH, "//button[@data-test='chooseOptionsButton']")
SELECT_SHIPPING = (By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
ADD_SHIPPING = (By.XPATH, "//button[@data-test='shippingButton']")
ADD_TO_CART = (By.CSS_SELECTOR, "a[href='/cart']")


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'

@then('Place item in cart')
def place_item_in_cart(context):
    context.driver.find_element(*SELECT_ITEM).click()
    sleep(6)
    context.driver.find_element(*SELECT_SHIPPING).click()
    sleep(6)
    context.driver.find_element(*ADD_SHIPPING).click()
    sleep(6)
    context.driver.find_element(*ADD_TO_CART).click()
