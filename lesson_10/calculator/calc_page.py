from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from typing import Union
import allure


class CalculatorPage:
    """
    Класс для работы со страницей калькулятора.
    Предоставляет методы для взаимодействия с элементами страницы и выполнения вычислений.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.
        Args:
            driver: Экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора по URL.      
        Returns:
            None
        """
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    @allure.step("Установить задержку вычислений: {delay_seconds} секунд")
    def set_delay(self, delay_seconds: Union[int, str]) -> None:
        """
        Устанавливает время задержки перед выполнением вычислений.
        Args:
            delay_seconds: Время задержки в секундах (целое число или строка)
        Returns:
            None
        """
        delay_input: WebElement = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))

    @allure.step("Нажать кнопку: '{button_text}'")
    def click_button(self, button_text: Union[str, int]) -> None:
        """
        Нажимает кнопку калькулятора по тексту на ней.
        Args:
            button_text: Текст на кнопке (строка или число)
        Returns:
            None
        """
        button_locator: str = f"//span[text()='{button_text}']"
        button: WebElement = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    @allure.step("Ввести выражение: {num1} {operator} {num2}")
    def enter_calculation(self, num1: Union[int, str], operator: str, num2: Union[int, str]) -> None:
        """
        Вводит математическое выражение и запускает вычисление.
        Args:
            num1: Первое число
            operator: Математический оператор (+, -, *, /)
            num2: Второе число
        Returns:
            None
        """
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button('=')

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Возвращает текст из поля результата.
        Returns:
            str: Текущее значение в поле результата
        """
        result_field: WebElement = self.driver.find_element(By.CSS_SELECTOR, '.screen')
        return result_field.text

    @allure.step("Ожидать завершения вычисления (таймаут: {timeout} сек)")
    def wait_for_calculation_to_complete(self, timeout: int = 50) -> str:
        """
        Ожидает завершения вычисления калькулятора.
        Args:
            timeout: Максимальное время ожидания в секундах
        Returns:
            str: Результат вычисления после завершения
        Raises:
            TimeoutException: Если вычисление не завершилось за указанное время
        """
        result_field: tuple = (By.CSS_SELECTOR, '.screen')

        def is_calculation_complete(driver: WebDriver) -> bool:
            """
            Проверяет, завершилось ли вычисление.
            Args:
                driver: Экземпляр WebDriver
            Returns:
                bool: True если вычисление завершено, иначе False
            """
            current_text: str = driver.find_element(*result_field).text.strip()
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