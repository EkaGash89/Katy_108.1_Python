import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Открыть сайт магазина в Firefox
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
        
# Шаг 2: Авторизация как пользователь standard_user
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
        
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()
        
# Ожидание загрузки страницы с товарами
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        
# Шаг 3: Добавление товаров в корзину
# Sauce Labs Backpack
backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
backpack_add_button.click()
        
# Sauce Labs Bolt T-Shirt
tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
tshirt_add_button.click()
        
# Sauce Labs Onesie
onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
onesie_add_button.click()
        
# Шаг 4: Перейти в корзину
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
        
# Ожидание загрузки страницы корзины
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout")))
        
# Шаг 5: Нажать Checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
        
# Ожидание загрузки формы
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name")))
        
# Шаг 6: Заполнить форму данными
first_name_field = driver.find_element(By.ID, "first-name")
last_name_field = driver.find_element(By.ID, "last-name")
postal_code_field = driver.find_element(By.ID, "postal-code")
        
first_name_field.send_keys("Иван")
last_name_field.send_keys("Петров")
postal_code_field.send_keys("123456")
        
# Шаг 7: Нажать кнопку Continue
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
        
# Ожидание загрузки страницы с итоговой стоимостью
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        
# Шаг 8: Прочитать итоговую стоимость
total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
total_text = total_element.text
        
# Извлечь числовое значение из текста
total_amount = total_text.replace("Total: $", "")
        
# Шаг 9: Проверить, что итоговая сумма равна $58.29
expected_total = "58.29"
assert total_amount == expected_total, f"Ожидаемая сумма: ${expected_total}, Фактическая сумма: ${total_amount}"
        
print(f"Тест пройден! Итоговая сумма: ${total_amount}")

driver.quit()