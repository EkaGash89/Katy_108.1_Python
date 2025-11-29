import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage

@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Закрытие браузера после теста
    driver.quit()

def test_saucedemo_purchase_robust(driver):
    # Тестовые данные
    username = "standard_user"
    password = "secret_sauce"
    first_name = "John"
    last_name = "Doe"
    postal_code = "12345"
    expected_total = 58.29
    
    # Создаем экземпляры страниц
    login_page = LoginPage(driver)
    login_page.open()

    # Авторизация
    inventory_page = (login_page
                     .enter_username(username)
                     .enter_password(password)
                     .click_login())
    
    # Ожидание загрузки страницы товаров
    inventory_page.wait_for_page_load()
    
    # Добавление товаров в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()

    # Проверка количества товаров в корзине
    cart_count = inventory_page.get_cart_items_count()
    assert cart_count == 3, f"Expected 3 items in cart, but got {cart_count}"
    
    # Переход в корзину
    cart_page = inventory_page.go_to_cart()
    cart_page.wait_for_page_load()
    
    # Переход к оформлению заказа
    checkout_page = cart_page.click_checkout()
    checkout_page.wait_for_form_load()
    
    # Заполнение формы и переход к итогам
    (checkout_page
     .fill_checkout_form(first_name, last_name, postal_code)
     .click_continue())
    
    # Ожидание загрузки страницы с итогами
    checkout_page.wait_for_summary_load()
    
    # Проверка итоговой суммы
    actual_total = checkout_page.get_total_price()
    assert actual_total == expected_total, f"Expected total ${expected_total}, but got ${actual_total}"
    
    print(f"Тест пройден! Итоговая сумма: ${actual_total}")