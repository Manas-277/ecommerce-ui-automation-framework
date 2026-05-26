from pages.product_page import ProductPage
from pages.login_page import LoginPage

def test_add_all_product_to_cart(logged_in_driver):
    product_page = ProductPage(logged_in_driver)
    product_page.add_product_to_cart(10)
    assert product_page.get_cart_product_count() == 6

def test_add_product_to_cart(logged_in_driver):
    product_page = ProductPage(logged_in_driver)
    product_page.add_product_to_cart(1)
    assert product_page.get_cart_product_count() == 1

