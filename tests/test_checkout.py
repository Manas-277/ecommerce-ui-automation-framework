from pages.checkout_page import CheckoutPage

def test_valid_checkout(checkout_driver):
    checkout_page = CheckoutPage(checkout_driver)
    assert checkout_page.fill_checkout_information(
        "John",
        "Doe",
        "12345"
    ) is None

    assert checkout_page.verify_overview_page()
    checkout_page.finish_checkout()
    assert checkout_page.verify_successful_checkout()
    assert checkout_page.logout(), "Logout failed, login page not displayed"

def test_invalid_checkout(checkout_driver):
    checkout_page = CheckoutPage(checkout_driver)
    error_message = checkout_page.fill_checkout_information(
        "",
        "",
        ""
    )

    assert error_message == "Error: First Name is required"

    error_message = checkout_page.fill_checkout_information(
        "John",
        "",
        ""
    )

    assert error_message == "Error: Last Name is required"

    error_message = checkout_page.fill_checkout_information(
        "John",
        "Doe",
        ""
    )

    assert error_message == "Error: Postal Code is required"

    assert not checkout_page.verify_overview_page(), \
        "Overview page should not be displayed with invalid input"