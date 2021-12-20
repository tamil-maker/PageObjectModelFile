from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):

    HEADER = By.CSS_SELECTOR, "fas fa-user font-18pt text-green"
    CARD_TITLE = By.CSS_SELECTOR,"h4.card-title font-14pt mb-0"
    def __init__(self,driver):
        super().__init__(driver)

    def get_home_page_title(self,title):
        return self.get_title(title) 
    
    def is_settings_icons_exit(self):
        return self.is_visible(self.SETTINGS_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)