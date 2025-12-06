from pages.base_page import BasePage
from components.components import WedElement


class AlertsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super.alertButton = WedElement(driver, '#alertButton')
