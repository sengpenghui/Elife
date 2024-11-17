"""base.py"""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import page
from base.get_driver import driver


# _*_coding:utf-8_*_
# Author: pseng


class Base:

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(10)


    def open(self, url):
        driver.get(url)

    def base_find_element(self, loc, timeout=30, poll=0.5 ):
        return WebDriverWait(driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_find_elements(self,loc, timeout=30, poll=0.5):
        return WebDriverWait(driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_elements(*loc))

    #通过元素查找元素
    def base_element_find_element(self,element, loc):
        element.find_element(loc)

    def base_element_find_elements(self,element, loc):
        element.find_elements(loc)

    def base_element_is_display(self,loc):
        return self.base_find_element(loc).is_displayed()

    def base_input(self, loc, value):
        ele = self.base_find_element(loc)
        ele.clear()
        ele.send_keys(value)

    def base_click(self,loc):
        self.base_find_element(loc).click()

    def base_select(self,loc):
        return Select(self.base_find_element(loc))
        # sel.select_by_visible_text(value)

    def base_get_text(self,loc):
        return self.base_find_element(loc).text

    def base_get_elements_text(self,loc):
        ele_list = self.base_find_elements(loc)
        text = []
        for i in range(len(ele_list)):
            text.append(ele_list[i].text)

        return text

    def base_alert_accept_click(self):
        driver.switch_to.alert.accept()

    def base_alert_get_text(self):
        return driver.switch_to.alert.text


    """获取第一个结果"""
    def base_get_result_info(self):
        return self.base_find_elements(page.com_first_result_info)

    """删除结果"""
    def base_delete_result_item(self):
        delBtn = self.base_find_elements(page.com_result_item_delete_btn)
        if len(delBtn) > 0:
            delBtn[0].click()
            self.base_alert_accept_click()


