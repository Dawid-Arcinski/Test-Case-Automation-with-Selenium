from pages.base_page import BasePage
from pages.locators import PrimaryHeaderLocators
from pages.locators import ProductsPageLocators
from selenium.webdriver.support.ui import Select


class ProductsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(*PrimaryHeaderLocators.menu)
        self.sort_button = Select(self.driver.find_element(*ProductsPageLocators.sort_button))
        self.sort_az_option = ProductsPageLocators.sort_az_option
        self.sort_za_option = ProductsPageLocators.sort_za_option
        self.sort_low_high_option = ProductsPageLocators.sort_low_high_option
        self.sort_high_low_option = ProductsPageLocators.sort_high_low_option

        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def refresh_inventory(self):
        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def process_inventory(self):
        products = {}
        for item in self.inventory:
            products.update({get_item_name(item): get_item_price(item)})
        return products

    def sort_inventory(self, option):
        self.sort_button.select_by_visible_text(option)


def get_item_name(item):
    return item.find_element(*ProductsPageLocators.store_item_name).text


def get_item_price(item):
    item_price = "".join([c for c in item.find_element(*ProductsPageLocators.store_item_price).text if
                          c.isdigit() or c == "."])
    return float(item_price)
