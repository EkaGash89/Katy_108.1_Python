import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    
    # Явное ожидание загрузки страницы товаров
    inventory_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    
    # Добавление товаров в корзину
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    
    # Переход в корзину
    cart_page = inventory_page.go_to_cart()
    
    # Ожидание загрузки корзины
    cart_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))
    
    # Переход к оформлению заказа
    checkout_page = cart_page.click_checkout()
    
    # Ожидание появления формы
    checkout_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout_info")))
    
    # Заполнение формы
    checkout_page.fill_checkout_form(first_name, last_name, postal_code)
    checkout_page.click_continue()
    
    # Ожидание загрузки страницы с итогами
    checkout_page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))
    
    # Проверка итоговой суммы
    actual_total = checkout_page.get_total_price()
    assert actual_total == expected_total, f"Expected total ${expected_total}, but got ${actual_total}"
    
    print(f"Тест пройден! Итоговая сумма: ${actual_total}")