import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.accordion import AccordionPage


class TestAccordionVisibility(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.accordion_page = AccordionPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_visible_accordion(self):

        self.accordion_page.open()

        content = self.driver.find_element(*self.accordion_page.section1_content)
        self.assertTrue(content.is_displayed(), "Элемент должен быть виден")

        self.driver.find_element(*self.accordion_page.section1_heading).click()
        time.sleep(2)
        self.assertFalse(content.is_displayed(), "Элемент должен быть скрыт")

    def test_visible_accordion_default(self):

        self.accordion_page.open()
        elements = [
            self.accordion_page.section2_content_p1,
            self.accordion_page.section2_content_p2,
            self.accordion_page.section3_content
        ]

        for locator in elements:
            element = self.driver.find_element(*locator)
            self.assertFalse(element.is_displayed(), f"Элемент {locator} должен быть скрыт")


if __name__ == "__main__":
    unittest.main()