from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_list = (By.XPATH, "//div[@class='inventory_list']")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(),'Add to cart')]")
        self.cart_badge_locator = (By.CLASS_NAME, "shopping_cart_badge")

    def add_product_to_cart(self, number_of_product):
        add_to_cart_buttons = self.driver.find_elements(*self.add_to_cart_button)
        if number_of_product >= len(add_to_cart_buttons):
            # add all available products to cart
            for button in add_to_cart_buttons:
                button.click()
        else:
            for i in range(number_of_product):
                add_to_cart_buttons[i].click()
    
    def get_cart_product_count(self):
        try:
            cart_badge = self.driver.find_element(*self.cart_badge_locator)
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0