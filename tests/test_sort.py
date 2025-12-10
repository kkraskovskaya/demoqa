from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_table_sorting_short():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")

    headers = driver.find_elements(By.CSS_SELECTOR, ".rt-resizable-header-content")[:-1]

    for header in headers:
        name = header.text
        parent = header.find_element(By.XPATH, "./..")


        header.click()
        time.sleep(0.3)
        class1 = parent.get_attribute("class")
        assert any(marker in class1 for marker in ['sort', 'asc', 'desc']), \
            f"Сортировка не активирована для '{name}'"


        header.click()
        time.sleep(0.3)
        class2 = parent.get_attribute("class")
        assert class1 != class2, f"Направление не изменилось для '{name}'"

        print(f" {name}: сортировка работает")

    print("\n Все проверки пройдены!")
    driver.quit()


if __name__ == "__main__":
    test_table_sorting_short()