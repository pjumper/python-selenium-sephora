from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):



    def open_home(self):
        self.open_url('https://www.sephora.com/')


