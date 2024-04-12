from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_LINKS = (By.CSS_SELECTOR, "a[href*='target-circle']")

@then('Verify 5 links in benefits section')
def verify_benefit_links(context):
    links = context.driver.find_elements(*BENEFIT_LINKS)
    assert len(links) == 5, f"Expected 5 links, got {len(links)}"