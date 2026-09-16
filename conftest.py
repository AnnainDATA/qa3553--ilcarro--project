import pytest
from selenium import webdriver
import logging

from data.user_data import existing_user
from pages.login_page import LoginPage
from utils.logger_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    logger.info("Starting browser session")
    driver=webdriver.Chrome()
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    #driver.implicitly_wait(5)
    yield driver

    #driver.implicitly_wait(5)
    logger.info("Closing browser session")
    driver.quit()

@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.email)
    login_page.fill_password(user.password)
    login_page.submit_login()
    login_page.close_window()
    return driver