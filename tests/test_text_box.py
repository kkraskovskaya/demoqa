from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_browser_and_go_to_url():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    return driver


def fill_text_box_fields(driver, full_name, current_address):
    driver.find_element(By.ID, "userName").send_keys(full_name)
    driver.find_element(By.ID, "currentAddress").send_keys(current_address)


def click_submit_button(driver):
    driver.find_element(By.ID, "submit").click()


def check_output_elements(driver, full_name, current_address):
    time.sleep(1)
    name_output = driver.find_element(By.ID, "name").text
    address_output = driver.find_element(By.ID, "currentAddress").text


    assert full_name in name_output, f"Expected '{full_name}' in output, but got '{name_output}'"
    assert current_address in address_output, f"Expected '{current_address}' in output, but got '{address_output}'"

    print("Текст успешно отображен в выходных элементах")


def test_text_box():
    test_full_name = "Иван Иванов"
    test_current_address = "Москва, ул. Тестовая, д. 1"

    driver = open_browser_and_go_to_url()
    try:
        fill_text_box_fields(driver, test_full_name, test_current_address)
        click_submit_button(driver)
        check_output_elements(driver, test_full_name, test_current_address)
        print("Тест успешно пройден!")
    finally:
        driver.quit()



if __name__ == "__main__":
    test_text_box()