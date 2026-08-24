import random
from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page=RegistrationPage(driver)
# -------------
    random_suffix = random.randint(1,1_000_000)
    user=User(
        "Dony",
        "Molly",
        f"dony_{random_suffix}@gmail.com", #random email
        "Password123$"
    )
# -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.login_success_text()=="Registered"
    assert registration_page.login_success_text1() == "You are logged in success"
    registration_page.close_window()


#---------------------------------------------------------
def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "",
        "Molly",
        "dony_1@gmail.com",
        "Password123$"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Name is required"
    assert registration_page.is_button_disabled()
    registration_page.close_window()


#---------------------------------------------------------
def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "",
        "dony_1@gmail.com",
        "Password123$"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Last name is required"
    assert registration_page.is_button_disabled()
    registration_page.close_window()


#---------------------------------------------------------
def test_registration_with_wrong_email_format(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "Molly",
        "dony_1gmail.com",
        "Password123$"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Wrong email format"
    assert registration_page.is_button_disabled()
    registration_page.close_window()


def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "Molly",
        "",
        "Password123$"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Email is required"
    assert registration_page.is_button_disabled()
    registration_page.close_window()


#---------------------------------------------------------
def test_registration_with_wrong_password_format(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "Molly",
        "dony_13@gmail.com",
        "000"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Password must contain minimum 6 symbols"
    assert registration_page.is_button_disabled()
    registration_page.close_window()

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "Molly",
        "dony_13@gmail.com",
        ""
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Password is required"
    assert registration_page.is_button_disabled()
    registration_page.close_window()


#---------------------------------------------------------
def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)
    # -------------
    user = User(
        "Sally",
        "Molly",
        "dony_13@gmail.com",
        "Password123$"
    )
    # -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="You must accept the terms"
    assert registration_page.is_button_disabled()
    registration_page.close_window()