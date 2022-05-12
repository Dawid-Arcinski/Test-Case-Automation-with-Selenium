from pages.primary_header import PrimaryHeader
from pages.locators import PrimaryHeaderLocators
from pages.locators import ProductsPageLocators
from selenium.webdriver.support.ui import Select
from tools.test_tools import get_item_name, get_item_price


class ProductsPage(PrimaryHeader):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(*PrimaryHeaderLocators.menu_btn)
        self.sort_button = Select(self.driver.find_element(*ProductsPageLocators.sort_btn))
        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def refresh_inventory(self):
        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def process_inventory(self):
        products = {}
        for item in self.inventory:
            products.update({get_item_name(item): get_item_price(item)})
        return products

    def sort_inventory(self, order="az"):
        options = {"az": ProductsPageLocators.sort_az, "za": ProductsPageLocators.sort_za,
                   "lo_hi": ProductsPageLocators.sort_lo_hi, "hi_lo": ProductsPageLocators.sort_hi_lo}
        self.sort_button.select_by_visible_text(options[order])
