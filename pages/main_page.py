from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    questions_about_important_things = [By.XPATH, ".//*[contains(text(), 'Вопросы о важном')]"]
    accordion_heading_xpath = ".//div[contains(text(), '{}')]"
    accordion_panel_xpath = ".//div/p[text()='{}']"
    
    def __init__(self, driver):
        self.driver = driver

    def scroll_accordion_heading(self):
        element = self.driver.find_element(*self.questions_about_important_things)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_accordion_heading(self, heading):
        xpath = self.accordion_heading_xpath.format(heading)
        self.driver.find_element(By.XPATH, xpath).click()
    
    def check_accordion_panel(self, text):
        xpath = self.accordion_panel_xpath.format(text)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located([By.XPATH, xpath]))
        accordion_panel = self.driver.find_element(By.XPATH, xpath)

        assert accordion_panel.is_displayed()
