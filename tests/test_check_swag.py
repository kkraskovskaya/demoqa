import pytest
from selenium.webdriver.common.by import By
from pages.swag_labs import SwagLabs


def test_check_icon(browser):

    """Тест-кейс: Проверка наличия иконки
    1. Перейти на страницу https://www.saucedemo.com/
    2. Проверить наличие иконки"""


    page = SwagLabs(browser)
    page.visit()
    assert page.exist_icon() == True, "Иконка не найдена на странице"

    print("Тест пройден: Иконка найдена")



def test_check_username_field(browser):

    """Тест-кейс: Проверка наличия поля имени
    1. Перейти на страницу https://www.saucedemo.com/
    2. Проверить наличие поля имени"""


    page = SwagLabs(browser)
    page.visit()
    username_field = page.find_element((By.ID, "user-name"))

    assert username_field is not None, "Поле имени не найдено"
    assert username_field.is_displayed(), "Поле имени не отображается"

    print("Тест пройден: Поле имени найдено")


def test_check_password_field(browser):

    """Тест-кейс: Проверка наличия поля пароля
    1. Перейти на страницу https://www.saucedemo.com/
    2. Проверить наличие поля пароля"""


    page = SwagLabs(browser)
    page.visit()
    password_field = page.find_element((By.ID, "password"))

    assert password_field is not None, "Поле пароля не найдено"
    assert password_field.is_displayed(), "Поле пароля не отображается"

    print(" Тест пройден: Поле пароля найдено")