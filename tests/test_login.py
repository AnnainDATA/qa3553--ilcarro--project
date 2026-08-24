from selenium.common import TimeoutException
from pages.login_page import LoginPage

VALID_EMAIL="anna12345@gmail.com"
VALID_PASSWORD="123456!Anna"

VALID_EMAIL_UNREGISTERED="anna.anikeenko@gmail.com"
VALID_PASSWORD_UNREGISTERED="A13579!Ann"

# ------Registered user can log in with valid data------
#----------------------------------------------------------
# def test_login_success(driver):
#     login_page=LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#     assert login_page.login_success_text() == "You are logged in success"
#     login_page.close_window()
#     assert login_page.is_logged() is True
#
# def test_login_success_1(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.login(VALID_EMAIL, VALID_PASSWORD)
#     assert login_page.login_success_text() == "You are logged in success"
#     login_page.close_window()
#     assert login_page.is_logged() is True

# ----------LOGIN----------
# ------1.Registered user can't log in with invalid email------
#----------------------------------------------------------
# def test_login_valid_pwd_invalid_email_registered_user(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email("anna.anikeenkogmail.com")
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#     assert login_page.error_message_text()=="Wrong email format"
#     assert login_page.is_button_disabled()


# ------2.Registered user can't log in with email field empty------
#----------------------------------------------------------
# def test_login_valid_pwd_empty_email_registered_user(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email("")
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#     assert login_page.alert_wrong() is True
#     assert login_page.error_message_text()=="Email is required"
#     assert login_page.is_button_disabled()


# ------3.Registered user can't log in with invalid password------
# def test_login_invalid_pwd_valid_email_registered_user(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password("000")
#     login_page.submit_login()
#     assert login_page.login_success_text() == "Login failed"
#     assert login_page.login_success_text1() == '"Login or Password incorrect"'


# ------4.Registered user can't log in with password field empty------
# ------The message "Password is required" appeared
#----------------------------------------------------------
# def test_login_empty_pwd_valid_email_registered_user(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password("")
#     login_page.submit_login()
#     assert login_page.alert_wrong() is True

# ------The "Yalla" button is disabled
#----------------------------------------------------------
# def test_login_empty_pwd_valid_email_registered_user1(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password("")
#     assert login_page.is_button_disabled() is True

# ------5.Unregistered user can't log in with valid data------
# def test_login_not_success_unregister_user(driver):
#     login_page=LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL_UNREGISTERED)
#     login_page.fill_password(VALID_PASSWORD_UNREGISTERED)
#     login_page.submit_login()
#     assert login_page.login_success_text() == "Login failed"
#     assert login_page.login_success_text1() == '"Login or Password incorrect"'

