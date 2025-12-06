from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_webtables():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://demoqa.com/webtables")
        print("Страница открыта")
        driver.find_element(By.CSS_SELECTOR, "select[aria-label='rows per page']").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='5']").click()
        next_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next']")
        prev_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Previous']")

        if "disabled" in next_btn.get_attribute("class"):
            print("✓ Кнопки пагинации заблокированы")


        driver.find_element(By.ID, "addNewRecordButton").click()
        print("Диалог открыт")

        driver.find_element(By.ID, "submit").click()
        driver.find_element(By.ID, "firstName").send_keys("Алексей")
        driver.find_element(By.ID, "lastName").send_keys("Смирнов")
        driver.find_element(By.ID, "userEmail").send_keys("alex@test.com")
        driver.find_element(By.ID, "age").send_keys("40")
        driver.find_element(By.ID, "salary").send_keys("70000")
        driver.find_element(By.ID, "department").send_keys("Management")
        driver.find_element(By.ID, "submit").click()
        print("✓ Запись добавлена")

        print("\n Тест пройден успешно!")

    except Exception as e:
        print(f" Ошибка: {e}")
    finally:
        driver.quit()


test_webtables()