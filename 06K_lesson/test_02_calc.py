from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

pole_voda = driver.find_element(By.CSS_SELECTOR, '#delay').clear() #очищаем поле
pole_voda = driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(45)#введите значение 45.

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

result_wait = WebDriverWait(driver, 50)
result = result_wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        
#ожидание 50 секунд
long_wait = WebDriverWait(driver, 50)
        
# Ожидаем появление результата 15
result = long_wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

driver.quit()