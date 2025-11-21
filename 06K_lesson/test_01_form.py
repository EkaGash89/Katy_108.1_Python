from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
import time

def test_form():
    edge_driver_path = r"D:\edgedriver_win64 (1)\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    # Шаг 1: Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
        
    # Ждем загрузки формы
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))      
    # Шаг 2: Заполнить форму значениями
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")       
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")      
    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear() #очищаем поле
    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
        
    # Прокручиваем к кнопке Submit
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Submit')]")))
        
    # Прокручиваем страницу к кнопке
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        
    # Используем JavaScript для клика (обход перехвата клика)
    driver.execute_script("arguments[0].click();", submit_button)
        
    # Шаг 4: Проверить, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_class = zip_code_field.get_attribute("class")
    
        
    # Проверяем, что поле имеет класс указывающий на ошибку
    assert "alert-danger" in zip_code_class, f"Поле Zip code должно быть подсвечено красным (class: {zip_code_class})"
        
    # Шаг 5: Проверить, что остальные поля подсвечены зеленым
    fields_to_check = ["first-name","last-name", "address","e-mail","phone","city","country","job-position","company"]
        
    for field_name in fields_to_check:
        field = driver.find_element(By.ID, field_name)
        field_class = field.get_attribute("class")
        
    # Проверяем, что поле имеет класс указывающий на успешную валидацию
    assert "alert-success" in field_class, f"Поле {field_name} должно быть подсвечено зеленым (class: {field_class})"

    driver.quit()
