# pytest -v tests/test_registration.py

import time
import pytest
from faker import Faker
from data.user_data import create_user
from models.user import User
from pages.registration_page import RegistrationPage

fake = Faker()

# ---------Registration positive---------
# 1. ------Unregistered User can register with correct data------
def test_registration_success(driver):
    registration_page=RegistrationPage(driver)
    user=create_user()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text()=="Registered"
    assert registration_page.confirmation_message() == "You are logged in success"

# ---------Registration negative---------
# 1. -----Unregistered User can't register with field [NAME] empty------
def test_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Name is required"
    assert registration_page.submit_button_disabled()

# 2. ------Unregistered User can't register with field [LAST NAME] empty------
def test_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(last_name="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Last name is required"
    assert registration_page.submit_button_disabled()

# 3. ------Unregistered User can't register with incorrect data in field [EMAIL]------
def test_registration_with_wrong_email_format(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(email="dony_1gmail.com")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Wrong email format"
    assert registration_page.submit_button_disabled()

# 4. ------Unregistered User can't register with field [EMAIL] empty------
def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    user=create_user(email="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Email is required"
    assert registration_page.submit_button_disabled()

# ------5. Unregistered User can't register with incorrect data in field [PASSWORD]------
def test_registration_with_wrong_password_format(driver):
    registration_page = RegistrationPage(driver)
    user=create_user(password="0000")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()

#---------------------------------------------------------
# 6. ------Unregistered User can't register with field [PASSWORD] empty------
def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)
    user=create_user(password="")

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="Password is required"
    assert registration_page.submit_button_disabled()

# ------7. Unregistered User can't register with unsigned checkbox------
def test_registration_without_checkbox(driver):
    registration_page = RegistrationPage(driver)
    user=create_user()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.error_message_text()=="You must accept the terms"
    assert registration_page.submit_button_disabled()

# ------8. Registered user can`t register with registered data (email and password)
def test_registration_email_pwd_registered(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()

    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    registration_page.close_window1()

    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registration failed"

#---------------------------------------------------------
# 9. Registered user can`t register with registered email and new valid password
def test_registration_email_registered_pwd_new(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()
    duplicate_user = create_user(name=user.name, last_name=user.last_name, email=user.email)

    print(f"\nUser password: {user.password}")
    print(f"Duplicate user password: {duplicate_user.password}")
# -------------
    registration_page.open_registration_form()
    registration_page.fill_registration_form(user)
    registration_page.check_policy()
    registration_page.submit_registration()
    registration_page.close_window1()

    registration_page.fill_registration_form(duplicate_user)
    registration_page.check_policy()
    registration_page.submit_registration()

    assert registration_page.confirmation_text() == "Registration failed"
