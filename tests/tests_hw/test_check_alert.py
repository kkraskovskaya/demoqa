from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_alert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demoqa.com/alerts")
        driver.find_element(By.ID, "timerAlertButton").click()

        WebDriverWait(driver, 10).until(lambda d: d.switch_to.alert)
        alert = driver.switch_to.alert
        print(f"Alert текст: {alert.text}")
        alert.accept()

    finally:
        driver.quit()


test_alert()