from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Header(Page):

    MAIN_HEADER_LINKS = (By.CSS_SELECTOR, "nav[data-at='cat_nav'] div[data-comp*='TopNavItem']")
    NEW_HEADER_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0_trigger")
    NEW_HEADER_LINKS = (By.CSS_SELECTOR, "#top_nav_drop_0 .css-1kczxm6 a")
    NEW_PAGE_LINKS = (By.CSS_SELECTOR, ".css-c8e0cz .fresnel-lessThan-md")
    MAKEUP_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href='/beauty/new-makeup']")
    VERIFY_MAKEUP_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_SKIN_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='/beauty/new-skin']")
    VERIFY_NEW_SKIN_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_HAIRCARE_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='/beauty/new-hair']")
    VERIFY_NEW_HAIRCARE_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_FRAGRANCE_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href='/beauty/new-perfumes']")
    VERIFY_NEW_FRAGRANCE_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_BATH_BODY_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='new-body-products']")
    VERIFY_NEW_BATH_BODY_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEW_TOOLS_BRUSHES_PAGE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='new-beauty-tools']")
    VERIFY_NEW_TOOLS_BRUSHES_PAGE_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    BRAND_HEADER_LINKS = (By.CSS_SELECTOR, "#top_nav_drop_1 .css-1kczxm6 a")
    def verify_main_header_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_result = self.find_elements(*self.MAIN_HEADER_LINKS)
        assert len(actual_result) == expected_amount, f'Expected {expected_amount} but got {len(actual_result)}'


    def verify_new_dropdown_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_results = self.find_elements(*self.NEW_PAGE_LINKS)
        assert len(actual_results) == expected_amount, f'Expected {expected_amount} but got {len(actual_results)}'

    def verify_new_header_dropdown_links(self, *locator, expected_amount):
        expected_amount = int(expected_amount)
        actual_results = self.find_elements(*self.NEW_HEADER_LINKS)
        assert len(actual_results) == expected_amount, f'Expected {expected_amount} but got {len(actual_results)}'

    def hover_new_header_link(self):
        new_header_link = self.find_element(*self.NEW_HEADER_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_header_link)
        actions.perform()


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

    def click_new_haircare_link(self, *locator):
        self.click(*self.NEW_HAIRCARE_PAGE_LINK)

    def verify_new_haircare_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEW_HAIRCARE_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def click_new_fragrance_link(self, *locator):
        self.click(*self.NEW_FRAGRANCE_PAGE_LINK)

    def verify_new_fragrance_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEW_FRAGRANCE_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def click_new_bath_body_link(self, *locator):
        self.click(*self.NEW_BATH_BODY_PAGE_LINK)

    def verify_new_bath_body_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEW_BATH_BODY_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def click_new_tools_brushes_link(self, *locator):
        self.click(*self.NEW_TOOLS_BRUSHES_PAGE_LINK)

    def verify_new_tools_brushes_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEW_TOOLS_BRUSHES_PAGE_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'