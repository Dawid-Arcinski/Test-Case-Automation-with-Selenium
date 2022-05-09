import unittest
from tests.login_page_tests import LoginPageTest
from tests.products_page_tests import ProductsPageTests

login_page_test = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
product_page_test = unittest.TestLoader().loadTestsFromTestCase(ProductsPageTests)

# tests = [login_page_test, product_page_test]
tests = [product_page_test]

test_suite = unittest.TestSuite(tests)

unittest.TextTestRunner(verbosity=2).run(test_suite)
