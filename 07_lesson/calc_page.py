from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        
    def open(self):#Открывает страницу калькулятора
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        
    def set_delay(self, delay_seconds):#Устанавливает время задержки вычислений
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        
    def click_button(self, button_text):#Нажимает кнопку калькулятора по тексту
        button_locator = f"//span[text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()
        
    def enter_calculation(self, num1, operator, num2):#Вводит выражение для вычисления
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button('=')
        
    def get_result(self):#Возвращает текст из поля результата
        result_field = self.driver.find_element(By.CSS_SELECTOR, '.screen')
        return result_field.text
    
    def wait_for_calculation_to_complete(self, timeout=50):#Ожидает завершения вычисления
        result_field = (By.CSS_SELECTOR, '.screen')
        
        def is_calculation_complete(driver):
            current_text = driver.find_element(*result_field).text.strip()
            # Если текст пустой или содержит выражение, продолжаем ждать
            if not current_text or current_text in ['7+8', '7 + 8']:
                return False
            # Если текст - число, значит вычисление завершено
            try:
                int(current_text)
                return True
            except ValueError:
                return False
        
        self.wait.until(is_calculation_complete)
        return self.get_result()