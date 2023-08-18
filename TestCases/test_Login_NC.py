import time

import pytest

from PageObjectModel.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Login:

    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    pwd = ReadConfig.get_password()
    path = "D:\\Software Testing\\TK NopCommerce\\Screenshots\\"
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_login_001(self, setup):
        self.driver = setup
        self.log.info("Starting test_login_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->"+self.url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_email(self.email)
        self.log.info("Entering Email-->"+self.email)
        self.lp.enter_password(self.pwd)
        self.log.info("Entering Password-->"+self.pwd)
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")
        if self.driver.title == "Dashboard / nopCommerce administration":    #self.lp.login_status():
            self.log.info("Page Title Matched--test_login_001 is Passed")
            self.driver.save_screenshot(f"{self.path}test_login_001--Passed.png")
            self.log.info("Saving test_login_001--Passed Screenshot")
            time.sleep(2)
            self.lp.click_logout()
            self.log.info("Clicking on Logout Button")
            assert True
        else:
            self.log.info("Page Title Didn't Match--test_login_001 is Failed")
            self.driver.save_screenshot(f"{self.path}test_login_001--Failed.png")
            self.log.info("Saving test_login_001--Failed Screenshot")
            assert False


    # def test_login_002(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.enter_email(self.email)
    #     self.lp.enter_password(self.pwd)
    #     self.lp.click_login_button()
    #     if self.driver.title == "Dashboard / nopCommerce administration":
    #         self.driver.save_screenshot(f"{self.path}test_login_001--Passed.png")
    #         # time.sleep(2)
    #         self.lp.click_logout()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(f"{self.path}test_login_001--Failed.png")
    #         assert False
