from random import choice
from pages.primary_header import PrimaryHeader
from tests.base_test import BaseTest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from tools.test_tools import get_sorted_list, extract_data, get_item_name, add_to_cart, get_item_price


class ProductsPageTests(BaseTest):

    def test_tc201_sorting_store_items_alphabetically_asc(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        products_names = get_sorted_list(products_page.process_inventory())
        products_page.sort_inventory("az")
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory())
        self.assertEqual(products_names, sorted_items)

    def test_tc202_sorting_store_items_alphabetically_desc(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        products_names = get_sorted_list(products_page.process_inventory(), order="desc")
        products_page.sort_inventory("za")
        products_page.refresh_inventory()
        sorted_items = extract_data(products_page.process_inventory())
        self.assertEqual(products_names, sorted_items)

    def test_tc203_sorting_store_items_prices_asc(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        products_prices = get_sorted_list(products_page.process_inventory(), "v")
        products_page.sort_inventory("lo_hi")
        products_page.refresh_inventory()
        sorted_items_prices = extract_data(products_page.process_inventory(), "v")
        self.assertEqual(products_prices, sorted_items_prices)

    def test_tc204_sorting_store_items_prices_desc(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        products_prices = get_sorted_list(products_page.process_inventory(), "v", "desc")
        products_page.sort_inventory("hi_lo")
        products_page.refresh_inventory()
        sorted_items_prices = extract_data(products_page.process_inventory(), "v")
        self.assertEqual(products_prices, sorted_items_prices)

    def test_tc205_products_page_adds_correct_item_to_cart(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        item_name = get_item_name(item)
        item_price = get_item_price(item)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        primary_header.shopping_cart_button.click()
        cart_page = CartPage(driver)
        cart_item_name = get_item_name(cart_page.cart_list)
        cart_item_price = get_item_price(cart_page.cart_list)
        assert cart_item_name == item_name and cart_item_price == item_price
