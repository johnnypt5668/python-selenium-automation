from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Target homepage is open')
def open_target_homepage(context):
    context.driver.get('https://www.target.com/')

TOP_LOGIN = (By.CSS_SELECTOR, "a['data-test='@web/AccountLink']")
SIDE_LOGIN = (By.CSS_SELECTOR, "a['data-test='accountNav-signIn']")
#@when('Click on login on top and on side')
#def target_login(context):
    #context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    #context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@when('Click on header login')
def header_login(context):
    context.app.header.click_login()


@then('Verify sign in page is open')
def verify_sign_in(context):
    sign_in_text=context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in sign_in_text, f"Expected text {sign_in_text} is not on page."


@then('Store original login window')
def store_original_login_window(context):
    context.original_window = context.app.signin_page.get_current_window()

@then('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.signin_page.click_tc_link()
    sleep(5)

@then('Switch to newly opened window')
def switch_to_newly_opened_window(context):
    context.app.signin_page.switch_to_newly_opened_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.signin_page.verify_tc_page()

@then('User can close new window and switch back to original')
def close_and_return_to_original_window(context):
    context.app.signin_page.close()
    context.app.signin_page.switch_window_by_id(context.original_window.id)

