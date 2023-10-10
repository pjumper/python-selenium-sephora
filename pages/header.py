from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Header(Page):

    MAIN_HEADER_LINKS = (By.CSS_SELECTOR, "nav[data-at='cat_nav'] div[data-comp*='TopNavItem']")
    NEW_HEADER_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0_trigger")
    ALL_NEW_LINK = (By.CSS_SELECTOR, ".css-1kczxm6 a[href='/beauty/new-beauty-products']")
    NEW_PAGE_LINKS = (By.CSS_SELECTOR, ".css-c8e0cz .fresnel-lessThan-md")
    JUST_DROPPED_LINK = (By.CSS_SELECTOR, "a[href='/beauty/new-releases']")
    VERIFY_JUST_DROPPED_TEXT = (By.CSS_SELECTOR, ".css-r5gry1[href*='_new_just_dropped']")
    MAKEUP_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href='/beauty/new-makeup']")
    VERIFY_MAKEUP_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_SKIN_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='/beauty/new-skin']")
    VERIFY_NEW_SKIN_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")

    def verify_main_header_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_result = self.find_elements(*self.MAIN_HEADER_LINKS)
        assert len(actual_result) == expected_amount, f'Expected {expected_amount} but got {len(actual_result)}'

    def click_new_header_link(self, *locator):
        # self.wait_for_element_click(*self.NEW_HEADER_LINK)
        self.click(*self.ALL_NEW_LINK)

    def click_just_dropped_link(self, *locator):
        self.click(*self.JUST_DROPPED_LINK)

    def verify_new_dropdown_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_results = self.find_elements(*self.NEW_PAGE_LINKS)
        assert len(actual_results) == expected_amount, f'Expected {expected_amount} but got {len(actual_results)}'

    def hover_new_header_link(self):
        new_header_link = self.find_element(*self.NEW_HEADER_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_header_link)
        actions.perform()

    def verify_just_dropped_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_JUST_DROPPED_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def click_makeup_page_link(self, *locator):
        self.click(*self.MAKEUP_PAGE_LINK)


    def verify_makeup_page_link_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_MAKEUP_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'


    def click_new_skin_link(self, *locator):
        self.click(*self.NEW_SKIN_PAGE_LINK)


    def verify_new_skin_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEW_SKIN_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'
