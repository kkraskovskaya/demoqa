from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def open_practice_form():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    return driver


def fill_state_and_city(driver, state_name="NCR", city_name="Delhi"):
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)


    state_dropdown = driver.find_element(By.ID, "state")
    driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
    state_dropdown.click()
    time.sleep(1)


    state_option = driver.find_element(By.XPATH, f"//div[text()='{state_name}']")
    state_option.click()

    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()
    time.sleep(1)

    city_option = driver.find_element(By.XPATH, f"//div[text()='{city_name}']")
    city_option.click()

    print(f" Выбраны State: {state_name}, City: {city_name}")


def verify_state_and_city_selection(driver, expected_state="NCR", expected_city="Delhi"):

    state_element = driver.find_element(By.CSS_SELECTOR, "#state .css-1uccc91-singleValue")
    selected_state = state_element.text

    city_element = driver.find_element(By.CSS_SELECTOR, "#city .css-1uccc91-singleValue")
    selected_city = city_element.text


    assert selected_state == expected_state, f"Expected state '{expected_state}', but got '{selected_state}'"
    assert selected_city == expected_city, f"Expected city '{expected_city}', but got '{selected_city}'"

    print(f" Проверка пройдена: State='{selected_state}', City='{selected_city}'")


def test_state_and_city_fill():
    driver = open_practice_form()
    try:
        fill_state_and_city(driver)
        verify_state_and_city_selection(driver)
        print("Тест заполнения State и City успешно пройден!")
        time.sleep(2)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_state_and_city_fill()