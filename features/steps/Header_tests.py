from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Click New header link')
def click_new_header_link(context):
    context.app.header.click_new_header_link()


@when('Click Just Dropped Link')
def click_just_dropped_link(context):
    context.app.header.click_just_dropped_link()


@then('Verify main header has {expected_amount} links')
def verify_main_header(context, expected_amount):
    context.app.header.verify_main_header_links(expected_amount=12)


@then('Verify New page has {expected_amount} links')
def verify_new_dropdown_links(context, expected_amount):
    context.app.header.verify_new_dropdown_links(expected_amount=7)