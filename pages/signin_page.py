from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):

    SIGNIN_PAGE_HEADER = (By.CSS_SELECTOR, "h1")

    def verify_signin_page(self, expected_text):
        #def verify_search_results(self, expected_item):
        expected_text= 'Sign into your Target account'
        actual_text = self.find_element(*self.SIGNIN_PAGE_HEADER).text
        assert expected_text == actual_text, f'Error! Text {expected_text} not on page'