import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password",
    [
        ( "standard_user", "secret_sauce" ),
        ( "problem_user", "secret_sauce" ),
        ( "performance_glitch_user", "secret_sauce" ),
        ( "error_user", "secret_sauce" ),
        ( "visual_user", "secret_sauce" ),
    ]
)

def test_valid_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.get_products_title().is_displayed(), "Login Failed"


@pytest.mark.parametrize(
    "username, password",
    [
        ( "invalid_user", "invalid_password" ),
        ( "standard_user", "invalid_password" ),
        ( "invalid_user", "secret_sauce" ),
    ]
)
def test_invalid_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

@pytest.mark.parametrize(
    "username, password",
    [
        ( "", "secret_sauce"),
        ( "standard_user", "" ),
        ( "", "" )
    ]
)
def test_empty_fields_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.get_error_message() in ["Epic sadface: Username is required", "Epic sadface: Password is required"]
