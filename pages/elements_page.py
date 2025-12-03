from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div.col-12:nth-child(2)')
        self.icon = WebElement(driver, 'header > a > ing')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #iten-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver,'div:nth-child(1) > div > ul > #iten-1 > span')
