# -*- coding: utf-8 -*-
from base import init_driver
from page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login001(self):
        # 点击主页的我图标
        self.page.home.click_mine_icon()
        # 点击我的页面的”已有账号，去登录“
        self.page.mine.click_login_button()
        # 登录页面输入账号和密码，并点击登录按钮
        self.page.login.input_username("13554958766")
        self.page.login.input_password("123000")
        self.page.login.click_login()