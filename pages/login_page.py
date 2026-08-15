from selenium.webdriver.common.by import By


class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn--primary")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, "button.navigation-link.linklike")

    def __init__ (self,driver):
        self.driver=driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

