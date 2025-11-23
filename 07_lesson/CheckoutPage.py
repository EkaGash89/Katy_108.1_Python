from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        # Используем presence_of_element_located вместо element_to_be_clickable
        first_name_field = self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        
        last_name_field = self.wait.until(EC.presence_of_element_located(self.LAST_NAME_INPUT))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        
        postal_code_field = self.wait.until(EC.presence_of_element_located(self.POSTAL_CODE_INPUT))
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        
        return self
    
    def click_continue(self):
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_btn.click()
        return self
    
    def get_total_price(self):
        total_element = self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))
        total_text = total_element.text
        # Извлекаем числовое значение из текста "Total: $58.29"
        total_price = total_text.split('$')[-1]
        return float(total_price)
    
    def click_finish(self):
        finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        finish_btn.click()
        return self