from pages.base_page import BasePage
from pages.locators import PrimaryHeaderLocators


class PrimaryHeader(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(*PrimaryHeaderLocators.menu)
        self.logout_link = self.driver.find_element(*PrimaryHeaderLocators.menu_logout_link)
        self.shopping_cart_button = self.driver.find_element(*PrimaryHeaderLocators.shopping_cart_button)
