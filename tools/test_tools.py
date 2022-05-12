import json
from faker import Faker
from pages.locators import ProductsPageLocators


def prepare_test_data(path):
    fake = Faker(locale="pl_PL")
    test_data = json.load(open(path))
    test_data.update({"wrong_password": fake.password(), "wrong_username": fake.user_name(),
                      "first_name": fake.first_name(), "last_name": fake.last_name(), "postal_code": fake.postcode()})
    return test_data


def get_sorted_list(dictionary, option="k", order="asc"):
    result = sorted(extract_data(dictionary, option))
    if order == "desc":
        return list(reversed(result))
    return result


def extract_data(dictionary, option="k"):
    result = dictionary.values() if option == "v" else dictionary.keys()
    return list(result)


def get_item_name(item):
    return item.find_element(*ProductsPageLocators.store_item_name).text


def get_item_price(item):
    item_price = "".join([c for c in item.find_element(*ProductsPageLocators.store_item_price).text if
                          c.isdigit() or c == "."])
    return float(item_price)


def add_to_cart(item):
    item.find_element(*ProductsPageLocators.add_to_cart_btn).click()
