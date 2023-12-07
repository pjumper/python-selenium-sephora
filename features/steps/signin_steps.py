from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@when('Click Signin Link')
def click_signin(context):
    context.app.signin.click_signin()

@when('Hover over Signin Link')
def hover_sign(context):
    context.app.signin.hover_signin()


@when('Input {text} in email field')
def input_signin_email(context, text):
    context.app.signin.input_signin_email(text)


@when('Input {text} in password field')
def input_signin_password(context, text):
    context.app.signin.input_signin_password(text)


@when('Click Signin Button')
def click_signin_bttn(context):
    context.app.signin.click_signin_bttn()


@when('Click popup signin button')
def click_signin_popup_bttn(context):
    context.app.signin.click_signin_popup_bttn()

@when('Hover over signin icon')
def hover_signed_in_icon(context):
    context.app.signin.hover_signed_in_icon()


@then('Verify user is signed in')
def verify_user_signed_in(context):
    context.app.signin.verify_user_signed_in()