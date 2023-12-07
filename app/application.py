from pages.main_page import MainPage
from pages.header import Header
from pages.new_header import NewHeader
from pages.signin_page import Signin

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.new_header = NewHeader(self.driver)
        self.signin = Signin(self.driver)
