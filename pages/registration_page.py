import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    NAV_REGISTRATION_BTN=(By.CSS_SELECTOR,"[href='/register']")
    NAME_INPUT=(By.CSS_SELECTOR,"input[name='firstName']")
    LASTNAME_INPUT=(By.CSS_SELECTOR,"input[name='lastName']")
    EMAIL_INPUT_REG = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT_REG = (By.CSS_SELECTOR, "input[name='password']")
    CHECK_BOX=(By.CSS_SELECTOR,"input[name='termsOfUse']")
    TERMS_OF_USE=(By.CSS_SELECTOR,"[href='/terms-of-use']")
    PRIVACY_POLICY = (By.CSS_SELECTOR,"[href='/privacy-policy']")
    BTN_YALLA=(By.CSS_SELECTOR, "button.btn.btn--primary")
    BTN_YALLA_DISABLED = (By.CSS_SELECTOR, "button.btn.btn--primary[disabled]")
    OK_BTN = (By.CSS_SELECTOR, "button.btn.btn--primary")

    CONFIRMATION_TEXT = (By.CSS_SELECTOR,"h3")
    CONFIRMATION_TEXT1 = (By.CSS_SELECTOR, "p")

    ERROR_MESSAGE = (By.CLASS_NAME, "error")
    ALERT_NAME_IS_REQUIRED=(By.XPATH,"//div[text()='Name is required']")
    ALERT_LASTNAME_IS_REQUIRED = (By.XPATH, "//div[text()='Last name is required']")
    ALERT_EMAIL_IS_REQUIRED = (By.XPATH, "//div[text()='Email is required']")
    ALERT_PWD_IS_REQUIRED = (By.XPATH, "//div[text()='Password is required']")
    ALERT_ACCEPT_THE_TERMS = (By.XPATH, "//div[text()='You must accept the terms']")

    def __init__(self,driver):
        self.driver=driver

    def open_registration_form(self):
        self.driver.find_element(*self.NAV_REGISTRATION_BTN).click()
        time.sleep(5)

    def fill_name(self,name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_last_name(self,last_name):
        self.driver.find_element(*self.LASTNAME_INPUT).clear()
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(last_name)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT_REG).clear()
        self.driver.find_element(*self.EMAIL_INPUT_REG).send_keys(email)

    def fill_password(self,password):
        self.driver.find_element(*self.PASSWORD_INPUT_REG).clear()
        self.driver.find_element(*self.PASSWORD_INPUT_REG).send_keys(password)

    def check_policy(self):
        self.driver.find_element(*self.CHECK_BOX).click()

    def submit_registration(self):
        self.driver.find_element(*self.BTN_YALLA).click()

    def fill_registration_form(self, user):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_password(user.password)

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

    def error_message_text(self):
        element = WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text


    def is_button_disabled(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.BTN_YALLA_DISABLED))
            return True
        except TimeoutException:
            return False