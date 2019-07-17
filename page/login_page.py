# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginPage(BaseAction):

    input_username_button = By.XPATH, "text,请输入手机/昵称"
    input_password_button = By.XPATH, "resource-id,com.yunmall.lc:id/logon_password_textview"
    login_button = By.XPATH, ("text,登录" ,"resource-id,com.yunmall.lc:id/logon_button")

    @allure.step(title="登录页面输入用户名")
    def input_username(self, username):
        allure.attach("输入用户名", username)  # 此方法可以在报告中显示输入的数据内容，但是要点击一下
        # 输入用户名
        self.input(self.input_username_button, username)

    @allure.step(title="登录页面输入密码")
    def input_password(self, password):
        allure.attach("输入密码" + password, "")  # 此方法可以在报告中显示输入的数据内容，不需要再点击
        # 输入密码
        self.input(self.input_password_button, password)

    @allure.step(title="登录页面点击登录按钮")
    def click_login(self):
        # 点击登录按钮
        self.click(self.login_button)

    def is_login_button_enabled(self):
        """
        判断登录按钮的enabled状态
        :return:
        """
        return self.is_feature_enabled(self.login_button)
