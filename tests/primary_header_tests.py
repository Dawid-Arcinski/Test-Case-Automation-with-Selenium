from random import choice
from tools.test_tools import add_to_cart
from pages.login_page import LoginPage
from pages.primary_header import PrimaryHeader
from pages.products_page import ProductsPage
from tests.base_test import BaseTest


class PrimaryHeaderTest(BaseTest):

    def test_tc101_cart_badge_displays_correct_number(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        products_page = ProductsPage(driver)
        item = choice(products_page.inventory)
        add_to_cart(item)
        primary_header = PrimaryHeader(driver)
        assert primary_header.get_cart_counter() == 1
