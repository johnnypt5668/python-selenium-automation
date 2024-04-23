from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page
class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    TOP_LOGIN = (By.CSS_SELECTOR, "a['data-test='@web/AccountLink']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_login(self):
        self.wait_until_clickable_click(*self.TOP_LOGIN)
