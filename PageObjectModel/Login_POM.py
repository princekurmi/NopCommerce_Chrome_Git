from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    xpath_email = (By.XPATH, '//*[@id="Email"]')
    xpath_password = (By.XPATH, '//*[@id="Password"]')
    xpath_login_button = (By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button')
    xpath_logout_button = (By.XPATH, '//*[@id="navbarText"]/ul/li[3]/a')
    # xpath_login_status = (By.XPATH, '//*[@id="navbarText"]/ul/li[2]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_email(self, email):
        element = self.wait.until(EC.presence_of_element_located(LoginPage.xpath_email))
        element.clear()
        element.send_keys(email)

    def enter_password(self, pwd):
        element = self.wait.until(EC.presence_of_element_located(LoginPage.xpath_password))
        element.clear()
        element.send_keys(pwd)

    def click_login_button(self):
        element = self.wait.until(EC.element_to_be_clickable(LoginPage.xpath_login_button))
        element.click()

    def click_logout(self):
        element = self.wait.until(EC.element_to_be_clickable(LoginPage.xpath_logout_button))
        element.click()

    # def login_status(self):
    #     try:
    #         element = self.wait.until(
    #             EC.presence_of_element_located(LoginPage.xpath_login_status))
    #         if element.text == "John Smith":
    #             return True
    #         else:
    #             print(element.text)
    #             return False
    #     except NoSuchElementException:
    #         return False
