"""test_device_model.py"""
import time

import pytest

import page
from page.device_model import device_model


# _*_coding:utf-8_*_
# Author: pseng


@pytest.fixture
def delete_device_model_item():

    yield
    if device_model.base_element_is_display(page.com_result_item_list):
        device_model.base_delete_result_item()


def test_device_model_add_001(login_elife,delete_device_model_item):

    dev_info = ['存储柜','elife-canbinlocker-g22-10-20-40','南京e生活存储柜-10大20中40小']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)

    ele = device_model.base_get_result_info()
    for index in range(len(dev_info)):
        assert dev_info[index] == ele[index].text


def test_device_model_add_002(login_elife, delete_device_model_item):

    # elif_login.elife_login('byhy', 'sdfsdf')
    # elif_login.base_click(page.device_model_page)

    dev_info = ['存储柜','柜'*100,'南京e生活存储柜-10大20中40小']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)

    ele = device_model.base_get_result_info()
    for index in range(len(dev_info)):
        assert dev_info[index] == ele[index].text

def test_device_model_add_101(login_elife, delete_device_model_item):

    # elif_login.elife_login('byhy', 'sdfsdf')
    # elif_login.base_click(page.device_model_page)

    dev_info = ['电瓶车充电站','bokpower-charger-g22-220v450w','杭州bok 2022款450瓦 电瓶车充电站']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)

    # ele = device_model.elife_get_first_item_filed_value()
    ele = device_model.base_get_result_info()
    print(ele)
    for index in range(len(dev_info)):
        assert dev_info[index] == ele[index].text

def test_device_model_add_201(login_elife, delete_device_model_item):

    # elif_login.elife_login('byhy', 'sdfsdf')
    # elif_login.base_click(page.device_model_page)

    dev_info = ['洗车站','njcw-carwasher-g22-2s','南京e生活2022款洗车机 2个洗车位']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)

    ele = device_model.base_get_result_info()
    print(ele)
    for index in range(len(dev_info)):
        assert dev_info[index] == ele[index].text

def test_device_model_add_301(login_elife, delete_device_model_item):

    # elif_login.elife_login('byhy', 'sdfsdf')
    # elif_login.base_click(page.device_model_page)

    dev_info = ['汽车充电站','yixun-charger-g22-220v7kw','南京易迅能源2022款7千瓦汽车充电站']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)

    ele = device_model.base_get_result_info()
    print(ele)
    for index in range(len(dev_info)):
        assert dev_info[index] == ele[index].text

def test_device_model_modify_501(login_elife, delete_device_model_item):

    dev_info = ['汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)
    modify_info = ["电瓶车充电站", "yixun-charger-g30-220v7kw","上海易迅能源2024款7千瓦汽车充电站"]
    device_model.elife_device_model_modify_first_item(modify_info[0], modify_info[1], modify_info[2])

    ele = device_model.base_get_result_info()
    print(ele)
    for index in range(len(dev_info)):
        assert modify_info[index] == ele[index].text


def test_device_model_delete_601(login_elife):

    dev_info = ['汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站']
    device_model.elife_add_new_device_model(dev_info[0], dev_info[1], dev_info[2])

    time.sleep(1)
    device_model.base_delete_result_item()

    time.sleep(1)
    no_result = device_model.elife_get_no_result_text()
    assert no_result == "系统中还没有相应数据"









