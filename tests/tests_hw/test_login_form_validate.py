from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

assert driver.find_element(By.ID, "firstName").get_attribute("placeholder") == "First Name"
assert driver.find_element(By.ID, "lastName").get_attribute("placeholder") == "Last Name"
assert driver.find_element(By.ID, "userEmail").get_attribute("placeholder") == "name@example.com"
assert driver.find_element(By.ID, "userEmail").get_attribute("pattern") is not None

driver.find_element(By.ID, "submit").click()
assert "was-validated" in driver.find_element(By.ID, "userForm").get_attribute("class")

print("✓ Тест пройден")
driver.quit()