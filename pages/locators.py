from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_message_box = (By.TAG_NAME, "h3")


class PrimaryHeaderLocators:
    menu_btn = (By.ID, "react-burger-menu-btn")
    close_menu_btn = (By.ID, "react-burger-cross-btn")
    logout_link = (By.ID, "logout_sidebar_link")
    shopping_cart_btn = (By.ID, "shopping_cart_container")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")


class ProductsPageLocators:
    store_item = (By.CLASS_NAME, "inventory_item")
    store_item_name = (By.CLASS_NAME, "inventory_item_name")
    store_item_price = (By.CLASS_NAME, "inventory_item_price")
    add_to_cart_btn = (By.TAG_NAME, "button")

    sort_btn = (By.TAG_NAME, "select")
    sort_az = "Name (A to Z)"
    sort_za = "Name (Z to A)"
    sort_lo_hi = "Price (low to high)"
    sort_hi_lo = "Price (high to low)"


class YourCartLocators:
    cart_list = (By.CLASS_NAME, "cart_list")
    cart_item = (By.CLASS_NAME, "cart_item")
    continue_shopping_btn = (By.ID, "continue-shopping")
    checkout_btn = (By.ID, "checkout")
