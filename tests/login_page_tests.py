from tests.base_test import BaseTest
from tools import test_tools
from pages.locators import LoginPageLocators
from pages.locators import PrimaryHeaderLocators


class LoginPageTest(BaseTest):

    def test_tc001_loging_in_using_correct_credentials(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["correct_password"])
        driver.find_element(*PrimaryHeaderLocators.menu).click()
        logout_link = driver.find_element(*PrimaryHeaderLocators.menu_logout_link)
        assert logout_link.accessible_name == self.test_data["logout_label"]

    def test_tc002_loging_in_using_wrong_username(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["wrong_username"], self.test_data["correct_password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]

    def test_tc003_loging_in_using_wrong_password(self):
        driver = self.driver
        test_tools.log_user_in(driver, self.test_data["correct_username"], self.test_data["wrong_password"])
        error_message = driver.find_element(*LoginPageLocators.error_message_box).text
        assert error_message == self.test_data["login_error_message"]
