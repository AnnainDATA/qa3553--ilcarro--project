import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    driver.implicitly_wait(10)
    yield driver

    driver.implicitly_wait(10)
    driver.quit()