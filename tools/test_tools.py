from selenium.webdriver.common.by import By
import json
from faker import Faker
from pages.locators import LoginPageLocators


def prepare_test_data(path):
    fake = Faker(locale="pl_PL")
    test_data = json.load(open(path))
    test_data.update({"wrong_password": fake.password(), "wrong_username": fake.user_name(),
                      "first_name": fake.first_name(), "last_name": fake.last_name(), "postal_code": fake.postcode()})
    return test_data


def log_user_in(driver, login, password):
    driver.find_element(*LoginPageLocators.username).send_keys(login)
    driver.find_element(*LoginPageLocators.password).send_keys(password)
    driver.find_element(*LoginPageLocators.login_button).click()


def get_sorted_list(dictionary, option="k", order="asc"):
    result = sorted(extract_data(dictionary, option))
    if order == "desc":
        return list(reversed(result))
    return result


def extract_data(dictionary, option="k"):
    result = dictionary.values() if option == "v" else dictionary.keys()
    return list(result)

#
#
# def fill_out_form(driver, first_name, last_name, postal_code):
#     driver.find_element(By.ID, "first-name").send_keys(first_name)
#     driver.find_element(By.ID, "last-name").send_keys(last_name)
#     driver.find_element(By.ID, "postal-code").send_keys(postal_code)
