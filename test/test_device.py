"""test_device.py"""
import pytest

import page
from base.get_driver import driver
from page.device import dev
from page.elife_login import elif_login


# _*_coding:utf-8_*_
# Author: pseng

# @pytest.fixture
# def login_switch_to_dev():
#     elif_login.elife_login('byhy', 'sdfsdf')
#     dev.base_click(page.dev_link)

@pytest.fixture
def delete_dev_item():
    yield
    # if dev.base_element_is_display(page.dev_result_item_list):
    #     dev.dev_delete_result_item()
    if dev.base_element_is_display(page.com_result_item_list):
        dev.base_delete_result_item()



def test_add_charging_stat_001(login_elife, delete_dev_item):

    dev.add_new_dev('电瓶车充电站',0,0,'电瓶车充电站001', '电瓶车充电站001号')

    first_result = dev.base_get_result_info()
    assert first_result[0].text == '电瓶车充电站'
    assert first_result[2].text == '电瓶车充电站001'
    assert first_result[5].text == '电瓶车充电站001号'

def test_add_wash_stat_101(login_elife, delete_dev_item):

    dev.add_new_dev('洗车站',0,0,'洗车站001', '洗车站001号')

    first_result = dev.base_get_result_info()
    assert first_result[0].text == '洗车站'
    assert first_result[2].text == '洗车站001'
    assert first_result[5].text == '洗车站001号'

def test_add_locker_201(login_elife, delete_dev_item):

    dev.add_new_dev('存储柜',0,0,'存储柜001', '存储柜001号')

    first_result = dev.base_get_result_info()
    assert first_result[0].text == '存储柜'
    assert first_result[2].text == '存储柜001'
    assert first_result[5].text == '存储柜001号'