from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddCustomer:
    drop_customers_menu_xpath = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    click_customers_xpath = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    click_addnew_button_xpath = (By.XPATH, "//a[@class='btn btn-primary']")
    enter_email_xpath = (By.XPATH, "//input[@id='Email']")
    enter_password_xpath = (By.XPATH, "//input[@id='Password']")
    enter_firstname_xpath = (By.XPATH, "//input[@id='FirstName']")
    enter_lastname_xpath = (By.XPATH, "//input[@id='LastName']")
    radio_male_box_xpath = (By.XPATH, "//input[@id='Gender_Male']")
    enter_dob_xpath = (By.XPATH, "//input[@id='DateOfBirth']")
    enter_company_name_xpath = (By.XPATH, "//input[@id='Company']")
    check_tax_box_xpath = (By.XPATH, "//input[@id='IsTaxExempt']")
    drop_newsletter_xpath = (By.XPATH, '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div/div')
    drop_roles_xpath = (By.XPATH, '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div')
    drop_vendor_xpath = (By.XPATH, "//select[@id='VendorId']")
    check_active_xpath = (By.XPATH, "//input[@id='Active']")
    enter_comment_xpath = (By.XPATH, "//textarea[@id='AdminComment']")
    click_save_btn_xpath = (By.XPATH, "//button[@name='save']")
    status_save_xpath = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_customers_dropdown(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.drop_customers_menu_xpath))
        ele.click()

    def click_customers(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.click_customers_xpath))
        ele.click()

    def click_addnew_btn(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.click_addnew_button_xpath))
        ele.click()

    def enter_email(self, email):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_email_xpath))
        ele.send_keys(email)

    def enter_password(self, pwd):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_password_xpath))
        ele.send_keys(pwd)

    def enter_firstname(self, firstname):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_firstname_xpath))
        ele.send_keys(firstname)

    def enter_lastname(self, lastname):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_lastname_xpath))
        ele.send_keys(lastname)

    def click_radio_male(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.radio_male_box_xpath))
        ele.click()

    def enter_dob(self, dob):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_dob_xpath))
        ele.send_keys(dob)

    def enter_company(self, company):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_company_name_xpath))
        ele.send_keys(company)

    def check_tax(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.check_tax_box_xpath))
        ele.click()

    def drop_newsletter(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.drop_newsletter_xpath))
        ele.click()
        element = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Test store 2']")))
        element.click()

    def drop_roles(self):
        element1 = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]')))
        element1.click()
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.drop_roles_xpath))
        ele.click()
        element = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Guests']")))
        element.click()

    def drop_vendor(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.drop_vendor_xpath))
        Select(ele).select_by_index(2)

    def check_active(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.check_active_xpath))
        ele.click()

    def enter_comment(self, comment):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.enter_comment_xpath))
        ele.send_keys(comment)

    def click_save(self):
        ele = self.wait.until(ec.element_to_be_clickable(AddCustomer.click_save_btn_xpath))
        ele.click()

    def save_status(self):
        try:
            ele = self.wait.until(ec.presence_of_element_located(AddCustomer.status_save_xpath))
            if ele.is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return False
