from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@when('Click All New link')
def click_all_new_link(context):
    context.app.new_header.click_all_new_link()


@when('Click Just Dropped Link')
def click_just_dropped_link(context):
    context.app.new_header.click_just_dropped_link()


@when('Click Holiday Gift Guide link')
def click_holiday_gift_guide_link(context):
    context.app.new_header.click_holiday_gift_guide_link()


@when('Click The Next Big Think Link')
def click_next_big_thing_link(context):
    context.app.new_header.click_next_big_thing_link()


@when('Click Bestseller Link')
def click_bestseller_link(context):
    context.app.new_header.click_bestseller_link()


@when('Click Trending on Social Link')
def click_trending_social_link(context):
    context.app.new_header.click_trending_social_link()


@then('Verify {expected_text} page is opened8')
def verify_just_dropped_page_opened(context, expected_text):
    context.app.new_header.verify_all_new_page_opened(expected_text)


@then('Verify {expected_text} page is opened')
def verify_just_dropped_page_opened(context, expected_text):
    context.app.new_header.verify_just_dropped_page_opened(expected_text)


@then('Verify {expected_text} page is opened7')
def verify_holiday_gift_guide_page_opened(context, expected_text):
    context.app.new_header.verify_holiday_gift_guide_page_opened(expected_text)


@then('Verify {expected_text} page is opened9')
def verify_next_big_thing_link(context, expected_text):
    context.app.new_header.verify_next_big_thing_link(expected_text)


@then('Verify {expected_text} page is opened10')
def verify_bestseller_link(context, expected_text):
    context.app.new_header.verify_bestseller_link(expected_text)


@then('Verify {expected_text} page is present11')
def verify_trending_social_page_present(context, expected_text):
    context.app.new_header.verify_trending_social_page_present(expected_text)