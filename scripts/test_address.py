# -*- coding: utf-8 -*-
from base import init_driver
from page import Page
import time

class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        # 主页，点击我的按钮
        self.page.home.click_mine_icon()
        # 我的页面，判断是否登录
        # 如果未登录
        if not self.page.mine.if_login():
            # 执行登录
            self.page.mine.click_login_button()
            self.page.login.login()
            time.sleep(1)
        # 我的页面，点击设置按钮
        self.page.mine.click_settings_button()
        time.sleep(1)
        # 设置页面，点击地址管理按钮
        if self.page.settings.if_scroll_until_feature_found(self.page.settings.feature_list, "关于百年奥莱", "up"):
            self.page.settings.click_about_bainian_button()
            assert True
        else:
            assert False
