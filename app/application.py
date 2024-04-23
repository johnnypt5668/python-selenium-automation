from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.signin_page import SigninPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)