"""device.py"""
import time

from selenium.webdriver.support.expected_conditions import alert_is_present

import page
from base.base import Base
from base.get_driver import driver
from page.elife_login import elif_login


# _*_coding:utf-8_*_
# Author: pseng

class Device(Base):
    def select_dev_type(self):
        return self.base_select(page.device_type)

    def select_dev_model(self):
        try:
            sel = self.base_select(page.dev_model_list)
            opt = sel.options[0]
            if opt:
                return sel
        except:
            print("设备型号列表为空，请先添加设备型号！")

    def select_dev_rules(self):
        try:
            sel = self.base_select(page.dev_rule_list)
            opt = sel.options[0]
            if opt:
                return sel
        except:
            print("业务规则列表为空，请先添加业务规则！")

    def input_dev_num(self, devNum):
        self.base_input(page.dev_num,devNum)

    def input_dev_desc(self, devDesc):
        self.base_input(page.dev_desc,devDesc)

    # def dev_get_result_info(self):
    #     return self.base_find_elements(page.dev_first_result_info)

    # def dev_delete_result_item(self):
    #     delBtn = self.base_find_elements(page.dev_result_item_delete_btn)
    #     if len(delBtn) > 0:
    #         delBtn[0].click()
    #         self.base_alert_accept_click()


    def add_new_dev(self, devType, mod_num, rul_num, devNum=None, devDesc=None):

        dev.base_click(page.dev_link)

        if self.base_find_element(page.device_model_add_btn).text == "添加":
            self.base_click(page.dev_add_btn)

        self.select_dev_type().select_by_visible_text(devType)
        self.select_dev_model().select_by_index(int(mod_num))
        self.select_dev_rules().select_by_index(int(rul_num))
        time.sleep(1)
        self.input_dev_num(devNum)
        self.input_dev_desc(devDesc)
        # self.base_click(page.dev_ok_btn)
        # driver.save_screenshot('123.png')
        self.base_find_element(page.dev_ok_btn).click()
        # driver.get_screenshot_as_file('123')



dev = Device()

# if __name__ == '__main__':
#     elif_login.elife_login('byhy', 'sdfsdf')
#     elif_login.base_click(page.dev_link)
#     dev.add_new_dev('电瓶车充电站',0,0,'电瓶车充电站001', '电瓶车充电站001号')
