from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.cart_page_title = (By.XPATH, "//span[@class='title']")
        self.remove_button = (By.XPATH, "//button[contains(text(), 'Remove')]")
        self.checkout_button = (By.XPATH, "//button[@id='checkout']")
        self.checkout_info = (By.XPATH, "//div[@class='checkout_info']")
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
    
    def remove_single_product(self):
        remove_buttons = self.driver.find_elements(*self.remove_button)
        if remove_buttons:
            remove_buttons[0].click()
    
    def remove_all_products(self):
        removed_count = 0
        while self.driver.find_elements(*self.remove_button):
            self.driver.find_elements(*self.remove_button)[0].click()
            removed_count += 1
        return removed_count
    
    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
    
    def get_cart_title(self):
        return self.driver.find_element(*self.cart_page_title).text
    
    def get_cart_product_count(self):
        return len(self.driver.find_elements(*self.remove_button))
    
    def is_checkout_info_displayed(self):
        return self.driver.find_element(*self.checkout_info).is_displayed()