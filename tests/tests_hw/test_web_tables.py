from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_web_tables_short():
    print("ТЕСТ Web Tables")

    data = {"first_name": "Анна", "last_name": "Иванова", "email": "anna@test.com",
            "age": "25", "salary": "50000", "department": "QA"}
    new_name = "Мария"

    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")

    try:
        driver.find_element(By.ID, "addNewRecordButton").click()
        time.sleep(1)

        driver.find_element(By.ID, "submit").click()
        time.sleep(1)
        assert driver.find_element(By.CLASS_NAME, "modal-title").is_displayed()
        print(" Пустая форма не сохраняется")

        for field, value in data.items():
            driver.find_element(By.ID, field).send_keys(value)
        driver.find_element(By.ID, "submit").click()
        time.sleep(1)
        print(" Форма сохранена")


        table_text = driver.find_element(By.CLASS_NAME, "rt-tbody").text
        for value in data.values():
            assert value in table_text
        print(" Данные в таблице")

        rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        for row in rows:
            if data["first_name"] in row.text:
                row.find_element(By.CSS_SELECTOR, "span[title='Edit']").click()
                break
        time.sleep(1)

        driver.find_element(By.ID, "firstName").clear()
        driver.find_element(By.ID, "firstName").send_keys(new_name)
        driver.find_element(By.ID, "submit").click()
        time.sleep(1)
        print(f" Имя изменено на {new_name}")

        rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        for row in rows:
            if new_name in row.text:
                row.find_element(By.CSS_SELECTOR, "span[title='Delete']").click()
                break
        time.sleep(1)

        table_text = driver.find_element(By.CLASS_NAME, "rt-tbody").text
        assert new_name not in table_text
        print(" Запись удалена")

        print("\nТЕСТ УСПЕШНО ЗАВЕРШЕН!")

    except Exception as e:
        print(f"\nОШИБКА: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_web_tables_short()