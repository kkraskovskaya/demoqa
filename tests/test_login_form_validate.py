from selenium.webdriver.common.by import By


def test_form_placeholders(driver):
    driver.get("https://demoqa.com/automation-practice-form")


    first_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "userEmail")

    assert first_name.get_attribute("placeholder") == "First Name"
    assert last_name.get_attribute("placeholder") == "Last Name"
    assert email.get_attribute("placeholder") == "name@example.com"


    pattern = email.get_attribute("pattern")
    assert pattern is not None
    assert pattern != ""


def test_empty_form_validation(driver):
    driver.get("https://demoqa.com/automation-practice-form")

    form = driver.find_element(By.ID, "userForm")
    submit_btn = driver.find_element(By.ID, "submit")


    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()


    assert "was-validated" in form.get_attribute("class")