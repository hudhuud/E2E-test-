import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Открытие браузера с интерфейсом для отладки
    page = browser.new_page()

    # Переход на сайт
    page.goto("https://www.saucedemo.com/")

    # Авторизация
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')

    # Выбор товара
    page.click('#add-to-cart-sauce-labs-backpack')

    # Переход в корзину
    page.click('.shopping_cart_link')

    # Проверка, что товар добавлен
    assert "Sauce Labs Backpack" in page.inner_text('.cart_item')

    # Оформление покупки
    page.click('#checkout')
    page.fill('#first-name', 'Test')
    page.fill('#last-name', 'User')
    page.fill('#postal-code', '12345')
    page.click('#continue')

    # Завершение покупки
    page.click('#finish')

    # Ожидание появления элемента с сообщением о завершении заказа
    page.wait_for_selector('.complete-header')

    # Получаем текст сообщения
    success_message = page.inner_text('.complete-header').strip()

    # Выводим сообщение для отладки
    print(f"Success message: {success_message}")

    # Приведение строк к нижнему регистру для сравнения
    assert success_message.lower() == "thank you for your order!".lower(), f"Expected 'THANK YOU FOR YOUR ORDER', but got '{success_message}'"

    print("Тест успешно завершен!")

    # Задержка перед закрытием браузера
    time.sleep(10)

    # Закрытие браузера
    browser.close()
