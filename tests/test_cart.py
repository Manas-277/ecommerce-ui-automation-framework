from pages.cart_page import CartPage

def test_cart_page(logged_in_driver):
    cart_page = CartPage(logged_in_driver)
    cart_page.go_to_cart()
    assert cart_page.get_cart_title() == "Your Cart"


def test_remove_single_product(cart_with_products):
    cart_page = CartPage(cart_with_products)
    cart_page.go_to_cart()
    products_in_cart = cart_page.get_cart_product_count()
    cart_page.remove_single_product()
    assert cart_page.get_cart_product_count() == products_in_cart - 1


def test_remove_all_products(cart_with_products):
    cart_page = CartPage(cart_with_products)
    cart_page.go_to_cart()
    if cart_page.get_cart_product_count() > 0:
        cart_page.remove_all_products()
    assert cart_page.get_cart_product_count() == 0


def test_proceed_to_checkout(cart_with_products):
    cart_page = CartPage(cart_with_products)
    cart_page.go_to_cart()
    cart_page.proceed_to_checkout()
    assert cart_page.is_checkout_info_displayed(), \
        "Checkout failed to display checkout information."