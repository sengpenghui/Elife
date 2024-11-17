"""__init__.py.py"""
from selenium.webdriver.common.by import By

# _*_coding:utf-8_*_
# Author: pseng

"""URL"""
elife_URL = 'http://127.0.0.1:8234/login.html'


"""公共页面元素"""
com_first_result_info = By.CSS_SELECTOR, '.result-list-item .field-value'
com_result_item_list = By.CSS_SELECTOR, '.result-list-item'
com_result_item_delete_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(1)"


"""登陆页面信息"""
username = By.ID, "username"
password = By.CSS_SELECTOR, "#password"
loginBtn = By.ID, "loginBtn"

navbar = By.CSS_SELECTOR, ".nav-logo"

"""设备型号页面信息"""
device_model_link = By.CSS_SELECTOR, ".sub-nav-bar a[href='#/devicemodel']"
device_model_add_btn = By.CSS_SELECTOR, ".add-one-area>span.btn"
device_type = By.ID, "device-type"
device_version = By.CSS_SELECTOR, "#device-model"
device_desc = By.ID, "device-model-desc"
device_model_cancel_btn = By.CSS_SELECTOR, ".add-one-area>span.btn"
device_model_ok_btn = By.CSS_SELECTOR, ".add-one-submit-btn-div .btn"
device_model_result_item_list = By.CSS_SELECTOR, ".result-list-item"
device_model_result_item_delete_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(1)"
device_model_result_item_modify_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(2)"
device_model_result_item_modify_type = By.CSS_SELECTOR, ".result-list-item .edit-one-form #device-type"
device_model_result_item_modify_version = By.CSS_SELECTOR, ".result-list-item .field:nth-child(2) .input-xl"
device_model_result_item_modify_desc = By.CSS_SELECTOR, ".result-list-item .field:nth-child(3) .input-xl"
device_model_result_item_modify_ok_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(1)"
device_model_items_values = By.CSS_SELECTOR, ".result-list-item:nth-child(1) .result-list-item-info span.field-value"
device_model_no_results = By.CSS_SELECTOR, ".result-list>p"

"""业务规则页面信息"""
bus_rule_link = By.CSS_SELECTOR, '.sub-nav-bar a[href="#/svcrule"]'
bus_rule_add_btn = By.CSS_SELECTOR, '.add-one-area>span.btn'
bus_rule_input_items = By.CSS_SELECTOR, '.add-one-form .field-name ~ input'
bus_rule_input_name = By.CSS_SELECTOR, '.add-one-form .field:nth-child(1)>input'
bus_rule_input_min_charge = By.CSS_SELECTOR, '.add-one-form .field:nth-child(3)>input'
bus_rule_input_est_charge = By.CSS_SELECTOR, '.add-one-form .field:nth-child(4)>input'
bus_rule_input_desc = By.XPATH, '//div[@class="add-one-submit-btn-div"]/preceding-sibling::*[1]/input'
bus_rule_input_select = By.ID, 'rule_type_id'
bus_rule_fee_rate_items = By.CSS_SELECTOR, '.fee-rate-list .fee-rate'
# bus_rule_fee_rate_inputs = By.CSS_SELECTOR, '.fee-rate input'
bus_rule_fee_rate_entry = By.CSS_SELECTOR, 'div.fee-rate:nth-last-child(2)'
bus_rule_fee_rate_inputs = By.CSS_SELECTOR, '.fee-rate>input'
bus_rule_fee_rate_add_btn = By.CSS_SELECTOR, '.fee-rate-list button'
bus_rule_fee_rate_del_btn = By.CSS_SELECTOR, '.fee-rate span:last-child'
bus_rule_ok_btn = By.CSS_SELECTOR, '.add-one-submit-btn-div .btn'
bus_rule_result_item_list = By.CSS_SELECTOR, ".result-list-item"
bus_rule_result_item_delete_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(1)"
bus_rule_first_result_info = By.CSS_SELECTOR, '.result-list-item .field-value'
bus_rule_first_result_fee_rate_info = By.CSS_SELECTOR, '.result-list-item:first-child .field-value span.sub-field-value'

"""设备页面信息"""
dev_link = By.CSS_SELECTOR, '.sub-nav-bar a[href="#/device'
dev_add_btn = By.CSS_SELECTOR, '.add-one-area>span.btn'
dev_select_list = By.ID, 'device-type'
dev_model_list = By.ID, 'device-model'
dev_rule_list = By.ID, 'svc-rule-id'
dev_num = By.ID, 'device-sn'
dev_desc = By.ID, 'device-desc'
dev_ok_btn = By.CSS_SELECTOR, '.add-one-submit-btn-div .btn'
dev_first_result_info = By.CSS_SELECTOR, '.result-list-item .field-value'
dev_result_item_list = By.CSS_SELECTOR, '.result-list-item'
dev_result_item_delete_btn = By.CSS_SELECTOR, ".result-list-item:first-child .result-list-item-btn-bar>span:nth-child(1)"

