from selenium.webdriver.common.by import By
import json
from faker import Faker


def prepare_test_data(path):
    fake = Faker(locale="pl_PL")
    test_data = json.load(open(path))
    test_data.update({"wrong_password": fake.password(), "first_name": fake.first_name(), "last_name": fake.last_name(),
                      "postal_code": fake.postcode()})

    return test_data


def log_user_in(driver, login, password):
    driver.find_element(By.ID, "user-name").send_keys(login)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def add_item(element):
    element.find_element(By.CLASS_NAME, "pricebar").find_element(By.TAG_NAME, "button").click()


def get_item_name(element):
    return element.find_element(By.CLASS_NAME, "inventory_item_name").text


def get_item_price(element):
    item_price = ""
    for c in element.find_element(By.CLASS_NAME, "inventory_item_price").text:
        if c.isdigit() or c == ".":
            item_price += c
    return float(item_price)


def fill_out_form(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
