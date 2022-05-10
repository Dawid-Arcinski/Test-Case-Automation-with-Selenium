from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username = self.driver.find_element(*LoginPageLocators.username)
        self.password = self.driver.find_element(*LoginPageLocators.password)
        self.login_button = self.driver.find_element(*LoginPageLocators.login_button)

    def log_user_in(self, login, password):
        self.username.send_keys(login)
        self.password.send_keys(password)
        self.login_button.click()
