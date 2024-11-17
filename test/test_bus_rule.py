"""test_bus_rule.py"""
import time

import pytest

import page
from page.bus_rule import bus_rule
from page.device_model import device_model
from page.elife_login import elif_login


# _*_coding:utf-8_*_
# Author: pseng


@pytest.fixture
def login_switch_to_device_model():
    elif_login.elife_login('byhy', 'sdfsdf')
    bus_rule.switch_to_bus_rule_link()

@pytest.fixture
def delete_bus_rule_item():

    yield
    if device_model.base_element_is_display(page.device_model_result_item_list):
        device_model.elife_device_model_delete_first_item()

# (self, ruleName:str, ruleType:str, minCharge=None, estCharge=None, feeRate=None, desc=None):

def test_bus_rule_001(login_switch_to_device_model):
    # elif_login.elife_login('byhy', 'sdfsdf')
    # bus_rule.switch_to_bus_rule_link()

    #new_rule = ['全国-电瓶车充电费率1', '预付费-下发业务量', '全国-电瓶车充电费率1', '0.1', '2', '千瓦时', '1']
    # bus_rule.bus_rule_add_new(new_rule[0],new_rule[1],new_rule[2],new_rule[3],new_rule[4],new_rule[5], new_rule[6])
    # ruleName = '全国-电瓶车充电费率1'
    # ruleType = '预付费-下发业务量'
    # minCharge = '0.1'
    # estCharge = '2'
    # feeRate = [['千瓦时', '1']]
    # desc = '全国-电瓶车充电费率1'
    # bus_rule.bus_rule_add_new_rule(ruleName, ruleType, minCharge, estCharge, feeRate[0], feeRate[1], desc)
    new_rule = ['全国-电瓶车充电费率1', '预付费-下发业务量', '0.1', '2', ['千瓦时', '1'],'全国-电瓶车充电费率1']
    bus_rule.bus_rule_add_new_rule(new_rule[0], new_rule[1], new_rule[2], new_rule[3], new_rule[4], new_rule[5])
    time.sleep(1)

    result_info = bus_rule.bus_rule_get_result_info()
    fee_rate = bus_rule.bus_rule_get_result_fee_rate_info()
    actual_result = [result_info[0].text,result_info[1].text,result_info[3].text,result_info[4].text,fee_rate, result_info[5].text]

    assert  actual_result == new_rule

# (self, ruleName:str, ruleType:str, minCharge=None, estCharge=None, feeRate=None, desc=None):
def test_bus_rule_101(login_switch_to_device_model):
    new_rule = ['南京-洗车机费率1', '预付费-下发费用', '2', '10', '南京-洗车机费率1']

    bus_rule.bus_rule_add_new_rule(new_rule[0],new_rule[1],minCharge=new_rule[2],estCharge=new_rule[3],desc=new_rule[4])
    time.sleep(1)

    result_info = bus_rule.bus_rule_get_result_info()
    # cost = bus_rule.base_find_elements('.sub-field-name ~ .field-value')
    actual_result = [result_info[0].text,result_info[1].text,result_info[3].text,result_info[4].text,result_info[5].text]

    assert  actual_result == new_rule

# (self, ruleName:str, ruleType:str, minCharge=None, estCharge=None, feeRate=None, desc=None):
def test_bus_rule_201(login_switch_to_device_model):
    # new_rule = ['南京-存储柜费率1', '后付费-上报业务量', '南京-存储柜费率1', '小时', '2', '100L']
    # bus_rule.bus_rule_add_new(new_rule[0],new_rule[1],new_rule[2],'','',new_rule[3],new_rule[4], new_rule[5])

    new_rule = ['南京-存储柜费率1', '后付费-上报业务量',
                [['100L', '小时', '2'], ['50L', '小时', '1'], ['10L', '小时', '0.5']],
                '南京-存储柜费率1']
    bus_rule.bus_rule_add_new_rule(new_rule[0], new_rule[1], feeRate=new_rule[2], desc=new_rule[3])
    time.sleep(1)

    result_info = bus_rule.bus_rule_get_result_info()
    fee_rate = bus_rule.bus_rule_get_result_fee_rate_info()
    actual_result = [result_info[0].text,result_info[1].text,fee_rate,result_info[3].text]

    assert  actual_result == new_rule


