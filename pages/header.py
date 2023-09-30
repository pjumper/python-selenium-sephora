from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    Main_Header_Links = (By.CSS_SELECTOR, "nav[data-at='cat_nav'] div[data-comp*='TopNavItem']")

    def verify_main_header_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_results = self.find_elements(*self.Main_Header_Links)
        assert len(actual_results) == expected_amount, f"Expected {expected_amount} but got {len(actual_results)}"

