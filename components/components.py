from selenium.webdriver.common.by import By

from pages.elements_page import ElementsPage


class WedElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def visible(self):
        return self.find_element().is_displayed()