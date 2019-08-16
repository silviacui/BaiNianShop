# -*- coding: utf-8 -*-
from base import init_driver
from page import Page
import time

class TestAppVersion:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_app_version(self):
        # 主页，点击我的按钮
        self.page.home.click_mine_icon()
        time.sleep(1)
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
        # 判断页面是否可以找到元素“关于百年里奥”，如果没有则滑动页面
        if self.page.settings.if_scroll_until_feature_found(self.page.settings.feature_list, "关于百年奥莱", "up"):
            # 如果找到，点击该按钮
            self.page.settings.click_about_bainian_button()
            app_version_text = self.page.about_bainian.get_app_version_text()
            print("当前app版本为" + app_version_text)
            assert True
        else:
            assert False



