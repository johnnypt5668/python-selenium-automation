from selenium.webdriver.common.by import By
from behave import then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.wait = WebDriverWait(driver, timeout=10)

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
    context.driver.find_element(*SELECT_ITEM)
    driver.wait.until(EC.element_to_be_clickable(*SELECT_ITEM)).click()
    context.driver.find_element(*SELECT_SHIPPING).click()
    context.driver.find_element(*ADD_SHIPPING).click()
    context.driver.find_element(*ADD_TO_CART).click()
