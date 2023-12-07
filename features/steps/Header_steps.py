from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Hover over New header link')
def hover_new_header_link(context):
    context.app.header.hover_new_header_link()


@when('Click Makeup link')
def click_makeup_page_link(context):
    context.app.header.click_makeup_page_link()


@when('Click New Skincare link')
def click_new_skin_link(context):
    context.app.header.click_new_skin_link()


@when('Click New Haircare link')
def click_new_haircare_link(context):
    context.app.header.click_new_haircare_link()


@when('Click New Fragrance link')
def click_new_fragrance_link(context):
    context.app.header.click_new_fragrance_link()


@when('Click New Bath & Body link')
def click_new_bath_body_link(context):
    context.app.header.click_new_bath_body_link()


@when('Click New Tools & Brushes link')
def click_new_tools_brushes_link(context):
    context.app.header.click_new_tools_brushes_link()


@then('Verify main header has {expected_amount} links')
def verify_main_header(context, expected_amount):
    context.app.header.verify_main_header_links(expected_amount=12)


@then('Verify new header has {expected_amount} links')
def verify_new_header_dropdown_links(context, expected_amount):
    context.app.header.verify_new_header_dropdown_links(expected_amount=17)


@then('Verify New page has {expected_amount} links')
def verify_new_dropdown_links(context, expected_amount):
    context.app.header.verify_new_dropdown_links(expected_amount=7)

@then('Verify {expected_text} page is opened1')
def verify_makeup_page_link(context, expected_text):
    context.app.header.verify_makeup_page_link_opened(expected_text)

@then('Verify {expected_text} page is opened2')
def verify_new_skin_page_opened(context, expected_text):
    context.app.header.verify_new_skin_page_opened(expected_text)


@then('Verify {expected_text} page is opened3')
def verify_new_haircare_page_opened(context, expected_text):
    context.app.header.verify_new_haircare_page_opened(expected_text)


@then('Verify {expected_text} page is opened4')
def verify_new_fragrance_page_opened(context, expected_text):
    context.app.header.verify_new_fragrance_page_opened(expected_text)


@then('Verify {expected_text} page is opened5')
def verify_new_bath_body_page_opened(context, expected_text):
    context.app.header.verify_new_bath_body_page_opened(expected_text)


@then('Verify {expected_text} page is opened6')
def verify_new_tools_brushes_page_opened(context, expected_text):
    context.app.header.verify_new_tools_brushes_page_opened(expected_text)



