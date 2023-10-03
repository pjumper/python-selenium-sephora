from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self,url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, *locator):
        self.driver.find_element(*locator).text()

    def wait_for_element_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        # e.click()

    def wait_for_element_to_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_disappear(self, *locator):
        return self.wait.until(EC.invisibility_of_element(locator))

    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))

    def wait_for_visibility_of_element(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_text_to_be_present(self, *locator):
        self.wait.until(EC.text_to_be_present_in_element(locator))

    def wait_for_elements_to_appear(self, *locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))


