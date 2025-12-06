from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_sort():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demoqa.com/webtables")

        headers = driver.find_elements(By.CSS_SELECTOR, ".rt-th:not(:last-child)")
        for header in headers:
            header.click()
            if "sort" in header.get_attribute("class"):
                print(f"Сортировка {header.text} - OK")

    finally:
        driver.quit()


test_sort()