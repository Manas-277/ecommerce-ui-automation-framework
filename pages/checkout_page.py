from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.XPATH, "//input[@id='first-name']")
        self.last_name_input = (By.XPATH, "//input[@id='last-name']")
        self.postal_code_input = (By.XPATH, "//input[@id='postal-code']")
        self.continue_button = (By.XPATH, "//input[@id='continue']")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
        self.overview_title = (By.XPATH, "//span[@class='title']")
        self.finish_button = (By.XPATH, "//button[@id='finish']")
        self.success_message = (By.XPATH, "//h2[@class='complete-header']")
        self.menu_button = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.logout_link = (By.XPATH, "//a[@id='logout_sidebar_link']")
        self.login_container = (By.XPATH, "//div[@id='login_button_container']")
    
    def fill_checkout_information(self, first_name, last_name, postal_code):
        first_name_element = self.driver.find_element(*self.first_name_input)
        last_name_element = self.driver.find_element(*self.last_name_input)
        postal_code_element = self.driver.find_element(*self.postal_code_input)

        first_name_element.clear()
        last_name_element.clear()
        postal_code_element.clear()

        first_name_element.send_keys(first_name)
        last_name_element.send_keys(last_name)
        postal_code_element.send_keys(postal_code)

        self.driver.find_element(*self.continue_button).click()

        error_messages = self.driver.find_elements(*self.error_message)
        if error_messages:
            return error_messages[0].text
        return None

    def verify_overview_page(self):
        overview_title = self.driver.find_element(*self.overview_title)
        return (overview_title.is_displayed() and overview_title.text == "Checkout: Overview")
    
    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
    
    def verify_successful_checkout(self):
        success_message = self.driver.find_element(*self.success_message)
        return (
            success_message.is_displayed()
            and
            success_message.text == "Thank you for your order!"
        )
    
    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        )
        logout_button.click()
        return self.driver.find_element(*self.login_container).is_displayed()