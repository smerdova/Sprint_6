from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
import tests.paths as paths

class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(paths.BASE_URL)
        cls.order_page = OrderPage(cls.driver)
        cls.base_page = BasePage(cls.driver)

    def test_placed_order_first_entry_point_positive_result(self):
        self.base_page.click_order_button()
        self.order_page.wait_for_load_first_name_input()
        self.order_page.set_first_name_input('Тест')
        self.order_page.set_last_name_input('Тестовый')
        self.order_page.set_adress_input('Уральская 12')
        self.order_page.click_metro_station_input()
        self.order_page.click_station_input()
        self.order_page.set_phone_input('+79463448752')
        self.order_page.click_further_button()
        self.order_page.wait_for_load_when_input()
        self.order_page.click_when_input()
        self.order_page.set_when_input()
        self.order_page.click_rental_period_input()
        self.order_page.click_two_days_input()
        self.order_page.click_black_color_checkbox_input()
        self.order_page.set_comment_input('тест')
        self.order_page.click_order_middle_button()
        self.order_page.wait_for_load_yes_button()
        self.order_page.click_yes_button()
        self.order_page.wait_for_load_placed_order_title()
        self.order_page.check_placed_order_title()
        self.order_page.click_view_status_button()
        self.order_page.wait_for_load_view_button()
        self.base_page.click_scooter_logo_button()
        self.order_page.check_main_page_scooter()

    def test_placed_order_second_entry_point_positive_result(self):
        self.base_page.scroll_order_ultrabig_button()
        self.base_page.click_order_ultrabig_button()
        self.order_page.wait_for_load_first_name_input()
        self.order_page.set_first_name_input('Иван')
        self.order_page.set_last_name_input('Иванов')
        self.order_page.set_adress_input('Первомайская 23')
        self.order_page.click_metro_station_input()
        self.order_page.click_station_input()
        self.order_page.set_phone_input('+79348962148')
        self.order_page.click_further_button()
        self.order_page.wait_for_load_when_input()
        self.order_page.click_when_input()
        self.order_page.set_when_input()
        self.order_page.click_rental_period_input()
        self.order_page.click_three_days_input()
        self.order_page.click_grey_color_checkbox_input()
        self.order_page.set_comment_input('комментарий')
        self.order_page.click_order_middle_button()
        self.order_page.wait_for_load_yes_button()
        self.order_page.click_yes_button()
        self.order_page.wait_for_load_placed_order_title()
        self.order_page.check_placed_order_title()
        self.order_page.click_view_status_button()
        self.order_page.wait_for_load_view_button()
        self.base_page.click_yandex_logo_button()
        self.order_page.check_main_page_dzen()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
