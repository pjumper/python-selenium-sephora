from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class NewHeader(Page):

    JUST_DROPPED_LINK = (By.CSS_SELECTOR, "a[href='/beauty/new-releases']")
    VERIFY_JUST_DROPPED_TEXT = (By.CSS_SELECTOR, ".css-r5gry1[href*='_new_just_dropped']")
    HOLIDAY_GUIDE_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href='/beauty/new-beauty-products']")
    VERIFY_GIFT_GUIDE_TEXT = (By.CSS_SELECTOR, ".css-1nol3g4 [href*='/beauty/holiday-sale?icid2=holiday']")
    ALL_NEW_LINK = (By.CSS_SELECTOR, ".css-1kczxm6 a[href='/beauty/new-beauty-products']")
    VERIFY_ALL_NEW_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    NEXT_BIG_THING_LINK = (By.CSS_SELECTOR, "#top_nav_drop_0 [href*='next-big-thing']")
    VERIFY_NEXT_BIG_THING_TEXT = (By.CSS_SELECTOR, ".css-1nol3g4 [href*='/beauty/next-big-thing']")
    BESTSELLER_LINK = (By.CSS_SELECTOR, "[href='/beauty/beauty-best-sellers']")
    VERIFY_BESTSELLER_TEXT = (By.CSS_SELECTOR, ".css-4hl9ti")
    TRENDING_SOCIAL_LINK = (By.CSS_SELECTOR, "[href='/beauty/trending-at-sephora']")
    VERIFY_TRENDING_SOCIAL_TEXT = (By.CSS_SELECTOR, ".css-1nol3g4 [href*='/beauty/trending-at-sephora']")
    def click_all_new_link(self, *locator):
        self.click(*self.ALL_NEW_LINK)

    def click_just_dropped_link(self, *locator):
        self.click(*self.JUST_DROPPED_LINK)

    def click_holiday_gift_guide_link(self, *locator):
        self.click(*self.HOLIDAY_GUIDE_LINK)

    def click_next_big_thing_link(self, *locator):
        self.click(*self.NEXT_BIG_THING_LINK)

    def click_bestseller_link(self, *locator):
        self.click(*self.BESTSELLER_LINK)

    def click_trending_social_link(self, *locator):
        self.click(*self.TRENDING_SOCIAL_LINK)

    def verify_all_new_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_ALL_NEW_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def verify_just_dropped_page_opened(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_JUST_DROPPED_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def verify_holiday_gift_guide_page_opened(self, expected_text):
        actual_results = self.find_element(*self.VERIFY_GIFT_GUIDE_TEXT).text
        assert actual_results == expected_text, f'Expected{expected_text} but got {actual_results}'

    def verify_next_big_thing_link(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_NEXT_BIG_THING_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def verify_bestseller_link(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_BESTSELLER_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'

    def verify_trending_social_page_present(self, expected_text):
        actual_result = self.find_element(*self.VERIFY_TRENDING_SOCIAL_TEXT).text
        assert actual_result == expected_text, f'Expected {expected_text} but got {actual_result}'
