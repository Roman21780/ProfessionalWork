from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Tests.config import yandex_login, yandex_password, yandex_phone  # Импортируем данные из конфига

# Константы
TIMEOUT = 120
SELECTORS = {
    "phone_field": 'input#passp-field-phone',  # Поле ввода телефона
    "enter_button": 'button[data-t="button:action:passp:sign-in"]',  # Кнопка "Войти"
    "login_field": 'input[name="login"]',
    "password_field": 'input[name="passwd"]',
    "submit_button": 'button[data-t="button:action"], #passp:sign-in',
}


@pytest.fixture
def browser():
    """Fixture для инициализации браузера."""
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def input_text(browser, selector, text, timeout=TIMEOUT):
    """Вводит текст в поле после его появления."""
    field = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )
    field.clear()
    field.send_keys(text)


def click_element(browser, selector, timeout=TIMEOUT):
    """Кликает по элементу после его появления."""
    element = WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    element.click()


def test_yandex_auth(browser):
    """Тест авторизации на Яндексе."""
    browser.get("https://passport.yandex.ru/auth/")

    try:
        # 1. Проверяем, запрашивается ли телефон
        try:
            print("Ожидание поля ввода телефона...")
            phone_field = WebDriverWait(browser, TIMEOUT).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, SELECTORS["phone_field"]))
            )
            print("Поле ввода телефона найдено. Вводим номер...")
            input_text(browser, SELECTORS["phone_field"], yandex_phone)  # Убираем "+7" из номера

            # Нажимаем кнопку "Войти"
            print("Нажимаем кнопку 'Войти'...")
            click_element(browser, SELECTORS["enter_button"])
        except Exception as e:
            print(f"Поле ввода телефона не найдено: {str(e)}")

        # 2. Вводим логин
        print("Вводим логин...")
        input_text(browser, SELECTORS["login_field"], yandex_login)
        click_element(browser, SELECTORS["submit_button"])

        # 3. Вводим пароль
        print("Вводим пароль...")
        input_text(browser, SELECTORS["password_field"], yandex_password)
        click_element(browser, SELECTORS["submit_button"])

        # 4. Проверяем успешный вход
        print("Проверяем успешный вход...")
        WebDriverWait(browser, TIMEOUT).until(
            lambda d: any(x in d.current_url.lower() for x in ["profile", "welcome", "id.yandex.ru"])
        )
        print("Авторизация прошла успешно!")

    except Exception as e:
        # Сохранение скриншота при ошибке
        browser.save_screenshot("yandex_auth_error.png")
        print(f"Ошибка: {str(e)}")
        raise