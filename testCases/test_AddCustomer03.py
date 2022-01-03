import random
import string
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import Login
from PageObjects.CustomersPage import CustomersPage
from Utilities.CustomLogger import CustomLogger
from Utilities import ExcelUtils
from Utilities.ReadConfig import ReadConfig
import pytest


class TestAddCustomers003:
    expected_confirmation='The new customer has been added successfully.'

    def test_add_new_customer(self, setup):
        driver=setup
        # driver = Chrome()
        login = Login(driver)
        customerPage = CustomersPage(driver)
        driver.get(ReadConfig.application_URL)
        login.SetEmailId(ReadConfig.user_email)
        login.SetPassword(ReadConfig.user_password)
        login.ClickSubmit()

        customerPage.get_customer_page()

        customerPage.set_email_id(random_generator()+'@gmail.com')
        customerPage.set_password('nalini')
        sleep(1)
        customerPage.set_first_name('Nalini')
        sleep(1)
        customerPage.set_last_name('pulpu')
        sleep(1)
        customerPage.set_gender('female')
        sleep(1)
        customerPage.set_DOB('12/8/1991')
        sleep(1)
        customerPage.set_company_name('oracle')
        sleep(1)
        customerPage.click_tax_exempt()
        sleep(1)

        customerPage.set_newsletter('Test store 2')
        customerPage.set_manager_of_vendor('Vendor 2')
        sleep(1)
        customerPage.set_customer_roles('Guests')
        customerPage.set_admin_content('new customer nalini')
        customerPage.click_save()
        msg=driver.find_element(By.TAG_NAME,"body").text
        if self.expected_confirmation in msg:
            CustomLogger.logger.info("The new customer has been added successfully.")
            assert True

        else:
            CustomLogger.logger.info("The new customer is not created")
            assert False



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))
