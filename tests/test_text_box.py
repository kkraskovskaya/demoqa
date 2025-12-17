from selenium.webdriver.common.by import By


def test_text_box_submission(driver):
    driver.get("https://demoqa.com/text-box")


    test_name = "Иван Иванов"
    test_address = "Москва, ул. Тестовая, д. 1"
    driver.find_element(By.ID, "userName").send_keys(test_name)
    driver.find_element(By.ID, "currentAddress").send_keys(test_address)


    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()


    name_output = driver.find_element(By.ID, "name").text
    address_output = driver.find_element(By.ID, "currentAddress").text

    assert test_name in name_output, f"Имя '{test_name}' не найдено"
    assert test_address in address_output, f"Адрес '{test_address}' не найден"