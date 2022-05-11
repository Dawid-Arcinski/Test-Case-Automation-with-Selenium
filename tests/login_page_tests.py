import unittest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.locators import LoginPageLocators
from pages.locators import PrimaryHeaderLocators


class LoginPageTest(BaseTest):

    def test_tc001_loging_in_using_correct_credentials(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        driver.find_element(*PrimaryHeaderLocators.menu_btn).click()
        logout_link = driver.find_element(*PrimaryHeaderLocators.logout_link)
        assert logout_link.accessible_name == self.test_data["logout_label"]

    def test_tc002_loging_in_using_wrong_username(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["wrong_username"], self.test_data["password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]

    def test_tc003_loging_in_using_wrong_password(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["wrong_password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]
