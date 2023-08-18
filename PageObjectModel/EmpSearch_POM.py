from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class EmployeeSearch:

    enter_firstname_xpath = (By.XPATH, "//input[@id='SearchFirstName']")
    search_button_xpath = (By.XPATH, "//button[@id='search-customers']")
    search_result_CSS = (By.CSS_SELECTOR, "td:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_fname(self, fname):
        ele = self.wait.until(ec.visibility_of_element_located(EmployeeSearch.enter_firstname_xpath))
        ele.send_keys(fname)

    def click_search_button(self):
        ele = self.wait.until(ec.element_to_be_clickable(EmployeeSearch.search_button_xpath))
        ele.click()

    def search_result_status(self):
        try:
            ele = self.wait.until(ec.presence_of_element_located(EmployeeSearch.search_result_CSS)).is_displayed()
            if ele:
                return True
            else:
                return False
        except NoSuchElementException:
            return False
