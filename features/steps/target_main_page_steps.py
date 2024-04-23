from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_LOGIN = (By.CSS_SELECTOR, "a['data-test='accountNav-signIn']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()

@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)

@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@then('Click on side login')
def click_side_login(self):
    self.wait_until_clickable_click(*self.SIDE_LOGIN)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # Add multiple:
    # add_cart_btns = context.driver.find_elements(*ADD_TO_CART_BTN)
    # for btn in add_cart_btns[:5]:
    #     btn.click() # => will click on the first 5 buttons 1 by 1
    # add_cart_btns[4].click() # => will only click on the 5th Add to cart btn
@when('Store product name')
def store_product_name(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not present on the page'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    context.wait.until(
        EC.invisibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side nav, Add to Cart button did not disappear'
    )
@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)
@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount): # expected_amount = '5'
    expected_amount = int(expected_amount)   # '5' (str) => 5 (int)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


#from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# SEARCH_INPUT = (By.ID, 'search')
# SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
# CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
# HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
# HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
#
#
# @given('Open Target main page')
# def open_target(context):
#     context.app.main_page.open_main()
#
#
# #@when("Search for {item}")
# #def search_product(context, item):
# #    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
# #    context.driver.find_element(*SEARCH_BTN).click()
# #    sleep(6)
#
# @when("Search for {item}")
# def search_item(context, item):
#     context.app.header.search_product(item)
#     sleep(6)
#
# # @when("Search for 'AirPods (3rd Generation)'")
# # def search_coffee(context):
# #     context.driver.find_element(*SEARCH_INPUT).send_keys('AirPods (3rd Generation)')
# #     context.driver.find_element(*SEARCH_BTN).click()
# #     sleep(6)
# @when('Click on Cart icon')
# def click_cart(context):
#     context.app.header.click_cart()
#
#
# @then('Verify header in shown')
# def verify_header_shown(context):
#     context.driver.find_element(*HEADER)
#
#
# @then('Verify header has {expected_amount} links')
# def verify_header_links(context, expected_amount): # expected_amount = '5'
#     expected_amount = int(expected_amount)   # '5' (str) => 5 (int)
#     links = context.driver.find_elements(*HEADER_LINKS)
#     assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
#     # to print all names:
#     # for link in links:
#     #     print(link.text)
#     # all_text = [link.text for link in links]
#     # print(all_text)
#
# @when('Click on Target page link')
# def click_target_cirrcle_page(context):
#     context.driver.find_element(By.ID, "utilityNav-circle").click()