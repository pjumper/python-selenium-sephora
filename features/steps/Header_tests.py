from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Verify main header has {expected_amount} links')
def verify_main_header_links(context, expected_amount):
    context.app.header.verify_main_header_links(expected_amount)