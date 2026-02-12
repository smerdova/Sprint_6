import allure
import pytest
from tests import paths
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(paths.BASE_URL)

    yield driver

    driver.quit()
