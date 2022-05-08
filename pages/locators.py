from selenium.webdriver.common.by import By


class LoginPageLocators:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message_box = (By.TAG_NAME, "h3")


class WebStorePageLocators:
    menu = (By.ID, "react-burger-menu-btn")
    menu_logout_link = (By.ID, "logout_sidebar_link")
    store_item = (By.CLASS_NAME, "inventory_item")
