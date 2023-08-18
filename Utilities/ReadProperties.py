import configparser

config = configparser.RawConfigParser()
config.read("D:\\Software Testing\\TK NopCommerce\\Configuration\\Config.ini")

addcust = configparser.RawConfigParser()
addcust.read("D:\\Software Testing\\TK NopCommerce\\Configuration\\AddCust.ini")

empsearch = configparser.RawConfigParser()
empsearch.read("D:\\Software Testing\\TK NopCommerce\\Configuration\\EmpSearch.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("Common Info", "Url")
        return url

    @staticmethod
    def get_email():
        email = config.get("Common Info", "Email")
        return email

    @staticmethod
    def get_password():
        password = config.get("Common Info", "Password")
        return password

    @staticmethod
    def get_mail():
        mail = addcust.get("AddCust Info", "mail")
        return mail

    @staticmethod
    def get_pwd():
        pwd = addcust.get("AddCust Info", "pwd")
        return pwd

    @staticmethod
    def get_firstname():
        firstname = addcust.get("AddCust Info", "firstname")
        return firstname

    @staticmethod
    def get_lastname():
        lastname = addcust.get("AddCust Info", "lastname")
        return lastname

    @staticmethod
    def get_dob():
        dob = addcust.get("AddCust Info", "dob")
        return dob

    @staticmethod
    def get_company():
        company = addcust.get("AddCust Info", "company")
        return company

    @staticmethod
    def get_comment():
        comment = addcust.get("AddCust Info", "comment")
        return comment

    @staticmethod
    def get_fname():
        fname = empsearch.get("EmpSearch Info", "Fname")
        return fname
