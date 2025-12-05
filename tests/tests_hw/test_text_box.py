from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/text-box")

name, address = "Иван Иванов", "ул. Примерная, 123"

driver.find_element(By.ID, "userName").send_keys(name)
driver.find_element(By.ID, "currentAddress").send_keys(address)
driver.find_element(By.ID, "submit").click()

assert name in driver.find_element(By.ID, "name").text
assert address in driver.find_element(By.ID, "currentAddress").text

print("✓ Тест пройден")
driver.quit()