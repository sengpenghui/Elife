"""elife_login.py"""
from selenium.webdriver.common.by import By

import page
from base.base import Base
from base.get_driver import GetDriver, driver


# _*_coding:utf-8_*_
# Author: pseng


class ElifeLogin(Base):

    def elife_login(self, username, password):
        # self.driver.find_element(By.ID, "username").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        # self.driver.find_element(By.ID, "loginBtn").click()

        driver.get(page.elife_URL)
        self.base_input(page.username, username)
        self.base_input(page.password, password)
        self.base_click(page.loginBtn)


elif_login = ElifeLogin()