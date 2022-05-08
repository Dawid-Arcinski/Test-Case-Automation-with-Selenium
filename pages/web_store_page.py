from pages.base_page import BasePage
from pages.locators import WebStorePageLocators


class WebStorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(*WebStorePageLocators.menu)

