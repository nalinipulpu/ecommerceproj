from time import sleep

import pytest
from selenium.webdriver import Chrome
from PageObjects.LoginPage import Login
from PageObjects.SearchCustomerPage import SearchCustomerPage
from Utilities.CustomLogger import CustomLogger


class TestSearchCustomer:

    @pytest.mark.regression
    def test_search_customer_by_email_001(self, setup):
        driver = setup
        login = Login(driver)
        login.login_as_admin()
        searchpage = SearchCustomerPage(driver)
        searchpage.get_search_customer_page()
        searchpage.set_email('victoria_victoria@nopCommerce.com')
        searchpage.click_search()
        sleep(3)
        if searchpage.search_customer_by_email('victoria_victoria@nopCommerce.com'):
            assert True
        else:
            assert False
