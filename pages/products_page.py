from pages.primary_header import PrimaryHeader
from pages.locators import PrimaryHeaderLocators
from pages.locators import ProductsPageLocators
from selenium.webdriver.support.ui import Select


class ProductsPage(PrimaryHeader):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = self.driver.find_element(*PrimaryHeaderLocators.menu_btn)
        self.sort_button = Select(self.driver.find_element(*ProductsPageLocators.sort_btn))
        self.sort_az = ProductsPageLocators.sort_az
        self.sort_za = ProductsPageLocators.sort_za
        self.sort_lo_hi = ProductsPageLocators.sort_lo_hi
        self.sort_hi_lo = ProductsPageLocators.sort_hi_lo
        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def refresh_inventory(self):
        self.inventory = self.driver.find_elements(*ProductsPageLocators.store_item)

    def process_inventory(self):
        products = {}
        for item in self.inventory:
            products.update({ProductsPage.get_item_name(item): ProductsPage.get_item_price(item)})
        return products

    def sort_inventory(self, option):
        self.sort_button.select_by_visible_text(option)

    @staticmethod
    def add_to_cart(item):
        item.find_element(*ProductsPageLocators.add_to_cart_btn).click()

    @staticmethod
    def get_item_name(item):
        return item.find_element(*ProductsPageLocators.store_item_name).text

    @staticmethod
    def get_item_price(item):
        item_price = "".join([c for c in item.find_element(*ProductsPageLocators.store_item_price).text if
                              c.isdigit() or c == "."])
        return float(item_price)
