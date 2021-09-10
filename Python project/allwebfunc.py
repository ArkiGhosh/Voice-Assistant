from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#WEBDRIVER code()
#----------------------------------------------------------------------------
class Webfunc:
    
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_site(self, url):
        self.driver.get(url)
    
    def imp_wait(self, t):
        self.driver.implicitly_wait(t)

    def button_click():
        pass

    def finding_element(self, iden):
        return self.driver.find_element_by_id(iden)

    def send_data(self, input_data, ide):
        self.driver.find_element_by_id(ide).send_keys(input_data)

    def search_click(self, ide):
        self.driver.find_element_by_id(ide).click()
    
#----------------------------------------------------------------------------

