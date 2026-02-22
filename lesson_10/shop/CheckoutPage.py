"""
Модуль содержит класс для работы со страницей оформления заказа.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    Класс для взаимодействия со страницей оформления заказа.
    Предоставляет методы для:
    - заполнения формы с личными данными
    - подтверждения заказа
    - получения итоговой суммы
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы элементов на странице
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Локаторы для страницы обзора заказа
    SUMMARY_INFO = (By.CLASS_NAME, "summary_info")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    @allure.step("Ожидать загрузки страницы оформления")
    def wait_for_page_load(self) -> 'CheckoutPage':
        """
        Ожидает полной загрузки страницы оформления заказа.
        Returns:
            CheckoutPage: экземпляр текущей страницы для цепочки вызовов
        """
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))
        return self
    
    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """
        Заполняет форму с персональными данными покупателя.
        Args:
            first_name: str - имя покупателя
            last_name: str - фамилия покупателя
            postal_code: str - почтовый индекс
        Returns:
            CheckoutPage: экземпляр текущей страницы для цепочки вызовов
        """
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        
        last_name_field = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT))
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        
        postal_code_field = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE_INPUT))
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        
        return self
    
    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> 'CheckoutPage':
        """
        Нажимает кнопку продолжения оформления заказа.
        Returns:
            CheckoutPage: экземпляр текущей страницы для цепочки вызовов
        """
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_btn.click()
        # Ждем загрузки страницы обзора заказа
        try:
            self.wait.until(EC.presence_of_element_located(self.SUMMARY_INFO))
        except:
            # Если есть ошибка, получаем её текст
            error = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            raise Exception(f"Ошибка при оформлении заказа: {error.text}")
        return self
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_price(self) -> float:
        """
        Получает итоговую сумму заказа со страницы.
        Returns:
            float: итоговая сумма заказа
        """
        total_element = self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))
        total_text = total_element.text
        # Извлекаем числовое значение из текста "Total: $XX.XX"
        total_price = total_text.replace('Total:', '').replace('$', '').strip()
        return float(total_price)
    
    @allure.step("Нажать кнопку Finish")
    def click_finish(self) -> 'CheckoutPage':
        """
        Нажимает кнопку завершения заказа.
        Returns:
            CheckoutPage: экземпляр текущей страницы для цепочки вызовов
        """
        finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        finish_btn.click()
        # Ждем завершения заказа
        self.wait.until(EC.presence_of_element_located(self.BACK_HOME_BUTTON))
        return self