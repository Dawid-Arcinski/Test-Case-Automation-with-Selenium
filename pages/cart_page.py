from pages.primary_header import PrimaryHeader
from pages.locators import YourCartLocators


class CartPage(PrimaryHeader):

    def __init__(self, driver):
        super().__init__(driver)
        self.cart = self.driver.find_element(*YourCartLocators.cart_list)
        self.continue_shopping = self.driver.find_element(*YourCartLocators.continue_shopping_btn)
        self.continue_shopping = self.driver.find_element(*YourCartLocators.checkout_btn)
