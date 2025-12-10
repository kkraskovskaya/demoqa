from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_dialogs():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/modal-dialogs")
    driver.maximize_window()


    modals = [
        ("Small modal", "showSmallModal"),
        ("Large modal", "showLargeModal")
    ]

    for modal_name, button_id in modals:
        print(f"Тестируем {modal_name}...")


        driver.find_element(By.ID, button_id).click()


        modal_content = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        assert modal_content.is_displayed(), f"{modal_name} не открылось"
        print(f"✓ {modal_name} открыто")


        driver.find_element(By.CLASS_NAME, "close").click()
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        print(f"✓ {modal_name} закрыто")

    print("\n Все тесты модальных окон пройдены!")
    driver.quit()


if __name__ == "__main__":
    test_modal_dialogs()