from selenium.webdriver import Chrome
import time

from selenium.webdriver.common.by import By


class SearchCustomerPage:
    email_textbox_id = "SearchEmail"
    firstname_textbox_id = 'SearchEmail'
    lastname_textbox_id = "SearchLastName"
    company_textbox_id = "SearchCompany"
    IPAddress_textbox_id = "SearchIpAddress"
    DOB_month_select_id = "SearchMonthOfBirth"
    DOB_day_select_id = "SearchDayOfBirth"
    search_button_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    row_xpath = "//table[@id='customers-grid']/tbody/tr"
    column_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
        # self.driver = Chrome()


    def get_search_customer_page(self):
        self.driver.get('https://admin-demo.nopcommerce.com/Admin/Customer/List')

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element(By.ID, self.firstname_textbox_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.ID, self.lastname_textbox_id).send_keys(last_name)

    def click_search(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def search_customer_by_name(self, name):
        # self.driver.find_elements()
        row_count = len(self.driver.find_elements(By.XPATH, self.row_xpath))
        for i in range(1, row_count + 2):
            act_name = self.driver.find_element(By.XPATH,
                                                "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[3]").text
            if act_name == name:
                flag = 'True'
                break
        return flag

    def search_customer_by_email(self, email):
        row_count = len(self.driver.find_elements(By.XPATH, self.row_xpath))
        for i in range(1, row_count + 2):
            act_email = self.driver.find_element(By.XPATH,
                                                 "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[2]").text
            if act_email == email:
                flag = 'True'
                break
        return flag
