from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Header(Page):

    MAIN_HEADER_LINKS = (By.CSS_SELECTOR, "nav[data-at='cat_nav'] div[data-comp*='TopNavItem']")
    NEW_HEADER_LINK = (By.CSS_SELECTOR, "a[aria-controls='top_nav_drop_0']")
    NEW_PAGE_LINKS = (By.CSS_SELECTOR, ".css-c8e0cz li a")
    JUST_DROPPED_LINK = (By.CSS_SELECTOR, ".fresnel-lessThan-md  a[href*='new_just_dropped']")

    def verify_main_header_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_result = self.find_elements(*self.MAIN_HEADER_LINKS)
        assert len(actual_result) == expected_amount, f'Expected {expected_amount} but got {len(actual_result)}'

    def click_new_header_link(self, *locator):
        # self.wait_for_element_click(*self.NEW_HEADER_LINK)
        self.click(*self.NEW_HEADER_LINK)

    def click_just_dropped_link(self, *locator):
        self.click(*self.JUST_DROPPED_LINK)

    def verify_new_dropdown_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_results = self.find_elements(*self.NEW_PAGE_LINKS)
        assert len(actual_results) == expected_amount, f'Expected {expected_amount} but got {len(actual_results)}'
