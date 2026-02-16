"""
Модуль содержит класс для работы со страницей корзины интернет-магазина.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_10.shop.CheckoutPage import CheckoutPage
import allure

class CartPage:
    """
    Класс для взаимодействия со страницей корзины.
    Предоставляет методы для работы с элементами корзины:
    - просмотр добавленных товаров
    - переход к оформлению заказа
    - получение информации о товарах в корзине
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы элементов на странице
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    @allure.step("Ожидать загрузки корзины")
    def wait_for_page_load(self) -> 'CartPage':
        """
        Ожидает полной загрузки страницы корзины.
        Returns:
            CartPage: экземпляр текущей страницы для цепочки вызовов
        """
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))
        return self
    
    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> CheckoutPage:
        """
        Нажимает кнопку оформления заказа.
        Returns:
            CheckoutPage: экземпляр страницы оформления заказа
        """
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        # Ждем загрузки страницы оформления
        self.wait.until(EC.url_contains("checkout-step-one"))
        return CheckoutPage(self.driver)
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине.
        Returns:
            int: количество товаров в корзине
        """
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM))
        return len(items)
    
    @allure.step("Получить названия товаров в корзине")
    def get_item_names(self) -> list:
        """
        Получает список названий товаров в корзине.
        Returns:
            list: список названий товаров
        """
        items = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAME))
        return [item.text for item in items]