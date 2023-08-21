import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjectModel.AddCust_POM import AddCustomer
from PageObjectModel.EmpSearch_POM import EmployeeSearch
from PageObjectModel.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Emp_Search:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    fname = ReadConfig.get_fname()
    path = "D:\\Software Testing\\TK NopCommerce\\Screenshots\\"

    @pytest.mark.sanity
    @allure.description("This testcase verifies search functionality of the application")
    @allure.link("https://admin-demo.nopcommerce.com")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Employee Search Testcase")
    def test_Emp_Search_001(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.ac = AddCustomer(self.driver)
        self.es = EmployeeSearch(self.driver)
        self.log = LogGenerator.log_gen()

        self.log.info("Starting test_login_001")
        self.log.info("Launching Browser")
        self.driver.get(self.url)
        self.log.info("Going to this URL-->" + self.url)
        self.lp.enter_email(self.email)
        self.log.info("Entering Email-->" + self.email)
        self.lp.enter_password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.click_login_button()
        self.log.info("Clicking on Login Button")

        self.ac.click_customers_dropdown()
        self.log.info("Clicking on Customers Dropdown Menu")
        self.ac.click_customers()
        self.log.info("Clicking on Customers option in Dropdown Menu")

        self.es.enter_fname(self.fname)
        self.log.info("Entering Firstname-->"+self.fname)
        self.es.click_search_button()
        self.log.info("Clicking on search button")
        if self.es.search_result_status():
            self.driver.save_screenshot(f"{self.path}test_Emp_Search_001--Passed.png")
            self.log.info("Saving screenshot for test_Emp_Search_001--Passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Pass-SS", attachment_type=AttachmentType.PNG)
            time.sleep(5)
            self.lp.click_logout()
            self.log.info("Clicking on logout button")
            assert True
        else:
            self.driver.save_screenshot(f"{self.path}test_Emp_Search_001--Failed.png")
            self.log.info("Saving screenshot for test_Emp_Search_001--Failed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Fail-SS", attachment_type=AttachmentType.PNG)
            self.lp.click_logout()
            self.log.info("Clicking on logout button")
            assert False
