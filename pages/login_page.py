import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn--primary")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, "button.navigation-link.linklike")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR,"h3")
    CONFIRMATION_TEXT1 = (By.CSS_SELECTOR, "p")
    OK_BTN = (By.CSS_SELECTOR,"a.btn.btn")
    ALERT_WRONG_EMAIL_FORMAT = (By.XPATH,"//div[text()='Wrong email format']")
    ALERT_EMAIL_IS_REQUIRED = (By.XPATH,"//div[text()='Email is required']")
    ALERT_LOGIN_FAILED = (By.XPATH, "//p[text()='\"Login or Password incorrect\"]") #------incorrect!!
    ALERT_PWD_IS_REQUIRED = (By.XPATH,"//div[text()='Password is required']")
    BTN_DISABLED = (By.CSS_SELECTOR, "button.btn.btn--primary[disabled]")
    ERROR_MESSAGE = (By.CLASS_NAME,"error")

    def __init__ (self,driver):
        self.driver=driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()
        time.sleep(5)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()


    def login_success_text(self):
        element=WebDriverWait(self.driver,timeout=5). until(
        EC.visibility_of_element_located(self.CONFIRMATION_TEXT),)
        return element.text

    def login_success_text1(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            EC.visibility_of_element_located(self.CONFIRMATION_TEXT1), )
        return element.text


    def close_window(self):
        self.driver.find_element(*self.OK_BTN).click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()


    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.SIGN_OUT_BUTTON))
            return True
        except TimeoutException:
            return False


    def alert_wrong(self):
        try:
            WebDriverWait(self.driver, timeout=15).until(
                EC.any_of(
                EC.visibility_of_element_located(self.ALERT_WRONG_EMAIL_FORMAT),
                EC.visibility_of_element_located(self.ALERT_EMAIL_IS_REQUIRED),
                EC.visibility_of_element_located(self.ALERT_LOGIN_FAILED),
                EC.visibility_of_element_located(self.ALERT_PWD_IS_REQUIRED),
                ))
            return True
        except TimeoutException:
            return False


    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout=15).until(
            EC.alert_is_present())
        return alert.text


    def error_message_text(self):
        element = WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text


    def is_button_disabled(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.BTN_DISABLED))
            return True
        except TimeoutException:
            return False