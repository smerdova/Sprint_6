import datetime
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class OrderPage(BasePage):
    first_name_input = [By.XPATH, ".//div/input[@placeholder='* Имя']"]
    last_name_input = [By.XPATH, ".//div/input[@placeholder='* Фамилия']"]
    adress_input = [By.XPATH, ".//div/input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station_input = [By.XPATH, ".//div/input[@placeholder='* Станция метро']"]
    station_input = [By.XPATH, ".//div[text()='Черкизовская']"]
    phone_input = [By.XPATH, ".//div/input[@placeholder='* Телефон: на него позвонит курьер']"]
    further_button = [By.XPATH, ".//div/button[text()='Далее']"]
    when_input = [By.XPATH, ".//div/input[@placeholder='* Когда привезти самокат']"]
    rental_period_input = [By.CLASS_NAME, "Dropdown-arrow"]
    two_days_input = [By.XPATH, ".//div[text()='двое суток']"]
    three_days_input = [By.XPATH, ".//div[text()='трое суток']"]
    black_color_checkbox_input = [By.XPATH, ".//input[@id='black']"]
    grey_color_checkbox_input = [By.XPATH, ".//input[@id='grey']"]
    comment_input = [By.XPATH, ".//div/input[@placeholder='Комментарий для курьера']"]
    order_middle_button = [By.XPATH, ".//div/button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    yes_button = [By.XPATH, ".//div/button[text()='Да']"]
    placed_order_title = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    view_status_button = [By.XPATH, ".//div/button[text()='Посмотреть статус']"]

    @allure.step('Открываем браузер Firefox')            
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузки страницы order')
    def wait_for_load_first_name_input(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.first_name_input))

    @allure.step('Ищем поле "Имя" и заполняем его')
    def set_first_name_input(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    @allure.step('Ищем поле "Фамилия" и заполняем его')
    def set_last_name_input(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    @allure.step('Ищем поле "Адресс" и заполняем его')
    def set_adress_input(self, adress):
        self.driver.find_element(*self.adress_input).send_keys(adress)

    @allure.step('Ищем поле "Станция метро" и нажимаем на него')
    def click_metro_station_input(self):
        self.driver.find_element(*self.metro_station_input).click()

    @allure.step('Ищем  станцию и выбираем ее')
    def click_station_input(self):
        self.driver.find_element(*self.station_input).click()
    
    @allure.step('Ищем поле "Телефон" и заполняем его')
    def set_phone_input(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)

    @allure.step('Ищем кнопку "Далее" и нажимаем на нее')
    def click_further_button(self):
        self.driver.find_element(*self.further_button).click()

    @allure.step('Ожидаем загрузки формы заказа')
    def wait_for_load_when_input(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.when_input))

    @allure.step('Ищем поле "Когда привезти самокат" и нажимаем на него')
    def click_when_input(self):
        self.driver.find_element(*self.when_input).click()

    @allure.step('Ищем поле "Когда привезти самокат" и заполняем его текущей датой')
    def set_when_input(self):
        self.driver.find_element(*self.when_input).send_keys(datetime.datetime.now().strftime('%d.%m.%Y'))

    @allure.step('Ищем поле "Срок аренды" и нажимаем на него')
    def click_rental_period_input(self):
        element = self.driver.find_element(*self.rental_period_input)
        element.click()

    @allure.step('Ищем поле "двое суток" и нажимаем на него')
    def click_two_days_input(self):
        self.driver.find_element(*self.two_days_input).click()

    @allure.step('Ищем поле "трое суток" и нажимаем на него')
    def click_three_days_input(self):
        self.driver.find_element(*self.three_days_input).click()

    @allure.step('Ищем чек-бокс "чёрный жемчуг" и нажимаем на него')
    def click_black_color_checkbox_input(self):
        self.driver.find_element(*self.black_color_checkbox_input).click()

    @allure.step('Ищем чек-бокс "серая безысходность" и нажимаем на него')
    def click_grey_color_checkbox_input(self):
        self.driver.find_element(*self.grey_color_checkbox_input).click()

    @allure.step('Ищем поле "Комментарий для курьера" и заполняем его')
    def set_comment_input(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    @allure.step('Ищем кнопку "Заказать" внизу формы и нажимаем на неё')
    def click_order_middle_button(self):
        self.driver.find_element(*self.order_middle_button).click()

    @allure.step('Ожидаем загрузки формы заказа')
    def wait_for_load_yes_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.yes_button))

    @allure.step('Ищем кнопку "Да" и нажимаем на неё')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Ожидаем надписи "Заказ оформлен"')
    def wait_for_load_placed_order_title(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.placed_order_title))

    @allure.step('Проверяем, что надпись "Заказ оформлен" отображается')
    def check_placed_order_title(self):
        element = self.driver.find_element(*self.placed_order_title)
        
        assert element.is_displayed()

    @allure.step('Ищем кнопку "Посмотреть статус" и нажимаем на неё')
    def click_view_status_button(self):
        self.driver.find_element(*self.view_status_button).click() 
