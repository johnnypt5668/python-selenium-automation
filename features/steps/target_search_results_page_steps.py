from selenium.webdriver.common.by import By
from behave import then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
SELECT_ITEM = (By.XPATH, "//button[@data-test='chooseOptionsButton']")
SELECT_SHIPPING = (By.XPATH, "//button[@data-test='fulfillment-cell-shipping']")
ADD_SHIPPING = (By.XPATH, "//button[@data-test='shippingButton']")
ADD_TO_CART = (By.CSS_SELECTOR, "a[href='/cart']")


@then('Place item in cart')
def place_item_in_cart(context):
    context.driver.find_element(*SELECT_ITEM)
    context.wait.until(EC.element_to_be_clickable(SELECT_ITEM)).click()
    context.driver.find_element(*SELECT_SHIPPING).click()
    context.driver.find_element(*ADD_SHIPPING).click()
    context.driver.find_element(*ADD_TO_CART).click()


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
#    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
#    assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
    context.app.search_result_page.verify_search_results(expected_item)

@then('Verify every product has a name and image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    top_products = context.driver.find_elements(*LISTINGS)[:4]
    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)