"""
Модуль содержит класс для работы со страницей товаров (инвентаря).
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from lesson_10.shop.CartPage import CartPage
import allure
import time


class InventoryPage:
    """
    Класс для взаимодействия со страницей каталога товаров.
    Предоставляет методы для:
    - добавления товаров в корзину
    - перехода в корзину
    - получения информации о количестве товаров в корзине
    """
    
    def __init__(self, driver):
        """
        Инициализация страницы товаров.
        Args:
            driver: WebDriver - экземпляр драйвера браузера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    # Локаторы элементов на странице
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BOLT_TSHIRT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    ONESIE_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    
    # Альтернативные локаторы на случай изменения ID
    BACKPACK_ALT = (By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
    BOLT_TSHIRT_ALT = (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button")
    ONESIE_ALT = (By.XPATH, "//div[text()='Sauce Labs Onesie']/ancestor::div[@class='inventory_item']//button")
    
    @allure.step("Ожидать загрузки страницы товаров")
    def wait_for_page_load(self) -> 'InventoryPage':
        """
        Ожидает полной загрузки страницы с товарами.
        Returns:
            InventoryPage: экземпляр текущей страницы для цепочки вызовов
        """
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
        self.wait.until(EC.presence_of_all_elements_located(self.INVENTORY_ITEM))
        return self
    
    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self) -> 'InventoryPage':
        """
        Добавляет товар 'Sauce Labs Backpack' в корзину.
        Returns:
            InventoryPage: экземпляр текущей страницы для цепочки вызовов
        """
        try:
            # Сначала проверяем, не добавлен ли уже товар
            try:
                remove_button = self.driver.find_element(*self.BACKPACK_REMOVE_BUTTON)
                if remove_button.is_displayed():
                    allure.attach("Товар уже в корзине", name="Sauce Labs Backpack", 
                                 attachment_type=allure.attachment_type.TEXT)
                    return self
            except:
                pass
            
            # Пробуем добавить через основной локатор
            add_button = self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON))
            add_button.click()
            allure.attach("Добавлен через основной локатор", name="Sauce Labs Backpack", 
                         attachment_type=allure.attachment_type.TEXT)
            
            # Проверяем, что кнопка изменилась на "Remove"
            self.wait.until(EC.presence_of_element_located(self.BACKPACK_REMOVE_BUTTON))
            
        except TimeoutException:
            # Если не получилось через основной локатор, пробуем альтернативный
            try:
                allure.attach("Основной локатор не сработал, пробую альтернативный", 
                             name="Sauce Labs Backpack", attachment_type=allure.attachment_type.TEXT)
                add_button = self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ALT))
                
                # Проверяем текст кнопки
                if "Add" in add_button.text or "add" in add_button.text.lower():
                    add_button.click()
                    allure.attach("Добавлен через альтернативный локатор", 
                                 name="Sauce Labs Backpack", attachment_type=allure.attachment_type.TEXT)
                else:
                    allure.attach(f"Кнопка уже в состоянии: {add_button.text}", 
                                 name="Sauce Labs Backpack", attachment_type=allure.attachment_type.TEXT)
            except:
                allure.attach("НЕ УДАЛОСЬ добавить товар!", 
                             name="Sauce Labs Backpack - ОШИБКА", 
                             attachment_type=allure.attachment_type.TEXT)
                # Делаем скриншот для диагностики
                self.driver.save_screenshot("backpack_error.png")
                allure.attach.file("backpack_error.png", name="Скриншот ошибки", 
                                  attachment_type=allure.attachment_type.PNG)
        
        return self
    
    @allure.step("Добавить футболку в корзину")
    def add_bolt_tshirt_to_cart(self) -> 'InventoryPage':
        """
        Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину.
        Returns:
            InventoryPage: экземпляр текущей страницы для цепочки вызовов
        """
        try:
            # Проверяем, не добавлен ли уже товар
            try:
                remove_button = self.driver.find_element(*self.BOLT_TSHIRT_REMOVE_BUTTON)
                if remove_button.is_displayed():
                    allure.attach("Товар уже в корзине", name="Sauce Labs Bolt T-Shirt", 
                                 attachment_type=allure.attachment_type.TEXT)
                    return self
            except:
                pass
            
            add_button = self.wait.until(EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON))
            add_button.click()
            allure.attach("Добавлен через основной локатор", name="Sauce Labs Bolt T-Shirt", 
                         attachment_type=allure.attachment_type.TEXT)
            self.wait.until(EC.presence_of_element_located(self.BOLT_TSHIRT_REMOVE_BUTTON))
            
        except TimeoutException:
            try:
                allure.attach("Основной локатор не сработал, пробую альтернативный", 
                             name="Sauce Labs Bolt T-Shirt", attachment_type=allure.attachment_type.TEXT)
                add_button = self.wait.until(EC.element_to_be_clickable(self.BOLT_TSHIRT_ALT))
                if "Add" in add_button.text or "add" in add_button.text.lower():
                    add_button.click()
                    allure.attach("Добавлен через альтернативный локатор", 
                                 name="Sauce Labs Bolt T-Shirt", attachment_type=allure.attachment_type.TEXT)
            except:
                allure.attach("НЕ УДАЛОСЬ добавить товар!", 
                             name="Sauce Labs Bolt T-Shirt - ОШИБКА", 
                             attachment_type=allure.attachment_type.TEXT)
                self.driver.save_screenshot("tshirt_error.png")
                allure.attach.file("tshirt_error.png", name="Скриншот ошибки", 
                                  attachment_type=allure.attachment_type.PNG)
        
        return self
    
    @allure.step("Добавить комбинезон в корзину")
    def add_onesie_to_cart(self) -> 'InventoryPage':
        """
        Добавляет товар 'Sauce Labs Onesie' в корзину.
        Returns:
            InventoryPage: экземпляр текущей страницы для цепочки вызовов
        """
        try:
            # Проверяем, не добавлен ли уже товар
            try:
                remove_button = self.driver.find_element(*self.ONESIE_REMOVE_BUTTON)
                if remove_button.is_displayed():
                    allure.attach("Товар уже в корзине", name="Sauce Labs Onesie", 
                                 attachment_type=allure.attachment_type.TEXT)
                    return self
            except:
                pass
            
            add_button = self.wait.until(EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON))
            add_button.click()
            allure.attach("Добавлен через основной локатор", name="Sauce Labs Onesie", 
                         attachment_type=allure.attachment_type.TEXT)
            self.wait.until(EC.presence_of_element_located(self.ONESIE_REMOVE_BUTTON))
            
        except TimeoutException:
            try:
                allure.attach("Основной локатор не сработал, пробую альтернативный", 
                             name="Sauce Labs Onesie", attachment_type=allure.attachment_type.TEXT)
                add_button = self.wait.until(EC.element_to_be_clickable(self.ONESIE_ALT))
                if "Add" in add_button.text or "add" in add_button.text.lower():
                    add_button.click()
                    allure.attach("Добавлен через альтернативный локатор", 
                                 name="Sauce Labs Onesie", attachment_type=allure.attachment_type.TEXT)
            except:
                allure.attach("НЕ УДАЛОСЬ добавить товар!", 
                             name="Sauce Labs Onesie - ОШИБКА", 
                             attachment_type=allure.attachment_type.TEXT)
                self.driver.save_screenshot("onesie_error.png")
                allure.attach.file("onesie_error.png", name="Скриншот ошибки", 
                                  attachment_type=allure.attachment_type.PNG)
        
        return self
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине (значение бейджа).
        Returns:
            int: количество товаров в корзине (0, если корзина пуста)
        """
        try:
            # Ждем появления бейджа
            badge = self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
            count = int(badge.text)
            allure.attach(f"Найден бейдж корзины со значением: {count}", 
                         name="Количество товаров", attachment_type=allure.attachment_type.TEXT)
            return count
        except:
            # Если бейджа нет, значит корзина пуста
            allure.attach("Бейдж корзины не найден - корзина пуста", 
                         name="Количество товаров", attachment_type=allure.attachment_type.TEXT)
            return 0
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.
        Returns:
            CartPage: экземпляр страницы корзины
        """
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
        cart_btn.click()
        # Ждем загрузки страницы корзины
        self.wait.until(EC.url_contains("cart"))
        return CartPage(self.driver)
    
    @allure.step("Получить список всех товаров на странице")
    def get_all_inventory_items(self) -> list:
        """
        Получает список всех товаров на странице для диагностики.
        Returns:
            list: список названий товаров
        """
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        item_names = []
        for item in items:
            try:
                name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                item_names.append(name)
            except:
                pass
        return item_names