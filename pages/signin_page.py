from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class Signin(Page):

    SIGNIN_HEADER = (By.CSS_SELECTOR, ".css-shwact")
    SIGNIN_EMAIL = (By.ID, "signin_username")
    SIGNIN_BTTN = (By.CSS_SELECTOR, ".css-1hea53j .css-1tb8cer")
    SIGNIN_PASSWORD = (By.ID, "signin_password")
    SIGNIN_POPUP_BTTN = (By.CSS_SELECTOR, ".css-1t1hir4")
    VERIFY_USER_SIGNED_IN = (By.CSS_SELECTOR, "button.css-nar1z4")
    HOVER_SIGNED_IN_ICON = (By.ID, "account_drop_trigger")

    def hover_signin(self):
        hover_signin = self.find_element(*self.SIGNIN_HEADER)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_signin)
        actions.perform()
    def hover_signed_in_icon(self):
        hover_signed_in_icon = self.find_element(*self.HOVER_SIGNED_IN_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_signed_in_icon)
        actions.perform()

    def click_signin(self, *locator):
        self.click(*self.SIGNIN_BTTN)

    def click_signin_bttn(self, *locator):
        self.click(*self.SIGNIN_BTTN)

    def click_signin_popup_bttn(self, *locator):
        self.click(*self.SIGNIN_POPUP_BTTN)

    def input_signin_email(self, text):
        self.input_text(text,*self.SIGNIN_EMAIL)

    def input_signin_password(self, text):
        self.input_text(text,*self.SIGNIN_PASSWORD)

    def verify_user_signed_in(self, *locator):
        self.wait_for_element_to_appear(*self.VERIFY_USER_SIGNED_IN)


