from components.components import WedElement
from pages.base_page import BasePage


class FromPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WedElement(driver, '#firstName')
        self.last_name = WedElement(driver, '#lastName')
        self.user_email = WedElement(driver, '#userEmail')
        self.gender_radio_1 = WedElement(driver, '#gender-radio-1')
        self.user_number = WedElement(driver, '#userNumber')
        self.btn_submit = WedElement(driver, '#submit')
        self.model_dialog = WedElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_model = WedElement(driver, '#closeLargeModal')
