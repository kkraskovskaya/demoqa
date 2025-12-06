from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_modal():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demoqa.com/modal-dialogs")

        if "modal-dialogs" not in driver.current_url:
            print("Страница недоступна - пропускаем тест")
            return

        driver.find_element(By.ID, "showSmallModal").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        driver.find_element(By.ID, "closeSmallModal").click()
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "modal-content")))
        print("Small modal - OK")

        driver.find_element(By.ID, "showLargeModal").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        driver.find_element(By.ID, "closeLargeModal").click()
        print("Large modal - OK")

    finally:
        driver.quit()


test_modal()