# -*- coding: utf-8 -*-
from base import init_driver
from page import Page
import time


class TestChangePassword:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_change_password(self):
        # 主页，点击我的按钮
        self.page.home.click_mine_icon()
        # 判断是否登录成功，如果未登录就登录
        if not self.page.mine.if_login():
            self.page.mine.click_login_button()
            self.page.login.login("13554958766", "ff123000")
        # 我的页面点击设置按钮
        time.sleep(1)
        self.page.mine.click_settings_button()
        # 设置界点击"修改密码"按钮
        time.sleep(1)
        self.page.settings.click_change_password_button()
        # 修改密码界面，输入旧密码
        time.sleep(1)
        self.page.change_password.input_old_password("ff123000")
        # 修改密码界面，输入新密码
        time.sleep(1)
        self.page.change_password.input_new_password("123000")
        # 修改密码界面，输入确认密码
        time.sleep(1)
        self.page.change_password.input_confirm_password("123000")
        # 修改密码界面，点击保存按钮
        self.page.change_password.click_save_button()
        time.sleep(1)
        # 提示密码修改成功
        if not self.page.settings.if_toast_exist("密码修改成功"):
            assert False
        # 设置界面滑动到底部，查找"退出"按钮，并点击
        time.sleep(1)
        if not self.page.settings.if_feature_exist_scroll_page(self.page.settings.logout_button_feature, "up"):
            raise Exception("找不到退出按钮")
        # 退出弹框点确认
        self.page.settings.click_logout_button_feature()
        time.sleep(1)
        self.page.settings.click_logout_confirm_button()
        # 主页，点击我的按钮
        time.sleep(1)
        self.page.home.click_mine_icon()
        self.page.mine.click_login_button()
        # 输入用户名和新密码进行登录
        self.page.login.login("13554958766", "ff123000")
