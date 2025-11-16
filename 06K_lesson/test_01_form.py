from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_driver_path = r"D:\edgedriver_win64 (1)\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

# Шаг 1: Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()
        
# Ждем загрузки формы
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))
        
# Шаг 2: Заполнить форму значениями
# First name
first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
        
# Last name
last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
        
# Address
address = driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
        
# Email
email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
        
# Phone number
phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
        
# Zip code - оставляем пустым
zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear() #очищаем поле
        
# City
city = driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
        
# Country
country = driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
        
# Job position
job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
        
# Company
company = driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
           
# Шаг 3: Нажать кнопку Submit
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
               
# Шаг 4: Проверить, что поле Zip code подсвечено красным
zip_code_field = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
zip_code_class = zip_code_field.get_attribute("class")
        
# Проверяем, что поле имеет класс указывающий на ошибку
assert "is-invalid" in zip_code_class, "Поле Zip code должно быть подсвечено красным"
print("✓ Поле Zip code подсвечено красным")
        
# Шаг 5: Проверить, что остальные поля подсвечены зеленым
fields_to_check = [
        "first-name",
        "last-name", 
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
        
for field_name in fields_to_check:
        field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
        field_class = field.get_attribute("class")
            
# Проверяем, что поле имеет класс указывающий на успешную валидацию
        assert "is-valid" in field_class, f"Поле {field_name} должно быть подсвечено зеленым"
        print(f"✓ Поле {field_name} подсвечено зеленым")
        
print("\nВсе проверки пройдены успешно!")
               
driver.quit()