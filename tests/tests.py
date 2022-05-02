import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from random import choice
from tools import utilities

# TEST DATA:
test_data = utilities.prepare_test_data("../data/test_data.json")


class DemoWebsiteTest(unittest.TestCase):
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.get(test_data["base_url"])

    def tearDown(self):
        self.driver.quit()

    def test_case_1(self):
        """TITLE: loging in using correct credentials

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/

        EXPECTED RESULTS:
        1. user is logged in"""

        # STEPS:
        driver = self.driver
        # 1. verify whether "Username" field is displayed and enabled, then enter correct username
        username_field = driver.find_element(By.ID, "user-name")
        assert username_field.is_displayed() and username_field.is_enabled()
        username_field.send_keys(test_data["correct_login"])
        # 2. verify whether "Password" field is displayed and enabled, then enter correct password
        password_field = driver.find_element(By.ID, "password")
        assert password_field.is_displayed() and password_field.is_enabled()
        password_field.send_keys(test_data["correct_password"])
        # 3. verify whether "Login" button is displayed and enabled, then click it
        login_button = driver.find_element(By.ID, "login-button")
        assert login_button.is_displayed() and login_button.is_enabled()
        login_button.click()
        # 4. confirm that user is logged in by verifying that shopping cart button is displayed and enabled
        shopping_cart_button = driver.find_element(By.ID, "shopping_cart_container")
        assert shopping_cart_button.is_displayed() and shopping_cart_button.is_enabled()

    def test_case_2(self):
        """ TITLE: attempting to log in using incorrect password

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/

        EXPECTED RESULTS:
        1. user is not logged in
        2. webpage displays prompt 'Epic sadface: Username and password do not match any user in this service'"""

        # STEPS:
        driver = self.driver
        # 1. enter correct username in "Username" field
        driver.find_element(By.ID, "user-name").send_keys(test_data["correct_login"])
        # 2. enter wrong password in "Password" field
        driver.find_element(By.ID, "password").send_keys(test_data["wrong_password"])
        # 3. click "Login" button
        driver.find_element(By.ID, "login-button").click()
        # 4. confirm that user is not logged in by verifying that website displays error message:
        # 'Epic sadface: Username and password do not match any user in this service'
        error_message = driver.find_element(By.TAG_NAME, "h3")
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    def test_case_3(self):
        """ TITLE: buying random item from the store

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/
        2. user logged in

        EXPECTED RESULTS:
        1. after completing purchase website displays message 'THANK YOU FOR YOUR ORDER'"""

        # STEPS:
        driver = self.driver
        utilities.log_user_in(driver, test_data["correct_login"], test_data["correct_password"])
        # 1. choose random item to buy and save its name to variable
        item_list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        item = choice(item_list)
        item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_to_cart_button = item.find_element(By.CLASS_NAME, "pricebar").find_element(By.TAG_NAME, "button")
        # 2. verify whether "ADD TO CART" button is displayed and enabled, then click it
        assert add_to_cart_button.is_displayed() and add_to_cart_button.is_enabled()
        add_to_cart_button.click()
        # 3. verify that "ADD TO CART" button was replaced with "REMOVE" button, check if "REMOVE" button is
        # displayed and enabled
        remove_button = item.find_element(By.TAG_NAME, "button")
        assert remove_button.text == "REMOVE"
        assert remove_button.is_displayed() and remove_button.is_enabled()
        # 4. verify, that badge representing number of selected items (1) is displayed on shopping cart icon
        shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_badge = shopping_cart.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert shopping_cart_badge.text == "1"
        # 5. open shopping cart
        shopping_cart.click()
        # 6. verify that shopping list is not empty and that name of item in shopping list corresponds to name of item
        # chosen in step 1.
        shopping_list = driver.find_element(By.CLASS_NAME, "cart_list")
        assert shopping_list.find_elements(By.CLASS_NAME, "cart_item")
        assert shopping_list.find_element(By.CLASS_NAME, "inventory_item_name").text == item_name
        # 7. verify that "CHECKOUT" button is displayed and enabled, then click it
        checkout_button = driver.find_element(By.ID, "checkout")
        assert checkout_button.is_displayed() and checkout_button.is_enabled()
        checkout_button.click()
        # 8. on "YOUR INFORMATION" page verify whether "First Name" field is displayed and enabled,
        # then enter first name
        first_name_field = driver.find_element(By.ID, "first-name")
        assert first_name_field.is_displayed() and first_name_field.is_enabled()
        # first_name_field.send_keys(test_data["first_name"])
        # 9. verify whether "Last Name" field is displayed and enabled, then enter last name
        last_name_field = driver.find_element(By.ID, "last-name")
        assert last_name_field.is_displayed() and last_name_field.is_enabled()
        # last_name_field.send_keys(test_data["last_name"])
        # 10. verify whether "Zip/Postal Code" field is displayed and enabled, then enter postal code
        postal_code_field = driver.find_element(By.ID, "postal-code")
        assert postal_code_field.is_displayed() and postal_code_field.is_enabled()
        # 11.
        utilities.fill_out_form(driver, test_data["first_name"], test_data["last_name"], test_data["postal_code"])
        # 12. verify whether "CONTINUE" button is displayed and enabled, then click it
        continue_button = driver.find_element(By.ID, "continue")
        assert continue_button.is_displayed() and continue_button.is_enabled()
        continue_button.click()
        # 13. check if item selected in step 1. is displayed in checkout overview
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == item_name
        # 14. check if "FINISH" button is displayed and enabled, then click it
        finish_button = driver.find_element(By.ID, "finish")
        assert finish_button.is_displayed() and finish_button.is_enabled()
        finish_button.click()
        # 15. verify whether after finalizing purchase website displays correct messages
        message_top = driver.find_element(By.CLASS_NAME, "complete-header")
        message_bottom = driver.find_element(By.CLASS_NAME, "complete-text")
        assert message_top.text == test_data["thank_you_header"]
        assert message_bottom.text == test_data["thank_you_message"]

    def test_case_4(self):
        """ TITLE: attempting to add multiple random items from the store to shopping cart

        PRECONDITIONS:
        1. browser opened on website https://www.saucedemo.com/
        2. user logged in

        EXPECTED RESULTS:
        1. names of items selected in the store correspond to names of items displayed on CHECKOUT OVERVIEW page
        2. total price of selected items (before tax) in checkout overview corresponds to value """

        # STEPS:
        driver = self.driver
        utilities.log_user_in(driver, test_data["correct_login"], test_data["correct_password"])
        # 1. choose random items, add them to shopping cart and save them to list
        item_list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        item_quantity = 4
        selected_items = []
        for i in range(item_quantity):
            selected_items.append(item_list.pop(item_list.index(choice(item_list))))
        # 2. save selected items' names to variable
        item_names = [utilities.get_item_name(item) for item in selected_items]
        item_names.sort()
        # 3. calculate combined price of selected items and save it to variable
        shopping_cart_value = sum([utilities.get_item_price(item) for item in selected_items])
        # 4. add selected items to shopping cart
        for item in selected_items:
            utilities.add_item(item)
        # 5. move to "YOUR CART" page by clicking shopping cart icon
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        # 6. move to "YOUR INFORMATION" page by clicking "CHECKOUT" button
        driver.find_element(By.ID, "checkout").click()
        # 7. fill out "First Name", "Last Name" and "Zip/Postal Code" fields
        utilities.fill_out_form(driver, test_data["first_name"], test_data["last_name"], test_data["postal_code"])
        # 8. move to "CHECKOUT OVERVIEW" page by clicking "CONTINUE" button
        driver.find_element(By.ID, "continue").click()
        # 9. verify that items displayed on "CHECKOUT OVERVIEW" page correspond to names on the list created in step 2
        checkout_items = [utilities.get_item_name(item) for item in driver.find_elements(By.CLASS_NAME, "cart_item")]
        checkout_items.sort()
        assert checkout_items == item_names
        # 10. verify that total price of selected items (before tax) in corresponds to value calculated in step 3
        checkout_value = sum(
            [utilities.get_item_price(item) for item in driver.find_elements(By.CLASS_NAME, "cart_item")])
        assert shopping_cart_value == checkout_value
