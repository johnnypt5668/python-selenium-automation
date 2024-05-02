from selenium.webdriver.common.by import By
from pages.base_page import Page

class SigninPage(Page):

    SIGNIN_PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    SIGNIN_PAGE_EMAIL_BOX = (By.ID, "username")
    SIGNIN_PAGE_PASSWORD_BOX = (By.ID, "password")
    SIGNIN_BUTTON = (By.ID, "login")
    INCORRECT_PASSWORD = (By.ID, 'password--ErrorMessage')
    TC_LINK = (By.CSS_SELECTOR, "a[href='/c/terms-conditions/-/N-4sr7l']")


    def verify_signin_page(self, expected_text):
        #def verify_search_results(self, expected_item):
        expected_text= 'Sign into your Target account'
        actual_text = self.find_element(*self.SIGNIN_PAGE_HEADER).text
        assert expected_text == actual_text, f'Error! Text {expected_text} not on page'

    def enter_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        self.click(*self.SIGNIN_BUTTON)

    def verify_incorrect_password_message(self):
        expected_message = "Please enter a valid password"
        actual_message = self.find_element(*self.INCORRECT_PASSWORD).text
        assert expected_message == actual_message, f'Error! Text {expected_message} not on page.'


    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')