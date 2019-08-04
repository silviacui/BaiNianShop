# -*- coding: utf-8 -*-

from base import init_driver
from page import Page
import pytest
from base import data_analyze


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # login场景一：未登录成功，有错误提示的场景
    # @pytest.mark.parametrize("args",data_analyze("test_login"))
    # def test_login(self,args):
    #
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     # 点击主页的我图标
    #     self.page.home.click_mine_icon()
    #     # 点击我的页面的”已有账号，去登录“
    #     self.page.mine.click_login_button()
    #     # 登录页面输入账号和密码，并点击登录按钮
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login()
    #     # 判断toast
    #     # if "此用户不存在" == self.page.login.find_toast("此用户不存在"):
    #     #     assert True
    #     # else:
    #     #     assert False
    #     assert self.page.login.if_toast_exist(expect)

    # login场景二：未登录成功，使用一个参数登录的场景
    # @pytest.mark.parametrize("args", data_analyze("test_login_with_blank_info"))
    # def test_login_with_blank_info(self, args):
    #
    #     username = args["username"]
    #     password = args["password"]
    #
    #     #点击主页的我图标
    #     self.page.home.click_mine_icon()
    #     # 点击我的页面的”已有账号，去登录“
    #     self.page.mine.click_login_button()
    #     # 登录页面输入账号和密码，并点击登录按钮
    #     # 判断用户名和密码数据的状态
    #     if username == "":
    #         self.page.login.input_password(password)
    #     elif password == "":
    #         self.page.login.input_username(username)
    #     # 当登录按钮enabled状态为false的时候，才是执行成功
    #     # 方法一：
    #     assert not self.page.login.is_login_button_enabled()
        # 方法二：
        # if self.page.login.is_login_button_enabled():
        #     assert False
        # else:
        #     assert True

    # login场景三：登录成功的场景
    # @pytest.mark.parametrize("args", data_analyze("test_login_success"))
    # def test_login_success(self, args):
    #
    #     username = args["username"]
    #     password = args["password"]
    #
    #     # 点击主页的我图标
    #     self.page.home.click_mine_icon()
    #     # 点击我的页面的”已有账号，去登录“
    #     self.page.mine.click_login_button()
    #     # 登录页面输入账号和密码，并点击登录按钮
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login()
    #     # 在已登录页面，定位人头图像，并判断该按钮是否enabled
    #     assert self.page.mine.if_my_avatar_icon_exist() and self.page.mine.is_my_avatar_icon_enabled()

    def test_if_login(self):
        # 点击主页的我图标
        self.page.home.click_mine_icon()
        # 判断是否登录成功
        assert self.page.mine.if_login()

