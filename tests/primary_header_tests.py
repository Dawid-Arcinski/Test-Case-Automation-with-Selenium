from random import choice
from tools.test_tools import add_to_cart
from pages.login_page import LoginPage
from pages.primary_header import PrimaryHeader
from pages.products_page import ProductsPage
from tests.base_test import BaseTest


class PrimaryHeaderTest(BaseTest):

    def test_tc101_cart_badge_displays_correct_number_after_adding_item(self):
        """
        TC101: cart badge displays correct number after adding item

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. add one random item from the store to cart
        2. check if shopping cart displays badge containing the number of added items

        EXPECTED RESULTS:
        1. shopping cart badge displays "1"
        """
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        self.assertEqual(primary_header.get_cart_counter(), 1)

    def test_tc102_cart_badge_disappears_after_removing_item(self):
        """
        TC102: cart badge disappears after removing item

        PRECONDITIONS:
        1. user logged in
        2. browser opened on website https://www.saucedemo.com/inventory.html

        STEPS:
        1. add one random item from the store to cart
        2. click "remove" button on previously selected item
        3. check if shopping cart displays badge containing the number of added items

        EXPECTED RESULTS:
        1. cart badge disappears
        """
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        add_to_cart(item)
        self.assertEqual(primary_header.get_cart_counter(), "")
