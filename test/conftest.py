"""conftest.py.py"""

# _*_coding:utf-8_*_
# Author: pseng

import os

import pytest

from base.get_driver import driver
from page.elife_login import elif_login
from datetime import datetime



# os.system("pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple")
# os.system("pip install pytest")

@pytest.fixture(scope='module')
def login_elife():
    elif_login.elife_login('byhy','sdfsdf')


@pytest.fixture
def clear_alert():
    yield
    try:
        driver.switch_to.alert.accept()
    except Exception as e:
        print(e)



"""以下为定制化HTML测试报告"""
# 1. 修改测试报告标题
def pytest_html_report_title(report):
    """修改标题"""
    report.title = "elife自动化测试报告"

# 2. 修改报告表格
@pytest.mark.optionahook
def pytest_html_results_table_header(cells):
    """修改表头属性，增加Time列，删除link列"""
    cells.insert(2, "<th>Description</th>")
    cells.insert(1,'<th class="sortable time" data-column-type="time">Time</th>')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{report.description}</td>')
    cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)

# 3. 报错误截图
"""当执行出现错误，截图显示在report中"""
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = f'<div><img src="data:image/png;base64,{screen_img}" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    report.description = str(item.function.__doc__)

def _capture_screenshot():
    """截图保存为base64， 展示到html中"""
    return driver.get_screenshot_as_base64()