from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.wd = webdriver.Firefox(options=options)
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser")
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_homepage(self):
        wd = self.wd
        if (len(wd.find_elements(By.XPATH, "//strong[normalize-space()='Select all']")) == 0 and
                len(wd.find_elements(By.XPATH, "//select[@name='to_group']")) == 0):
            wd.find_element(By.XPATH, "//a[normalize-space()='home']").click()

    def destroy(self):
        wd = self.wd
        wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
