from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModalDialogsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/modal-dialogs"
        self.modal_buttons = (By.XPATH, "//button[contains(text(), 'Modal')]")
        self.home_icon = (By.CSS_SELECTOR, "header a img")

    def open(self):
        self.driver.get(self.url)
        return self

    def get_modal_buttons_count(self):
        buttons = self.driver.find_elements(*self.modal_buttons)
        return len(buttons)

    def click_home_icon(self):
        home_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.home_icon)
        )
        home_icon.click()

    def refresh_page(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def set_default_window_size(self):
        self.driver.set_window_size(1000, 1000)