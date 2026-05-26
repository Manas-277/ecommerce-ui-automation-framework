from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_input_xpath = (By.XPATH, "//input[@id='user-name']")
        self.password_input_xpath = (By.XPATH, "//input[@id='password']")
        self.login_button_xpath = (By.XPATH, "//input[@id='login-button']")
        self.products_title_xpath = (By.XPATH, "//span[@class='title']")
        self.error_message_xpath = (By.XPATH, "//h3[@data-test='error']")
    
    def login(self, username, password):
        self.driver.find_element(*self.username_input_xpath).send_keys(username)
        self.driver.find_element(*self.password_input_xpath).send_keys(password)
        self.driver.find_element(*self.login_button_xpath).click()

        WebDriverWait(self.driver, 10).until(
            EC.any_of(
                EC.presence_of_element_located(
                    self.products_title_xpath
                ),
                EC.presence_of_element_located(
                    self.error_message_xpath
                )
            )
        )

    
    def get_error_message(self):
            return self.driver.find_element(
                *self.error_message_xpath
            ).text
    
    def get_products_title(self):
        return self.driver.find_element(*self.products_title_xpath)