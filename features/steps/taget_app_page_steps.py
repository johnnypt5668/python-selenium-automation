from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Target App page')
def open_taget_app(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print ('Current:', context.original_window)
