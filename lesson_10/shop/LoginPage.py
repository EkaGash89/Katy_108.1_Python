"""
Модуль содержит класс для работы со страницей авторизации.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_10.shop.InventoryPage import InventoryPage
import allure
import time


class LoginPage:
    """
    Класс для взаимодействия со страницей входа в систему.
    Предоставляет методы для:
    - открытия страницы авторизации
    - ввода учетных данных
    - выполнения входа в систему
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Увеличен таймаут
    
    # Локаторы элементов на странице
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    @allure.step("Открыть страницу авторизации")
    def open(self) -> 'LoginPage':
        """
        Открывает страницу авторизации в браузере.
        Returns:
            LoginPage: экземпляр текущей страницы для цепочки вызовов
        """
        self.driver.get("https://www.saucedemo.com/")
        # Ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        
        # Проверяем наличие всплывающих окон и закрываем их если есть
        try:
            # Пытаемся найти и закрыть любые всплывающие окна сохранения пароля
            alerts = self.driver.find_elements(By.CSS_SELECTOR, "[role='alert'], .alert, [class*='notification']")
            for alert in alerts:
                if alert.is_displayed():
                    alert.click()  # или закрыть другим способом
        except:
            pass  # Игнорируем, если окон нет
        
        return self
    
    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> 'LoginPage':
        """
        Вводит имя пользователя в поле логина.
        Args:
            username: str - имя пользователя  
        Returns:
            LoginPage: экземпляр текущей страницы для цепочки вызовов
        """
        # Дополнительная проверка, что поле доступно
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> 'LoginPage':
        """
        Вводит пароль в соответствующее поле.
        Args:
            password: str - пароль пользователя  
        Returns:
            LoginPage: экземпляр текущей страницы для цепочки вызовов
        """
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    @allure.step("Нажать кнопку Login")
    def click_login(self) -> InventoryPage:
        """
        Нажимает кнопку входа в систему.
        Returns:
            InventoryPage: экземпляр страницы с товарами
        """
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()
        
        # Даем время на обработку входа
        time.sleep(1)
        
        # Ждем перехода на страницу товаров
        self.wait.until(EC.url_contains("inventory"))
        return InventoryPage(self.driver)
    
    @allure.step("Проверить сообщение об ошибке")
    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке при неудачной авторизации.
        Returns:
            str: текст сообщения об ошибке
        """
        error_element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        return error_element.text