import unittest
from tests.login_page_tests import LoginPageTest
from tests.primary_header_tests import PrimaryHeaderTest
from tests.products_page_tests import ProductsPageTests


login_page_test = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
primary_header_test = unittest.TestLoader().loadTestsFromTestCase(PrimaryHeaderTest)
product_page_test = unittest.TestLoader().loadTestsFromTestCase(ProductsPageTests)

tests = [login_page_test, primary_header_test, product_page_test]

test_suite = unittest.TestSuite(tests)

unittest.TextTestRunner(verbosity=2).run(test_suite)
