# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class MinePage(BaseAction):

    login_button = By.XPATH, "text,已有账号"
    # 下面是登录之后，我的页面才有的按钮
    my_avatar_icon = By.ID, "com.yunmall.lc:id/iv_my_avatar_stroke"
    settings_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    @allure.step(title="我的页面点击'已有账户，去登录'按钮")
    def click_login_button(self):

        self.click(self.login_button)

    # 登录之后的动作
    def if_my_avatar_icon_exist(self):
        """
        判断人头图像是否enabled
        :return:
        """
        return self.if_feature_exist(self.my_avatar_icon)

    def is_my_avatar_icon_enabled(self):
        """
        判断人头图像是否enabled
        :return:
        """
        return self.is_feature_enabled(self.my_avatar_icon)

    def click_settings_button(self):
        self.click(self.settings_button)

    # 判断是否登录
    def if_login(self):
        # 写法二：
        # 判断人头图标存不存在，并把结果存到if_login
        if_login = self.if_my_avatar_icon_exist()
        self.click_settings_button()
        return if_login

        # 写法一
        # if self.if_my_avatar_icon_exist():
        #     self.click_settings_button()
        #     return True
        # else:
        #     return False

