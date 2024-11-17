"""bus_rule.py"""
import time

from selenium.webdriver.common.by import By

import page
from base.base import Base
from base.get_driver import driver


# _*_coding:utf-8_*_
# Author: pseng

class BusRule(Base):

    def switch_to_bus_rule_link(self):
        self.base_click(page.bus_rule_link)

    def bus_rule_add_btn_click(self):
        self.base_click(page.bus_rule_add_btn)

    def bus_rule_add_input_list(self):
        return self.base_find_elements(page.bus_rule_input_items)

    def bus_rule_fee_rate_input_list(self):
        return self.base_find_elements(page.bus_rule_fee_rate_inputs)

    def bus_rule_name_input(self, name):
        print('获取name')
        rule_name = self.bus_rule_add_input_list()[0]
        rule_name.send_keys(name)

    def bus_rule_type_select(self,value):
        print('获取type')
        self.base_select(page.bus_rule_input_select, value)

    def bus_rule_min_charge_input(self, charge):
        print('获取min_charge')
        if len(self.bus_rule_add_input_list()) == 6 or len(self.bus_rule_add_input_list()) == 4:
            min_charge = self.bus_rule_add_input_list()[1]
            min_charge.send_keys(charge)

    def bus_rule_est_charge_input(self,charge):
        print('获取est_charge')
        if len(self.bus_rule_add_input_list()) == 6 or len(self.bus_rule_add_input_list()) == 4:
            est_charge = self.bus_rule_add_input_list()[2]
            est_charge.send_keys(charge)

    def bus_rule_fee_unit_input(self,unit):
        print('获取fee_unit')
        est_charge = self.bus_rule_fee_rate_input_list()[0]
        est_charge.send_keys(unit)

    def bus_rule_fee_price_input(self,price):
        print('获取fee_price')
        est_charge = self.bus_rule_fee_rate_input_list()[1]
        est_charge.send_keys(price)

    def bus_rule_desc_input(self,desc):
        print('获取desc')
        if len(self.bus_rule_add_input_list()) == 6 or len(self.bus_rule_add_input_list()) == 4:
            est_charge = self.bus_rule_add_input_list()[3]
            est_charge.send_keys(desc)
        # elif len(self.bus_rule_add_input_list()) == 4:
        #     est_charge = self.bus_rule_add_input_list()[3]
        #     est_charge.send_keys(desc)
        elif len(self.bus_rule_add_input_list()) == 2:
            est_charge = self.bus_rule_add_input_list()[1]
            est_charge.send_keys(desc)

    # 后续费 - 上报业务量
    def bus_rule_fee_rate_items(self):
        return self.base_find_elements(page.bus_rule_fee_rate_items)

    def bus_rule_fee_rate_inputs(self, bus_code, unit, price):

        # fee_rate_items = self.base_find_elements(page.bus_rule_fee_rate_items)
        # if len(fee_rate_items) == 1:
        #     self.base_element_find_elements(page.bus_rule_fee_rate_inputs)
        rate_inputs = self.base_find_elements(page.bus_rule_fee_rate_inputs)
        rate_inputs[0].send_keys(bus_code)
        rate_inputs[1].send_keys(unit)
        rate_inputs[2].send_keys(price)

    # def bus_rule_fee_rate_del_list(self):
    #     return self.base_find_elements(page.bus_rule_fee_rate_del_btn)

    def bus_rule_fee_rate_add(self):
        self.base_click(page.bus_rule_fee_rate_add_btn)

    def bus_rule_ok_btn_click(self):
        print('获取ok button')
        self.base_click(page.bus_rule_ok_btn)

    def bus_rule_get_result_info(self):
        # result_info_list = []
        # for text in self.base_get_elements_text(page.bus_rule_result_info):
        #     a = text.strip()
        #     result_info_list.append(a)
        # return result_info_list
        return self.base_find_elements(page.bus_rule_first_result_info)

    def bus_rule_get_result_fee_rate_info(self):
            fee_list = []
            tmp = []
            entry = self.base_get_elements_text(page.bus_rule_first_result_fee_rate_info)
            if len(entry)%2 == 0:
                for text in entry:
                    a = text.strip().split('：')
                    fee_list.append(a[1])
            elif len(entry)%3 == 0:
                for text in entry:
                    a = text.strip().split('：')
                    print(a[1])
                    tmp.append(a[1])
                print(tmp)
                for index in range(0, len(tmp), 3):
                    fee_list.append(tmp[index:index+3])
                    # for text in tmp:
                    #     a = text.strip().split('：')
                    #     # b = [a[1]]
                    #     fee_list.append(a[1])

            print(fee_list)
            return fee_list

    def bus_rule_delete_first_item(self):

        driver.implicitly_wait(0)
        delBtn = self.base_find_elements(page.bus_rule_result_item_delete_btn)

        driver.implicitly_wait(10)
        if len(delBtn) > 0:
            delBtn[0].click()
            self.base_alert_accept_click()


    def bus_rule_add_new_rule(self, ruleName:str, ruleType:str,
                              minCharge=None, estCharge=None,
                              feeRate=None, desc=None):
        """
        :param ruleName: 规则名称
        :param ruleType: 规则类型：只能是 '预付费-下发业务量'， ’预付费-下发费用‘， '后付费-上报业务量'：
        :param minCharge: 最小费用，没有是为None
        :param estCharge: 预估消费， 没有时为None
        :param desc: 规则描述
        :param feeRate: 费率，当ruleType为'预付费-下发业务量'  格式为：
        ['小时', '0.5'];
        '后付费-上报业务量':
        [
        ['10L', '小时', '0.5'],
        ['50L', '小时', '1']
        ]
        :return:
        """
        if self.base_get_text(page.bus_rule_add_btn) == "添加":
            self.bus_rule_add_btn_click()

        # 输入规则名称
        ele = self.base_find_element(page.bus_rule_input_name)
        ele.clear()
        ele.send_keys(ruleName)

        # 选择规则类型
        self.base_select(page.bus_rule_input_select).select_by_visible_text(ruleType)


        if ruleType != '后付费-上报业务量':
            min_input = self.base_find_element(page.bus_rule_input_min_charge)
            min_input.clear()
            if minCharge:
                min_input.send_keys(minCharge)

            est_input= self.base_find_element(page.bus_rule_input_est_charge)
            est_input.clear()
            if estCharge:
                est_input.send_keys(estCharge)
        # 因为desc的次序会有变化，所以用Xpath，从后面找同级的第一个。
        if desc:
            descEle = self.base_find_element(page.bus_rule_input_desc)
            descEle.clear()
            descEle.send_keys(desc)
        if ruleType == '预付费-下发业务量':
            eles = self.base_find_elements(page.bus_rule_fee_rate_inputs)
            eles[0].send_keys(feeRate[0])
            eles[1].send_keys(feeRate[1])
        elif ruleType == '后付费-上报业务量':
            # 删除遗留费率
            while True:
                # eles = self.base_find_elements(page.bus_rule_fee_rate_del_btn)
                eles = driver.find_elements(By.CSS_SELECTOR, '.fee-rate span:last-child')
                if eles:
                    eles[0].click()
                    time.sleep(0.5)
                else:
                    break

            driver.implicitly_wait(5)

            for fee in feeRate:
                self.base_find_element(page.bus_rule_fee_rate_add_btn).click()
                # self.base_click(page.bus_rule_fee_rate_add_btn)
                entry = self.base_find_element(page.bus_rule_fee_rate_entry)
                # entry = self.wd.find_element(By.CSS_SELECTOR, 'div.fee-rate:nth-last-child(2)')
                # fee_rate_inputs = self.base_element_find_elements(entry, page.bus_rule_fee_rate_inputs)
                # 业务码
                # fee_rate_inputs[0].send_keys(fee[0])
                # fee_rate_inputs[1].send_keys(fee[1])
                # fee_rate_inputs[2].send_keys(fee[2])
                # 业务码
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(1)').send_keys(fee[0])
                # 计费单位
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(2)').send_keys(fee[1])
                # 单位价格
                entry.find_element(By.CSS_SELECTOR, 'input:nth-of-type(3)').send_keys(fee[2])
                # eles = self.base_find_elements(page.bus_rule_fee_rate_inputs)
                # eles[0].send_keys(fee[0])
                # eles[1].send_keys(fee[1])
                # eles[2].send_keys(fee[2])

        print("2-提交")
        self.bus_rule_ok_btn_click()

bus_rule = BusRule()

