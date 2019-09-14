# -*- coding: utf-8 -*-
from base import init_driver
from page import Page
import time
from base import  data_analyze
import pytest


class TestPassword:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # 修改密码成功的场景
    # @pytest.mark.parametrize("args", data_analyze("test_password_success"))
    # def test_password_success(self, args):
    #
    #     username = args["username"]
    #     old_password = args["old_password"]
    #     new_password = args["new_password"]
    #     confirm_password = args["confirm_password"]
    #     toast_msg = args["toast_msg"]
    #
    #     # 主页，点击我的按钮
    #     self.page.home.click_mine_icon()
    #     # 判断是否登录成功，如果未登录就登录
    #     if not self.page.mine.if_login():
    #         self.page.mine.click_login_button()
    #         self.page.login.login(username, old_password)
    #     # 我的页面点击设置按钮
    #     time.sleep(1)
    #     self.page.mine.click_settings_button()
    #     # 设置界点击"修改密码"按钮
    #     time.sleep(1)
    #     self.page.settings.click_change_password_button()
    #     # 修改密码界面，输入旧密码
    #     time.sleep(1)
    #     self.page.change_password.input_old_password(old_password)
    #     # 修改密码界面，输入新密码
    #     time.sleep(1)
    #     self.page.change_password.input_new_password(new_password)
    #     # 修改密码界面，输入确认密码
    #     time.sleep(1)
    #     self.page.change_password.input_confirm_password(confirm_password)
    #     # 修改密码界面，点击保存按钮
    #     self.page.change_password.click_save_button()
    #     time.sleep(1)
    #     # 提示密码修改成功
    #     if not self.page.settings.if_toast_exist(toast_msg):
    #         assert False
    #     # 设置界面滑动到底部，查找"退出"按钮，并点击
    #     time.sleep(1)
    #     if not self.page.settings.if_feature_exist_scroll_page(self.page.settings.logout_button_feature, "up"):
    #         raise Exception("找不到退出按钮")
    #     # 退出弹框点确认
    #     self.page.settings.click_logout_button_feature()
    #     time.sleep(1)
    #     self.page.settings.click_logout_confirm_button()
    #     # 主页，点击我的按钮
    #     time.sleep(1)
    #     self.page.home.click_mine_icon()
    #     self.page.mine.click_login_button()
    #     # 输入用户名和新密码进行登录
    #     self.page.login.login(username, new_password)

    # 修改密码失败的场景一--错误的旧密码
    # @pytest.mark.parametrize("args", data_analyze("test_wrong_old_password"))
    # def test_wrong_old_password(self, args):
    #
    #     username = args["username"]
    #     old_password = args["old_password"]
    #     new_password = args["new_password"]
    #     confirm_password = args["confirm_password"]
    #     toast_msg = args["toast_msg"]
    #
    #     # 主页，点击我的按钮
    #     self.page.home.click_mine_icon()
    #     # 判断是否登录成功，如果未登录就登录
    #     if not self.page.mine.if_login():
    #         self.page.mine.click_login_button()
    #         self.page.login.login(username, "ff1230000")
    #     # 我的页面点击设置按钮
    #     time.sleep(1)
    #     self.page.mine.click_settings_button()
    #     # 设置界点击"修改密码"按钮
    #     time.sleep(1)
    #     self.page.settings.click_change_password_button()
    #     # 修改密码界面，输入旧密码
    #     time.sleep(1)
    #     self.page.change_password.input_old_password(old_password)
    #     # 修改密码界面，输入新密码
    #     time.sleep(1)
    #     self.page.change_password.input_new_password(new_password)
    #     # 修改密码界面，输入确认密码
    #     time.sleep(1)
    #     self.page.change_password.input_confirm_password(confirm_password)
    #     # 修改密码界面，点击保存按钮
    #     self.page.change_password.click_save_button()
    #     time.sleep(1)
    #     # 提示密码修改成功
    #     assert self.page.settings.if_toast_exist(toast_msg)

    # 修改密码失败的场景一--正确的旧密码
    @pytest.mark.parametrize("args", data_analyze("test_password_unsuccess"))
    def test_password_unsuccess(self, args):

        username = args["username"]
        old_password = args["old_password"]
        new_password = args["new_password"]
        confirm_password = args["confirm_password"]
        toast_msg = args["toast_msg"]

        # 主页，点击我的按钮
        time.sleep(1)
        self.page.home.click_mine_icon()
        # 判断是否登录成功，如果未登录就登录
        if not self.page.mine.if_login():
            self.page.mine.click_login_button()
            self.page.login.login(username, old_password)
        # 我的页面点击设置按钮
        time.sleep(1)
        self.page.mine.click_settings_button()
        # 设置界点击"修改密码"按钮
        time.sleep(1)
        self.page.settings.click_change_password_button()
        # 修改密码界面，输入旧密码
        time.sleep(1)
        self.page.change_password.input_old_password(old_password)
        # 修改密码界面，输入新密码
        time.sleep(1)
        self.page.change_password.input_new_password(new_password)
        # 修改密码界面，输入确认密码
        time.sleep(1)
        self.page.change_password.input_confirm_password(confirm_password)
        # 修改密码界面，点击保存按钮
        self.page.change_password.click_save_button()
        time.sleep(1)
        # 提示密码修改成功
        assert self.page.settings.if_toast_exist(toast_msg)
