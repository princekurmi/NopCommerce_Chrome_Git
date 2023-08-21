import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjectModel.AddCust_POM import AddCustomer
from PageObjectModel.Login_POM import LoginPage
from Utilities.Logger import LogGenerator
from Utilities.ReadProperties import ReadConfig


class Test_Add_Cust:
    url = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    mail = ReadConfig.get_mail()
    pwd = ReadConfig.get_pwd()
    fname = ReadConfig.get_firstname()
    lname = ReadConfig.get_lastname()
    dob = ReadConfig.get_dob()
    company = ReadConfig.get_company()
    comment = ReadConfig.get_comment()
    path = "D:\\Software Testing\\TK NopCommerce\\Screenshots\\"

    @pytest.mark.sanity
    @allure.description("This testcase verifies login functionality of the application")
    @allure.link("https://admin-demo.nopcommerce.com")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Add_Cust_001(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.ac = AddCustomer(self.driver)
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
        self.ac.click_addnew_btn()
        self.log.info("Clicking on Add New Button")
        self.ac.enter_email(self.mail)
        self.log.info("Entering new Customer's Email")
        self.ac.enter_password(self.pwd)
        self.log.info("Entering new Customer's Password")
        self.ac.enter_firstname(self.fname)
        self.log.info("Entering new Customer's Firstname")
        self.ac.enter_lastname(self.lname)
        self.log.info("Entering new Customer's Lastname")
        self.ac.click_radio_male()
        self.log.info("Clicking on 'Male' radio Button")
        self.ac.enter_dob(self.dob)
        self.log.info("Entering DOB of new Customer")
        self.ac.enter_company(self.company)
        self.log.info("Entering new Customer's Company Name")
        self.ac.check_tax()
        self.log.info("Clicking on 'Tax' checkbox")
        self.ac.drop_newsletter()
        self.log.info("Choosing option from newsletter dropdown")
        self.ac.drop_roles()
        self.log.info("Choosing option from roles dropdown")
        self.ac.drop_vendor()
        self.log.info("Choosing option vendor dropdown")
        self.ac.check_active()
        self.log.info("Clicking on 'active' checkbox")
        self.ac.enter_comment(self.comment)
        self.log.info("Entering comment for new Customer")
        time.sleep(5)
        self.ac.click_save()
        self.log.info("Clicking on save button")
        if self.ac.save_status():
            self.driver.save_screenshot(f"{self.path}test_Add_Cust_001--Passed.png")
            self.log.info("Saving screenshot for test_Add_Cust_001--Passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="Pass-SS", attachment_type=AttachmentType.PNG)
            self.lp.click_logout()
            self.log.info("Clicking on logout button")
            assert True
        else:
            self.driver.save_screenshot(f"{self.path}test_Add_Cust_001--Failed.png")
            self.log.info("Saving screenshot for test_Add_Cust_001--Failed")
            allure.attach(self.driver.get_screenshot_as_png() , name="Fail-SS", attachment_type=AttachmentType.PNG)
            self.lp.click_logout()
            self.log.info("Clicking on logout button")
            assert False
