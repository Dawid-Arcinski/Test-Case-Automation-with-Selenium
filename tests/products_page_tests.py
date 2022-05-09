from tests.base_test import BaseTest
from tools import test_tools
from pages.products_page import ProductsPage


class ProductsPageTests(BaseTest):

    def test_tc001_sorting_store_items_alphabetically_asc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_names = list(products_page.process_inventory().keys())
        products_names.sort()
        products_page.sort_inventory(products_page.sort_az_option)
        products_page.refresh_inventory()
        sorted_items = list(products_page.process_inventory().keys())
        self.assertEqual(products_names, sorted_items)

    def test_tc002_sorting_store_items_alphabetically_desc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_names = list(products_page.process_inventory().keys())
        products_names.sort()
        products_names = products_names[::-1]
        products_page.sort_inventory(products_page.sort_za_option)
        products_page.refresh_inventory()
        sorted_items = list(products_page.process_inventory().keys())
        self.assertEqual(products_names, sorted_items)

    def test_tc003_sorting_store_items_prices_asc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_prices = list(products_page.process_inventory().values())
        products_prices.sort()
        products_page.sort_inventory(products_page.sort_low_high_option)
        products_page.refresh_inventory()
        sorted_items = list(products_page.process_inventory().values())
        self.assertEqual(products_prices, sorted_items)

    def test_tc004_sorting_store_items_prices_desc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_prices = list(products_page.process_inventory().values())
        products_prices.sort()
        products_prices = products_prices[::-1]
        products_page.sort_inventory(products_page.sort_high_low_option)
        products_page.refresh_inventory()
        sorted_items = list(products_page.process_inventory().values())
        self.assertEqual(products_prices, sorted_items)



