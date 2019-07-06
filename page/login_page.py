# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    input_username_button = By.XPATH, "text,请输入手机/昵称"
    input_password_button = By.XPATH, "resource-id,com.yunmall.lc:id/logon_password_textview"
    login_button = By.XPATH, ("text,登录" ,"resource-id,com.yunmall.lc:id/logon_button")

    def input_username(self, username):
        # 输入用户名
        self.input(self.input_username_button, username)

    def input_password(self, password):
        # 输入密码
        self.input(self.input_password_button, password)

    def click_login(self):
        # 点击登录按钮
        self.click(self.login_button)
