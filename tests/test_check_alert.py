from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_timer_alert():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/alerts")

    try:
        print("Нажимаем кнопку для вызова алерта через 5 секунд...")


        start_time = time.time()


        driver.find_element(By.ID, "timerAlertButton").click()


        alert = WebDriverWait(driver, 6).until(EC.alert_is_present())


        elapsed_time = time.time() - start_time
        print(f"Алерт появился через {elapsed_time:.1f} секунд")


        assert elapsed_time >= 4.5, f"Алерт появился слишком быстро: {elapsed_time:.1f} секунд"

        assert elapsed_time <= 6.0, f"Алерт появился слишком поздно: {elapsed_time:.1f} секунд"

        alert_text = alert.text
        print(f"Текст алерта: '{alert_text}'")


        alert.accept()
        print("✓ Алерт успешно закрыт")

        print("Тест алерта пройден успешно!")

    except Exception as e:
        print(f"Ошибка в тесте: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    test_timer_alert()