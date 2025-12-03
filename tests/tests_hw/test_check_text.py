import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tests_hw.components import Component


class TestDemoQAText(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_footer_text(self):

        self.driver.get("https://demoqa.com/")

        footer_locator = (By.XPATH, "//footer//span")
        footer_component = Component(self.driver, footer_locator)

        actual_text = footer_component.get_text()
        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

        self.assertEqual(actual_text, expected_text,
                         f"Текст в подвале не совпадает. Ожидалось: {expected_text}, Получено: {actual_text}")
        print(f"✓ Тест 1 пройден: текст в подвале корректный")

    def test_center_text_on_elements_page(self):

        self.driver.get("https://demoqa.com/")
        elements_button = self.driver.find_element(By.XPATH, "//div[contains(@class,'card')]//h5[text()='Elements']")
        elements_button.click()

        current_url = self.driver.current_url
        self.assertIn("elements", current_url.lower(), "Не удалось перейти на страницу Elements")

        center_text_locator = (By.CLASS_NAME, "col-md-6")
        center_component = Component(self.driver, center_text_locator)

        actual_text = center_component.get_text().strip()
        expected_text = 'Please select an item from left to start practice.'

        self.assertEqual(actual_text, expected_text,
                         f"Текст по центру не совпадает. Ожидалось: {expected_text}, Получено: {actual_text}")
        print(f"✓ Тест 2 пройден: текст на странице Elements корректный")



if __name__ == "__main__":
    unittest.main()