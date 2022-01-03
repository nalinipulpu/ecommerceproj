from time import sleep
from Utilities.ReadConfig import ReadConfig
from PageObjects.LoginPage import Login
from datetime import date
from datetime import datetime
from Utilities.CustomLogger import CustomLogger


# import os


class Test_Login_DDT_002:
    expected_title = 'Your store. Login'
    today = date.today().strftime("%d-%m-%Y")
    secs_mins=datetime.now().strftime("%H:%M:%S")
    l = CustomLogger()
    CustomLogger().logger.info('*********************Test_Login_DDT_002 starts*******************')

    # today=str(today)
    # logger = LogGen.loggen()

    def test_login_ddt(self, setup, login_excel_data):
        CustomLogger().logger.info('*********************test_login_ddt starts*******************')
        self.driver = setup
        self.driver.get(ReadConfig.get_application_URL())
        lp = Login(self.driver)
        for row in range(2, login_excel_data.row_count + 1):
            lp.SetEmailId(login_excel_data.read_cell(row, 1))
            lp.SetPassword(login_excel_data.read_cell(row, 2))
            exp = login_excel_data.read_cell(row, 3)
            sleep(1)
            lp.ClickSubmit()
            sleep(1)
            ls = list()
            if self.driver.title == "Dashboard / nopCommerce administration":
                if exp == "Pass":
                    CustomLogger().logger.info('test_login passed for data set:' + " " + login_excel_data.read_cell(row,
                                                                                                                    1) +" " + login_excel_data.read_cell(
                        row, 2) +" " + login_excel_data.read_cell(row, 3))
                    ls.append('Pass')
                    lp.clickLogout()
                elif exp == "Fail":
                    CustomLogger().logger.info('test_login failed for data set:'" " + login_excel_data.read_cell(row,
                                                                                                                 1) +" " + login_excel_data.read_cell(
                        row, 2) +" " + login_excel_data.read_cell(row, 3))
                    ls.append('Fail')
                    self.driver.get_screenshot_as_file(
                        ".\\Screenshots\\" + self.today + "\\" + self.secs_mins + " test_login_ddt.png")
            else:
                if exp == "Pass":
                    CustomLogger().logger.info('test_login failed for data set:' + " " + login_excel_data.read_cell(row,
                                                                                                                    1) +" " + login_excel_data.read_cell(
                        row, 2) +" " + login_excel_data.read_cell(row, 3))
                    ls.append('Fail')
                    self.driver.get_screenshot_as_file(".\\Screenshots\\" + self.today + "\\"+self.secs_mins+" test_login_ddt.png")

                elif exp == "Fail":
                    CustomLogger().logger.info('test_login passed for data set:' + " " + login_excel_data.read_cell(row,
                                                                                                                    1) +" " + login_excel_data.read_cell(
                        row, 2) +" " + login_excel_data.read_cell(row, 3))
                    ls.append('Pass')

        if "Fail" not in ls:
              CustomLogger().logger.info(
                  "*********************test_login_ddt PASSED for all Test Data Sets *******************")

              self.driver.close()
              assert True
        else:
                CustomLogger().logger.info(
                        "*********************test_login_ddt FAILED  *******************")

                self.driver.close()

                assert False
        CustomLogger().logger.info(
            "********************* END of test_login_ddt *******************")
    CustomLogger().logger.info(
            "********************* Completed Test_Login_DDT_002 *******************")

