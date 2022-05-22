from pages.login_page import LoginPage
from tests.base_test import BaseTest
from pages.locators import LoginPageLocators
from pages.locators import PrimaryHeaderLocators


class LoginPageTest(BaseTest):

    def test_tc001_loging_in_using_correct_credentials(self):
        """
        TC001: loging in using correct credentials

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/

        STEPS:
        1. enter correct username
        2. enter correct password
        3. click login button

        EXPECTED RESULTS:
        1. user is logged in
        """
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["password"])
        driver.find_element(*PrimaryHeaderLocators.menu_btn).click()
        logout_link = driver.find_element(*PrimaryHeaderLocators.logout_link)
        assert logout_link.accessible_name == self.test_data["logout_label"]

    def test_tc002_loging_in_using_wrong_username(self):
        """
        TC002: loging in using wrong username

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/

        STEPS:
        1. enter wrong username
        2. enter correct password
        3. click login button

        EXPECTED RESULTS:
        1. user is not logged in
        2. webpage displays message 'Epic sadface: Username and password do not match any user in this service'
        """
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["wrong_username"], self.test_data["password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]

    def test_tc003_loging_in_using_wrong_password(self):
        """
        TC003: loging in using wrong password

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/

        STEPS:
        1. enter correct username
        2. enter wrong password
        3. click login button

        EXPECTED RESULTS:
        1. user is not logged in
        2. webpage displays message 'Epic sadface: Username and password do not match any user in this service'
        """
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.log_user_in(self.test_data["username"], self.test_data["wrong_password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]
