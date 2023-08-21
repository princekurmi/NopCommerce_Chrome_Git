import time

import pytest

from PageObjectModel.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Login_Params:
    url = ReadConfig.get_url()
    path = "D:\\Software Testing\\TK NopCommerce\\Screenshots\\"
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_login_params_001(self, setup, getDataForLogin):
        self.driver = setup
        self.log.info("Starting test_login_params_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp = LoginPage(self.driver)

        self.lp.enter_email(getDataForLogin[0])
        self.log.info("Entering Email-->" + getDataForLogin[0])
        self.lp.enter_password(getDataForLogin[1])
        self.log.info("Entering Password-->" + getDataForLogin[1])
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")

        status_list = []
        if self.driver.title == "Dashboard / nopCommerce administration":  # self.lp.login_status():
            if getDataForLogin[2] == "Pass":
                status_list.append("Pass")
                self.log.info("Page Title Matched--test_login_params_001 is Passed")
                self.driver.save_screenshot(f"{self.path}test_login_params_001--Passed.png")
                self.log.info("Saving test_login_params_001--Passed Screenshot")
                time.sleep(2)
                self.lp.click_logout()
                self.log.info("Clicking on Logout Button")
            elif getDataForLogin[2] == "Fail":
                status_list.append("Fail")
                self.log.info("Page Title Matched--test_login_params_001 is Failed")
                self.driver.save_screenshot(f"{self.path}test_login_params_001--Failed.png")
                self.log.info("Saving test_login_params_001--Failed Screenshot")
        else:
            if getDataForLogin[2] == "Pass":
                status_list.append("Fail")
                self.log.info("Page Title Didn't Match--test_login_params_001 is Failed")
                self.driver.save_screenshot(f"{self.path}test_login_params_001--Failed.png")
                self.log.info("Saving test_login_params_001--Failed Screenshot")
            elif getDataForLogin[2] == "Fail":
                status_list.append("Pass")
                self.log.info("Page Title Matched--test_login_params_001 is Passed")
                self.driver.save_screenshot(f"{self.path}test_login_params_001--Passed.png")
                self.log.info("Saving test_login_params_001--Passed Screenshot")

        print(status_list)
        if "Fail" not in status_list:
            assert True
        else:
            assert False
