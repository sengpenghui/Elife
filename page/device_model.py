"""device_model.py"""
import time

import page
from base.base import Base
from base.get_driver import driver
from page.elife_login import elif_login


# _*_coding:utf-8_*_
# Author: pseng

class DeviceModel(Base):

    def elife_device_model_add_click(self):
        self.base_find_element(page.device_model_add_btn).click()

    def elife_device_model_select(self):
        return self.base_select(page.device_type)

    def elife_device_model_version_input(self, version):
        self.base_input(page.device_version, version)

    def elife_device_model_desc_input(self, desc):
        self.base_input(page.device_desc, desc)

    def elife_device_model_ok_click(self):
        self.base_find_element(page.device_model_ok_btn).click()

    def elife_device_model_get_items(self):
        return self.base_find_elements(page.device_model_result_item_list)

    def elife_device_model_modify_select(self, model):
        self.base_select(page.device_model_result_item_modify_type).select_by_visible_text(model)

    def elife_device_model_modify_version_input(self, version):
        self.base_input(page.device_model_result_item_modify_version, version)

    def elife_device_model_modify_desc_input(self, desc):
        self.base_input(page.device_model_result_item_modify_desc, desc)

    def elife_device_model_modify_first_item(self, model, version, desc):
        self.base_click(page.device_model_result_item_modify_btn)
        # self.elife_device_model_select("电瓶车充电站")
        # self.elife_device_model_version_input("yixun-charger-g30-220v7kw")
        # self.elife_device_model_desc_input("上海易迅能源2024款7千瓦汽车充电站")
        self.elife_device_model_modify_select(model)
        self.elife_device_model_modify_version_input(version)
        self.elife_device_model_modify_desc_input(desc)
        time.sleep(1)
        self.base_click(page.device_model_result_item_modify_ok_btn)
        # self.base_find_element(page.device_model_result_item_modify_ok_btn).click()

    def elife_get_no_result_text(self):
        return self.base_get_text(page.device_model_no_results)


    def elife_get_first_item_filed_value(self):
        return self.base_get_elements_text(page.device_model_items_values)

    # def elife_device_model_delete_first_item(self):
    #
    #     driver.implicitly_wait(0)
    #     delBtn = self.base_find_elements(page.device_model_result_item_delete_btn)
    #
    #     driver.implicitly_wait(10)
    #     # if len(delBtn) > 0:
    #     #     for index in range(len(delBtn)):
    #     #         delBtn[0].click()
    #     #         self.base_assert_accept_click()
    #     # return True
    #     if len(delBtn) > 0:
    #         delBtn[0].click()
    #         self.base_alert_accept_click()

    def elife_add_new_device_model(self, model, version, desc):

        self.base_click(page.device_model_link)
        if self.base_find_element(page.device_model_add_btn).text == "添加":
            self.elife_device_model_add_click()

        self.elife_device_model_select().select_by_visible_text(model)
        self.elife_device_model_version_input(version)
        self.elife_device_model_desc_input(desc)

        self.elife_device_model_ok_click()



device_model = DeviceModel()

# if __name__ == '__main__':
#     elif_login.elife_login('byhy', 'sdfsdf')
#     elif_login.base_click(page.device_model_page)
#     device_model.elife_device_model_delete_first_item()

