from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_tab():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demoqa.com/links")
        home_link = driver.find_element(By.ID, "simpleLink")

        assert home_link.text == "Home"
        assert "demoqa.com" in home_link.get_attribute("href")

        original = driver.current_window_handle
        home_link.click()

        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window([w for w in driver.window_handles if w != original][0])
        print(f"Новая вкладка: {driver.current_url}")

    finally:
        driver.quit()


test_tab()