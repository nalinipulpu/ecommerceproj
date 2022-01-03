from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from Utilities.ReadConfig import ReadConfig

class Login:
    emailId_textbox_Xpath = "//input[@id='Email']"
    password_textbox_Id = "Password"
    submit_button_Xpath = "//button[contains(text(),'Log in')]"
    logout_link_linkText = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        # self.driver = Chrome()
        self.driver = driver

    def SetEmailId(self, username):
        self.driver.find_element(By.XPATH, self.emailId_textbox_Xpath).clear()
        self.driver.find_element(By.XPATH, self.emailId_textbox_Xpath).send_keys(username)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_Id).clear()
        self.driver.find_element(By.ID, self.password_textbox_Id).send_keys(password)

    def ClickSubmit(self):
        self.driver.find_element(By.XPATH, self.submit_button_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_link_linkText).click()

    def login_as_admin(self):
        self.driver.get(ReadConfig.application_URL)
        self.SetEmailId(ReadConfig.user_email)
        self.SetPassword(ReadConfig.user_password)
        self.ClickSubmit()


