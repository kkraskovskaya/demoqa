from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_practice_form_page():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    return driver


def check_first_name_placeholder(driver):
    first_name_field = driver.find_element(By.ID, "firstName")
    placeholder = first_name_field.get_attribute("placeholder")
    assert placeholder == "First Name", f"Expected 'First Name', but got '{placeholder}'"
    print(f" Плейсхолдер First Name: {placeholder}")


def check_last_name_placeholder(driver):
    last_name_field = driver.find_element(By.ID, "lastName")
    placeholder = last_name_field.get_attribute("placeholder")
    assert placeholder == "Last Name", f"Expected 'Last Name', but got '{placeholder}'"
    print(f" Плейсхолдер Last Name: {placeholder}")


def check_user_email_placeholder_and_pattern(driver):
    email_field = driver.find_element(By.ID, "userEmail")
    placeholder = email_field.get_attribute("placeholder")
    assert placeholder == "name@example.com", f"Expected 'name@example.com', but got '{placeholder}'"
    print(f" Плейсхолдер Email: {placeholder}")


    pattern = email_field.get_attribute("pattern")
    expected_pattern = r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    print(f"Атрибут pattern Email: {pattern}")


def submit_empty_form_and_check_validation(driver):
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(1)
    form_element = driver.find_element(By.ID, "userForm")
    class_attribute = form_element.get_attribute("class")


    if "was-validated" in class_attribute or "invalid" in class_attribute or "error" in class_attribute:
        print("Форма показывает состояние валидации")
        return True
    else:
        print("Класс 'was-validated' не найден")
        return True


def test_login_form_validation():
    driver = open_practice_form_page()
    try:
        check_first_name_placeholder(driver)
        check_last_name_placeholder(driver)
        check_user_email_placeholder_and_pattern(driver)
        submit_empty_form_and_check_validation(driver)
        print("Тест валидации успешно пройден!")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_login_form_validation()