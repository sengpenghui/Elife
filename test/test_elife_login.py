"""test_elife_login.py"""
import time

import pytest

from page.elife_login import *


# _*_coding:utf-8_*_
# Author: pseng



def test_login_001():
    # driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    #
    # driver.get("http://127.0.0.1:8234/login.html")
    #
    # driver.find_element(By.ID, "username").send_keys("byhy")
    # driver.find_element(By.CSS_SELECTOR, "#password").send_keys("sdfsdf")
    # driver.find_element(By.ID, "loginBtn").click()
    elif_login.elife_login( 'byhy', 'sdfsdf')

    assert elif_login.base_find_element(page.navbar).is_displayed()





@pytest.mark.parametrize('username, password, expectResult', [
    ('', 'sdfsdf', '请输入用户名'),('byhy', '', '请输入密码'),('byhy', 'sdfe', '登录失败： 用户名或者密码错误'),
    ('byhy', 'sdfsdfd', '登录失败： 用户名或者密码错误'),('byhy', 'sdfsd', '登录失败： 用户名或者密码错误'),
    ('byhyb', 'sdfsdf', '登录失败： 用户名不存在'), ('byh', 'sdfsdf', '登录失败： 用户名不存在')

])

def test_login_004(username, password, expectResult, clear_alert,):
    elif_login.elife_login(username, password)

    time.sleep(1)
    assert elif_login.base_alert_get_text() == expectResult

# def test_login_002(clear_alert):
#     # driver = webdriver.Chrome()
#     # driver.implicitly_wait(10)
#     #
#     # driver.get('http://127.0.0.1:8234/login.html')
#     #
#     # driver.find_element(By.ID, 'username').send_keys('')
#     # driver.find_element(By.CSS_SELECTOR, '#password').send_keys('sdfsdf')
#     # driver.find_element(By.ID, 'loginBtn').click()
#     elif_login.elife_login('', 'sdfsdf')
#
#     assert elif_login.driver.switch_to.alert.text == '请输入用户名'
#
#     # elif_login.driver.switch_to.alert.accept()
#
# def test_login_003(clear_alert):
#     # driver = webdriver.Chrome()
#     # driver.implicitly_wait(10)
#     #
#     # driver.get('http://127.0.0.1:8234/login.html')
#     #
#     # driver.find_element(By.ID, 'username').send_keys('byhy')
#     # driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
#     # driver.find_element(By.ID, 'loginBtn').click()
#     elif_login.elife_login('byhy', '')
#
#     assert elif_login.driver.switch_to.alert.text == '请输入密码'
#
#     # elif_login.driver.switch_to.alert.accept()
#
# def test_login_004(clear_alert):
#     # driver = webdriver.Chrome()
#     # driver.implicitly_wait(10)
#     #
#     # driver.get('http://127.0.0.1:8234/login.html')
#     #
#     # driver.find_element(By.ID, 'username').send_keys('byhy')
#     # driver.find_element(By.CSS_SELECTOR, '#password').send_keys('')
#     # driver.find_element(By.ID, 'loginBtn').click()
#     elif_login.elife_login('byhy', 'sdfe')
#
#     assert elif_login.driver.switch_to.alert.text == '登录失败： 用户名或密码错误