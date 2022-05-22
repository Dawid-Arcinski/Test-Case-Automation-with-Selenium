from random import choice
from pages.primary_header import PrimaryHeader
from tests.base_test import BaseTest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from tools.test_tools import get_sorted_list, extract_data, get_item_name, add_to_cart, get_item_price


class ProductsPageTests(BaseTest):

    def test_tc201_sorting_store_items_alphabetically_asc(self):
        """
        TC201: sorting store items alphabetically in ascending order

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. click sort button
        2. choose option "Name (A to Z)"

        EXPECTED RESULTS:
        1. products are sorted alphabetically in ascending order
        """
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
        """
        TC202: sorting store items alphabetically in descending order

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. click sort button
        2. choose option "Name (Z to A)"

        EXPECTED RESULTS:
        1. products are sorted alphabetically in descending order
        """
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
        """
        TC203: sorting store items' prices in ascending order

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. click sort button
        2. choose option "Price (low to high)"

        EXPECTED RESULTS:
        1. products' prices are sorted in ascending order
        """
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
        """
        TC204: sorting store items' prices in descending order

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. click sort button
        2. choose option "Price (high to low)"

        EXPECTED RESULTS:
        1. products' prices are sorted in descending order
        """
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
        """
        TC205: products page adds correct item to cart

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. add one random item from the store to cart
        2. click shopping cart button

        EXPECTED RESULTS:
        1. name of the product selected from the store corresponds to name of product in shopping cart
        2. price of the product selected from the store corresponds to price of product in shopping cart
        """
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
