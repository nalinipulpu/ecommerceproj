from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from selenium.webdriver.support.select import Select


class CustomersPage:
    customer_page_link = "https://admin-demo.nopcommerce.com/Admin/Customer/Create"
    email_textBox_Id = "Email"
    password_textBox_Id = "Password"
    firstname_textBox_Id = "FirstName"
    lastname_textBox_Id = "LastName"
    male_radioButton_id = 'Gender_Male'
    female_radioButton_id = 'Gender_Female'
    dob_textbox_xpath = "//input[@name='DateOfBirth']"
    companyName_textbox_id = "Company"
    is_taxExempt_textbox_id = "IsTaxExempt"

    newsletter_list_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']/preceding::div[1]"
    newsletter_list = ["Your store name", "Test store 2"]

    customer_roles_list_xpath = "//select[@id='SelectedCustomerRoleIds']/preceding::div[1]"

    customer_roles_list = ["Administrators", "Forum Moderators,Guests,Vendors"]

    manager_of_vendor_select_id = "VendorId"
    manager_of_vendor_list = ["Administrators", "Forum Moderators,Guests,Vendors"]

    active_checkbox_id = 'Active'
    admin_comment_textarea_id = "AdminComment"
    save_button_xpath = '//button[@name="save"]'
    save_and_edit_button_xpath = '//button[@name="save-continue"]'

    def __init__(self, driver):
        # self.driver = Chrome(executable_path='')

        self.driver = driver

    def get_customer_page(self):
        self.driver.get(self.customer_page_link)

    def set_email_id(self, mail_id):
        self.driver.find_element(By.ID, self.email_textBox_Id).send_keys(mail_id)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_textBox_Id).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(By.ID, self.firstname_textBox_Id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.ID, self.lastname_textBox_Id).send_keys(last_name)

    def set_gender(self, gender):
        if gender == 'Male' or 'M' or 'male':
            self.driver.find_element(By.ID, self.male_radioButton_id).click()
        else:
            self.driver.find_element(By.ID, self.female_radioButton_id).click()

    def set_DOB(self, DOB):
        self.driver.find_element(By.XPATH, self.dob_textbox_xpath).send_keys(DOB)

    def set_company_name(self, company_name):
        self.driver.find_element(By.ID, self.companyName_textbox_id).send_keys(company_name)

    def click_tax_exempt(self):
        self.driver.find_element(By.ID, self.is_taxExempt_textbox_id).click()

    def set_manager_of_vendor(self, value):

        manager_of_vendor_selector = Select(self.driver.find_element(By.ID, self.manager_of_vendor_select_id))
        manager_of_vendor_selector.select_by_visible_text(value)

    def set_newsletter(self, value):
        self.driver.find_element(By.XPATH, self.newsletter_list_xpath).click()
        sleep(3)
        if value == 'Your store name':

            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Test store 2')]").click()

    def set_customer_roles(self, value):
        self.driver.find_element(By.XPATH, self.customer_roles_list_xpath).click()
        sleep(3)
        if value == 'Administrators':

            self.driver.find_element(By.XPATH, "//li[contains(text(),'Administrators')]").click()
        elif value == 'Forum Moderators':
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Forum Moderators')]").click()
        elif value == 'Guests':
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]").click()
            sleep(2)
            self.driver.find_element(By.XPATH,
                                     "//span[contains(text(),'Registered')]/following-sibling::span[@title='delete']").click()
        elif value == 'Registered':
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Registered')]").click()
        elif value == 'Vendors':
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Vendors')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]").click()

    def click_active(self):
        self.driver.find_element(By.ID, self.active_checkbox_id).click()

    def set_admin_content(self, admin_content):
        self.driver.find_element(By.ID, self.admin_comment_textarea_id).send_keys(admin_content)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
