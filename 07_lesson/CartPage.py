from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CheckoutPage import CheckoutPage

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located(self.CART_LIST))
        return self
    
    def click_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        return CheckoutPage(self.driver)
    
    def get_cart_items_count(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEMS))
        return len(items)
    
    def get_item_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]