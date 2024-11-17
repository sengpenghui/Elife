"""get_driver.py"""
from selenium import webdriver

# _*_coding:utf-8_*_
# Author: pseng
class GetDriver:

    # @classmethod
    # def get_driver(cls, webURL):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(webURL)
    #     cls.driver.implicitly_wait(10)
    #
    #     return cls.driver
    #
    # @classmethod
    # def quit_driver(cls):
    #     cls.driver.quit()

    def __init__(self):
        self.dri = webdriver.Chrome()
        self.dri.implicitly_wait(10)


driver = GetDriver().dri