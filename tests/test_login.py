from selenium.common import TimeoutException

from data.user_data import existing_user
from pages.login_page import LoginPage


WRONG_EMAIL = "anna.moshegmail.com"

# ------Registered user can log in with valid data------
def test_login_success(driver):
    login_page=LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.confirmation_text() == "You are logged in success"
    login_page.close_window()
    assert login_page.is_logged() is True

# ----------LOGIN----------
# ------1.Registered user can't log in with invalid email------
def test_login_valid_pwd_wrong_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(WRONG_EMAIL)
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.error_message_text()=="Wrong email format"
    assert login_page.submit_button_disabled()

# ------2.Registered user can't log in with email field empty------
def test_login_valid_pwd_empty_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email("")
    login_page.fill_password(user.password)
    login_page.submit_login()
    assert login_page.error_message_text()=="Email is required"
    assert login_page.submit_button_disabled()

# ------3.Registered user can't log in with invalid password------
def test_login_wrong_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()
    wrong_password = "TotallyWrongPass123$"

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(wrong_password)
    login_page.submit_login()
    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'

# ------4.Registered user can't log in with password field empty------
# ------The "Yalla" button is disabled
# ------The message "Password is required" appeared
def test_login_empty_pwd_valid_email_registered_user(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password("")
    login_page.submit_login()
    assert login_page.error_message_text() == "Password is required"
    assert login_page.submit_button_disabled()

# ------5.Unregistered user can't log in with valid data------
def test_login_not_success_unregister_user(driver):
    login_page=LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("zimun15@gmail.com")
    login_page.fill_password("Zimun123456!")
    login_page.submit_login()
    assert login_page.confirmation_text() == "Login failed"
    assert login_page.confirmation_message() == '"Login or Password incorrect"'

