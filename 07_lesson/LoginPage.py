from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InventoryPage import InventoryPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()
        return InventoryPage(self.driver)