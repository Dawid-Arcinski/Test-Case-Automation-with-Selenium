import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tools.test_tools import prepare_test_data


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.test_data = prepare_test_data("data/test_data.json")
        s = Service(ChromeDriverManager().install())
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.get(self.test_data["base_url"])

    def tearDown(self):
        self.driver.quit()
