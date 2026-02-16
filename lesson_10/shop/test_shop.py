"""
Тестовый модуль для проверки сценария покупки в интернет-магазине Saucedemo.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lesson_10.shop.LoginPage import LoginPage
import allure
import time


@allure.feature("Покупка товаров")
@allure.story("Полный цикл покупки")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест полного цикла покупки трех товаров")
@allure.description("""
    Тест проверяет полный сценарий покупки трех товаров:
    1. Авторизация на сайте
    2. Добавление трех товаров в корзину
    3. Переход в корзину
    4. Оформление заказа с тестовыми данными
    5. Проверка итоговой суммы
""")
def test_saucedemo_purchase_robust(driver):
    """
    Тест полного цикла покупки товаров в интернет-магазине.
    """
    
    # Тестовые данные
    username = "standard_user"
    password = "secret_sauce"
    first_name = "John"
    last_name = "Doe"
    postal_code = "12345"
    expected_total = 58.29
    
    try:
        with allure.step("1. Открытие сайта и авторизация"):
            login_page = LoginPage(driver)
            login_page.open()
            
            time.sleep(1)
            
            inventory_page = (login_page
                             .enter_username(username)
                             .enter_password(password)
                             .click_login())
            
            inventory_page.wait_for_page_load()
        
        with allure.step("2. Диагностика - доступные товары на странице"):
            available_items = inventory_page.get_all_inventory_items()
            allure.attach("\n".join(available_items), name="Список доступных товаров", 
                         attachment_type=allure.attachment_type.TEXT)
            
            # Проверяем наличие нужных товаров
            expected_items = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
            for item in expected_items:
                assert item in available_items, f"Товар {item} не найден на странице!"
        
        with allure.step("3. Добавление товаров в корзину"):
            # Добавляем товары с проверкой каждого шага
            inventory_page.add_backpack_to_cart()
            time.sleep(0.5)
            
            # Проверяем промежуточное состояние
            count_after_first = inventory_page.get_cart_items_count()
            allure.attach(f"После первого товара: {count_after_first}", 
                         name="Промежуточная проверка", attachment_type=allure.attachment_type.TEXT)
            
            inventory_page.add_bolt_tshirt_to_cart()
            time.sleep(0.5)
            
            count_after_second = inventory_page.get_cart_items_count()
            allure.attach(f"После второго товара: {count_after_second}", 
                         name="Промежуточная проверка", attachment_type=allure.attachment_type.TEXT)
            
            inventory_page.add_onesie_to_cart()
            time.sleep(0.5)
            
            # Финальная проверка
            cart_count = inventory_page.get_cart_items_count()
            allure.attach(f"Финальное количество: {cart_count}", 
                         name="Количество товаров в корзине", 
                         attachment_type=allure.attachment_type.TEXT)
            
            # Делаем скриншот для диагностики
            driver.save_screenshot("after_adding_items.png")
            allure.attach.file("after_adding_items.png", name="После добавления товаров", 
                              attachment_type=allure.attachment_type.PNG)
            
            assert cart_count == 3, f"В корзине должно быть 3 товара, а сейчас {cart_count}"
        
        with allure.step("4. Переход в корзину"):
            cart_page = inventory_page.go_to_cart()
            cart_page.wait_for_page_load()
            
            # Проверяем, что в корзине правильное количество товаров
            cart_items = cart_page.get_cart_items_count()
            assert cart_items == 3, f"В корзине должно быть 3 товара, а сейчас {cart_items}"
            
            # Проверяем названия товаров
            item_names = cart_page.get_item_names()
            allure.attach("\n".join(item_names), name="Товары в корзине", 
                         attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("5. Оформление заказа"):
            checkout_page = cart_page.click_checkout()
            checkout_page.wait_for_page_load()
            
            checkout_page.fill_checkout_form(first_name, last_name, postal_code)
            checkout_page.click_continue()
        
        with allure.step("6. Проверка итоговой суммы"):
            actual_total = checkout_page.get_total_price()
            
            driver.save_screenshot("checkout_total.png")
            allure.attach.file("checkout_total.png", name="Итоговая сумма", 
                              attachment_type=allure.attachment_type.PNG)
            
            assert actual_total == expected_total, \
                f"Ожидаемая сумма ${expected_total}, фактическая ${actual_total}"
            
            allure.attach(f"Итоговая сумма: ${actual_total}", name="Результат", 
                         attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("7. Завершение заказа"):
            checkout_page.click_finish()
            allure.attach("Заказ успешно оформлен!", name="Статус", 
                         attachment_type=allure.attachment_type.TEXT)
    
    except Exception as e:
        # При ошибке делаем скриншот
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_error",
            attachment_type=allure.attachment_type.PNG
        )
        # Сохраняем HTML страницы для диагностики
        allure.attach(
            driver.page_source,
            name="page_source",
            attachment_type=allure.attachment_type.HTML
        )
        raise e