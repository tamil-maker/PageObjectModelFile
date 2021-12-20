from selenium webdriver.common.by import By 
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    """By locators OR"""
    EMIL = (By.ID,"inp_loginid")
    PASSWORD =(By.ID,"inp_password")
    LOGIN_BUTTON = (By.ID,"btn btn-primary btn-block my-4")
    SIGNUP_LINK = (By.LINK_TEST,"btn-link")

    """constructor of the page class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """Page actions"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """this is used to check signup link"""
    def is_signup_link_exit(self):
        return self.isvisible(self.SIGNUP_LINK) 

    """this is used to logon to app"""
    def do_login(self,inp_loginid,inp_password):
        self.do_send_keys(self.EMAIL,inp_loginid) 
        self.do_send_keys(self.PASSWORD,inp_password)           
        self.do_click(self.LOGIN_BUTTON)
