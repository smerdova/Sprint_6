import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import tests.paths as paths

class BasePage:
    order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    yandex_logo_button = [By.XPATH, ".//*[@class='Header_LogoYandex__3TSOI']/img[1]"]
    scooter_logo_button = [By.XPATH, ".//*[@class='Header_LogoScooter__3lsAR']/img[1]"]

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем кнопку "Заказать" в header и нажимаем на неё') 
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Ищем логотип Яндекса в header и нажимаем на него')
    def click_yandex_logo_button(self):
        self.driver.find_element(*self.yandex_logo_button).click()

    @allure.step('Ищем логотип Самоката в header и нажимаем на него')    
    def click_scooter_logo_button(self):
        self.driver.find_element(*self.scooter_logo_button).click()
    
    @allure.step('Проверяем, что при нажатии на логотип "Самоката", попадаешь на главную страницу "Самоката"')
    def check_main_page_scooter(self):
        assert self.driver.current_url == paths.BASE_URL
    
    @allure.step('Проверяем, что при нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def check_main_page_dzen(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(paths.URL_DZEN))
    