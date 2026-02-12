import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class MainPage(BasePage):
    order_ultrabig_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[1]"]
    questions_about_important_things = [By.XPATH, ".//*[contains(text(), 'Вопросы о важном')]"]
    accordion_heading_xpath = ".//div[contains(text(), '{}')]"
    accordion_panel_xpath = ".//div/p[text()='{}']"
    
    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ищем большую кнопку "Заказать" и переходим к ней') 
    def scroll_order_ultrabig_button(self):
        element = self.driver.find_element(*self.order_ultrabig_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ищем большую кнопку "Заказать" и нажимаем на неё') 
    def click_order_ultrabig_button(self):
        self.driver.find_element(*self.order_ultrabig_button).click()

    @allure.step('Ищем надпись "Вопросы о важном" и переходим к ней')
    def scroll_accordion_heading(self):
        element = self.driver.find_element(*self.questions_about_important_things)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ищем раскрывающийся список вопросов и нажимаем на него') 
    def click_accordion_heading(self, heading):
        xpath = self.accordion_heading_xpath.format(heading)
        self.driver.find_element(By.XPATH, xpath).click()
    
    @allure.step('Проверяем, что при нажатии на стрелочку, открывается соответствующий текст')
    def check_accordion_panel(self, text):
        xpath = self.accordion_panel_xpath.format(text)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located([By.XPATH, xpath]))
        accordion_panel = self.driver.find_element(By.XPATH, xpath)

        assert accordion_panel.is_displayed()
