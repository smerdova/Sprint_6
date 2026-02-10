import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import tests.paths as paths

class OrderPage:
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
    view_button = [By.XPATH, ".//div/button[text()='Посмотреть']"]
            
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_first_name_input(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.first_name_input))

    def set_first_name_input(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def set_last_name_input(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def set_adress_input(self, adress):
        self.driver.find_element(*self.adress_input).send_keys(adress)

    def click_metro_station_input(self):
        self.driver.find_element(*self.metro_station_input).click()

    def click_station_input(self):
        self.driver.find_element(*self.station_input).click()
    
    def set_phone_input(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)

    def click_further_button(self):
        self.driver.find_element(*self.further_button).click()

    def wait_for_load_when_input(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.when_input))

    def click_when_input(self):
        self.driver.find_element(*self.when_input).click()

    def set_when_input(self):
        self.driver.find_element(*self.when_input).send_keys(datetime.datetime.now().strftime('%d.%m.%Y'))

    def click_rental_period_input(self):
        element = self.driver.find_element(*self.rental_period_input)
        element.click()

    def click_two_days_input(self):
        self.driver.find_element(*self.two_days_input).click()

    def click_three_days_input(self):
        self.driver.find_element(*self.three_days_input).click()

    def click_black_color_checkbox_input(self):
        self.driver.find_element(*self.black_color_checkbox_input).click()

    def click_grey_color_checkbox_input(self):
        self.driver.find_element(*self.grey_color_checkbox_input).click()

    def set_comment_input(self, comment):
        self.driver.find_element(*self.comment_input).send_keys(comment)

    def click_order_middle_button(self):
        self.driver.find_element(*self.order_middle_button).click()

    def wait_for_load_yes_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.yes_button))

    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    def wait_for_load_placed_order_title(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.placed_order_title))

    def check_placed_order_title(self):
        element = self.driver.find_element(*self.placed_order_title)
        
        assert element.is_displayed()

    def click_view_status_button(self):
        self.driver.find_element(*self.view_status_button).click()

    def wait_for_load_view_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.view_button))

    def check_main_page_scooter(self):
        assert self.driver.current_url == paths.BASE_URL

    
    def check_main_page_dzen(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(paths.URL_DZEN))
