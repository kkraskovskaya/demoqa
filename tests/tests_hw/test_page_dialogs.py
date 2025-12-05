import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.modal_dialogs import ModalDialogsPage


class TestModalDialogs:
    @pytest.fixture(autouse=True)
    def setup(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.set_window_size(1000, 1000)
        yield
        self.driver.quit()

    def test_modal_elements(self):

        modal_page = ModalDialogsPage(self.driver)
        modal_page.open()
        buttons_count = modal_page.get_modal_buttons_count()
        expected_count = 5

        print(f"Найдено кнопок: {buttons_count}")
        print(f"Ожидалось кнопок: {expected_count}")

        assert buttons_count == expected_count, \
            f"Количество кнопок не совпадает: {buttons_count} вместо {expected_count}"

        print("✓ Тест test_modal_elements пройден успешно")

    def test_navigation_modal(self):
        modal_page = ModalDialogsPage(self.driver)
        modal_page.open()
        modal_page.refresh_page()
        print("Страница обновлена")


        modal_page.click_home_icon()
        print("Перешли на главную страницу через иконку")

        modal_page.go_back()
        print("Шаг назад - вернулись на modal-dialogs")

        modal_page.set_window_size(900, 400)
        print("Установлен размер окна: 900x400")

        modal_page.go_forward()
        print("Шаг вперед - вернулись на главную страницу")

        current_url = modal_page.get_current_url()
        expected_home_url = "https://demoqa.com/"

        print(f"Текущий URL: {current_url}")
        print(f"Ожидаемый URL главной: {expected_home_url}")

        assert expected_home_url in current_url, \
            f"URL не соответствует главной странице: {current_url}"

        page_title = modal_page.get_page_title()
        expected_title = "DEMOQA"

        print(f"Заголовок страницы: {page_title}")
        print(f"Ожидаемый заголовок: {expected_title}")

        assert expected_title in page_title, \
            f"Заголовок страницы не содержит '{expected_title}'"

        modal_page.set_default_window_size()
        print("Восстановлен размер окна: 1000x1000")

        print("✓ Тест test_navigation_modal пройден успешно")


if __name__ == "__main__":
    test = TestModalDialogs()

    print("Запуск test_modal_elements...")
    test.setup()
    test.test_modal_elements()
    test.driver.quit()

    print("\n" + "=" * 50 + "\n")

    print("Запуск test_navigation_modal...")
    test.setup()
    test.test_navigation_modal()
    test.driver.quit()