import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TrackPage(BasePage):
    view_button = [By.XPATH, ".//div/button[text()='Посмотреть']"]
    
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Ожидаем загрузки страницы track')
    def wait_for_load_view_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.view_button))
