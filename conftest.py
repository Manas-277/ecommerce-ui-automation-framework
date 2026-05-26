import pytest
import os
from datetime import datetime
from selenium import webdriver
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    return driver

@pytest.fixture(scope="function")
def cart_with_products(logged_in_driver):
    product_page = ProductPage(logged_in_driver)
    product_page.add_product_to_cart(3)
    return logged_in_driver

@pytest.fixture(scope="function")
def checkout_driver(logged_in_driver):
    product_page = ProductPage(logged_in_driver)
    product_page.add_product_to_cart(1)
    cart_page = CartPage(logged_in_driver)
    cart_page.go_to_cart()
    cart_page.proceed_to_checkout()
    return logged_in_driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "reports/screenshots"

            os.makedirs(
                screenshots_dir,
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            screenshot_name = (
                f"{item.name}_{timestamp}.png"
            )

            screenshot_path = os.path.join(
                screenshots_dir,
                screenshot_name
            )

            driver.save_screenshot(
                screenshot_path
            )