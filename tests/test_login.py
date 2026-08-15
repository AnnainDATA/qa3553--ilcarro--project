from pages.login_page import LoginPage

VALID_EMAIL="anna12345@gmail.com"
VALID_EMAIL_UNREGISTERED="anna.anikeenko@gmail.com"
VALID_PASSWORD="123456!Anna"
VALID_PASSWORD_UNREGISTERED="A13579!Ann"

# Registered user can log in with valid data
def test_login_success(driver):
    login_page=LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

# Unregistered user can’t log in with valid data
def test_login_unsuccess_unregistered_user(driver):
    login_page=LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL_UNREGISTERED)
    login_page.fill_password(VALID_PASSWORD_UNREGISTERED)
    login_page.submit_login()
