from pages.primary_header import PrimaryHeader
from pages.locators import YourCartLocators


class CartPage(PrimaryHeader):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_list = self.driver.find_element(*YourCartLocators.cart_list)

    def go_to_checkout(self, driver):
        driver.find_element(*YourCartLocators.checkout_btn).click()

    def go_back_to_products(self, driver):
        driver.find_element(*YourCartLocators.continue_shopping_btn).click()
