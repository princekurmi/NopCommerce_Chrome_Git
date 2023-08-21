import time

import pytest

from PageObjectModel.Login_POM import LoginPage
from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig
from Utilities.XLutils import getRowCount


class Test_Login_DDT:
    url = ReadConfig.get_url()
    sspath = "D:\\Software Testing\\TK NopCommerce\\Screenshots\\"
    log = LogGenerator.log_gen()
    xlpath = "D:\\Software Testing\\TK NopCommerce\\TestCases\\TestData\\LoginDataNopCommerce.xlsx"

    @pytest.mark.sanity
    def test_login_ddt_001(self, setup):
        self.driver = setup
        self.log.info("Starting test_login_ddt_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp = LoginPage(self.driver)

        row_count = getRowCount(self.xlpath, "Sheet1")
        status_list = []
        for row in range(2, row_count + 1):
            self.email = XLutils.readData(self.xlpath, "Sheet1", row, 2)
            self.pwd = XLutils.readData(self.xlpath, "Sheet1", row, 3)
            self.expected_result = XLutils.readData(self.xlpath, "Sheet1", row, 4)
            self.scenario = XLutils.readData(self.xlpath, "Sheet1", row, 6)
            self.lp.enter_email(self.email)
            self.log.info("Entering Email-->" + self.email)
            self.lp.enter_password(self.pwd)
            self.log.info("Entering Password-->" + self.pwd)
            time.sleep(2)
            self.lp.click_login_button()
            self.log.info("Clicking on Login Button")
            time.sleep(2)
            if self.driver.title == "Dashboard / nopCommerce administration":  # self.lp.login_status():
                if self.expected_result == "Pass":
                    status_list.append("Pass")
                    self.log.info("Page Title Matched--test_login_ddt_001 is Passed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Passed.png")
                    self.log.info("Saving test_login_ddt_001--Passed Screenshot")
                    time.sleep(2)
                    self.lp.click_logout()
                    self.log.info("Clicking on Logout Button")
                elif self.expected_result == "Fail":
                    status_list.append("Fail")
                    self.log.info("Page Title Didn't Match--test_login_ddt_001 is Failed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Failed.png")
                    self.log.info("Saving test_login_ddt_001--Failed Screenshot")

            else:
                if self.expected_result == "Pass":
                    status_list.append("Fail")
                    self.log.info("Page Title Didn't Match--test_login_ddt_001 is Failed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Failed.png")
                    self.log.info("Saving test_login_ddt_001--Failed Screenshot")
                elif self.expected_result == "Fail":
                    status_list.append("Pass")
                    self.log.info("Page Title Didn't Match--test_login_ddt_001 is Passed")
                    self.driver.save_screenshot(f"{self.sspath}test_login_ddt_001--{self.scenario}--Passed.png")
                    self.log.info("Saving test_login_ddt_001--Passed Screenshot")

        if "Fail" not in status_list:
            self.log.info("test_login_ddt_001 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_001 is Failed")
            assert False
        self.log.info("test_login_ddt_001 is Completed")
