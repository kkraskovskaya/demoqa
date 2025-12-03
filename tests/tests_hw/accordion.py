from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccordionPage(BasePage):
    url = "https://demoqa.com/accordian"

    section1_content = (By.CSS_SELECTOR, "#section1Content > p")
    section1_heading = (By.CSS_SELECTOR, "#section1Heading")

    section2_content_p1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    section2_content_p2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
    section3_content = (By.CSS_SELECTOR, "#section3Content > p")