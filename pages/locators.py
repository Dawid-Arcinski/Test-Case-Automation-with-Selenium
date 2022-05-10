from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message_box = (By.TAG_NAME, "h3")


class PrimaryHeaderLocators:
    menu = (By.ID, "react-burger-menu-btn")
    menu_logout_link = (By.ID, "logout_sidebar_link")
    shopping_cart_button = (By.CLASS_NAME, "shopping_cart_link")


class ProductsPageLocators:
    store_item = (By.CLASS_NAME, "inventory_item")
    store_item_name = (By.CLASS_NAME, "inventory_item_name")
    store_item_price = (By.CLASS_NAME, "inventory_item_price")
    add_to_cart_button = (By.TAG_NAME, "button")

    sort_button = (By.TAG_NAME, "select")
    sort_az_option = "Name (A to Z)"
    sort_za_option = "Name (Z to A)"
    sort_low_high_option = "Price (low to high)"
    sort_high_low_option = "Price (high to low)"


class YourCartLocators:
    cart_item = (By.CLASS_NAME, "cart_item")
