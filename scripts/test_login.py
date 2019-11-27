"""
登录测试用例
"""
import pytest

from common.utils import init_driver
from page.page_factory import PageFactory
from tools.read_yaml import build_login_data


class TestLogin(object):

    def setup(self):
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 工厂类实例对象

    def teardown(self):
        self.driver.quit()  # 退出驱动对象

    @pytest.mark.parametrize('name, pwd', build_login_data())
    def test_login(self, name, pwd):
        """登录测试方法"""
        self.page_factory.home_page.click_mine()  # 点击我的
        self.page_factory.mine_page.click_login()  # 点击登录
        self.page_factory.login_page.input_name(name)  # 输入用户名
        self.page_factory.login_page.input_pwd(pwd)  # 输入密码
        self.page_factory.login_page.click_login_btn()  # 点击登录按钮
        self.page_factory.login_page.click_com_btn()  # 点击确认按钮
