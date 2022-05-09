from tests.base_test import BaseTest
from tools import test_tools
from pages.products_page import ProductsPage
from tools.test_tools import get_sorted_list, extract_data


class ProductsPageTests(BaseTest):

    def test_tc001_sorting_store_items_alphabetically_asc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_names = get_sorted_list(products_page.process_inventory())
        products_page.sort_inventory(products_page.sort_az_option)
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory())
        self.assertEqual(products_names, sorted_items)

    def test_tc002_sorting_store_items_alphabetically_desc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_names = get_sorted_list(products_page.process_inventory(), order="desc")
        products_page.sort_inventory(products_page.sort_za_option)
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory())
        self.assertEqual(products_names, sorted_items)

    def test_tc003_sorting_store_items_prices_asc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_prices = get_sorted_list(products_page.process_inventory(), "v")
        products_page.sort_inventory(products_page.sort_low_high_option)
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory(), "v")
        self.assertEqual(products_prices, sorted_items)

    def test_tc004_sorting_store_items_prices_desc(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        products_page = ProductsPage(driver)
        products_prices = get_sorted_list(products_page.process_inventory(), "v", "desc")
        products_page.sort_inventory(products_page.sort_high_low_option)
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory(), "v")
        self.assertEqual(products_prices, sorted_items)