# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    input_username = By.XPATH, "text,请输入手机/昵称"
    input_password = By.XPATH, "resource-id,com.yunmall.lc:id/logon_password_textview"
    login_button = By.XPATH, ("text,登录" ,"resource-id,com.yunmall.lc:id/logon_button")

    def input_username_passord_to_login(self, username, password):

        # 输入用户名
        self.input(self.input_username, username)
        # 输入密码
        self.input(self.input_password, password)
        # 点击登录按钮
        self.click(self.login_button)
