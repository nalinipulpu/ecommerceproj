from time import sleep
from Utilities.ReadConfig import ReadConfig
from PageObjects.LoginPage import Login
from datetime import date
from Utilities.CustomLogger import CustomLogger
# import os


class Test_Login_001:
    expected_title = 'Your store. Login'
    today = date.today().strftime("%d-%m-%Y")
    l=CustomLogger()
    CustomLogger().logger.info('*********************Test_001_Login*******************')

    # today=str(today)
    # logger = LogGen.loggen()

    def test_homepage_title(self, setup,login_excel_data):
        CustomLogger().logger.info('*********************Verifying home page Title*******************')
        self.driver = setup
        self.driver.get(ReadConfig.application_URL)
        actual_title = self.driver.title
        if actual_title == self.expected_title:
            CustomLogger().logger.info('test_homepage_title Passed ')


            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + self.today + "\\test_homepageTitle.png")
            CustomLogger().logger.error('test_homepage_title Failed ')

            self.driver.close()
            assert False

    def test_login(self, setup):
        CustomLogger().logger.info('*********************test_login starts*******************')
        self.driver = setup
        self.driver.get(ReadConfig.application_URL)
        lp = Login(self.driver)
        lp.SetEmailId(ReadConfig.user_email)
        lp.SetPassword(ReadConfig.user_password)
        sleep(2)
        lp.ClickSubmit()
        sleep(2)
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.close()
            CustomLogger().logger.info('test_login Passed ')
            assert True

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + self.today + "\\test_Login.png")
            self.driver.close()
            print(self.today)
            CustomLogger().logger.error('test_login Failed ')
            assert False

