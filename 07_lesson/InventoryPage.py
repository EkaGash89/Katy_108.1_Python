from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CartPage import CartPage

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_LIST))
        return self
    
    def add_backpack_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON))
        add_button.click()
        return self
    
    def add_bolt_tshirt_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON))
        add_button.click()
        return self
    
    def add_onesie_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON))
        add_button.click()
        return self
    
    def get_cart_items_count(self):
        try:
            badge = self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
            return int(badge.text)
        except:
            return 0
    
    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
        cart_btn.click()
        return CartPage(self.driver)