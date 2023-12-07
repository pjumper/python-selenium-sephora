from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Home Page')
def open_home(context):
    context.app.main_page.open_home()
