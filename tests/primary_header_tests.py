from random import choice
from tools.test_tools import add_to_cart
from pages.login_page import LoginPage
from pages.primary_header import PrimaryHeader
from pages.products_page import ProductsPage
from tests.base_test import BaseTest


class PrimaryHeaderTest(BaseTest):

    def test_tc101_cart_badge_displays_correct_number_after_adding_item(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        self.assertEqual(primary_header.get_cart_counter(), 1)

    def test_tc102_cart_badge_disappears_after_removing_item(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        add_to_cart(item)
        self.assertEqual(primary_header.get_cart_counter(), "")
