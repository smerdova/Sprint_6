from selenium.webdriver.common.by import By

class BasePage:
    order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    order_ultrabig_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[1]"]
    yandex_logo_button = [By.XPATH, ".//*[@class='Header_LogoYandex__3TSOI']/img[1]"]
    scooter_logo_button = [By.XPATH, ".//*[@class='Header_LogoScooter__3lsAR']/img[1]"]

    def __init__(self, driver):
        self.driver = driver
        
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def scroll_order_ultrabig_button(self):
        element = self.driver.find_element(*self.order_ultrabig_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_order_ultrabig_button(self):
        self.driver.find_element(*self.order_ultrabig_button).click()

    def click_yandex_logo_button(self):
        self.driver.find_element(*self.yandex_logo_button).click()
        
    def click_scooter_logo_button(self):
        self.driver.find_element(*self.scooter_logo_button).click()
    