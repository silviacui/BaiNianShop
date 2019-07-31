# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginedPage(BaseAction):

    my_avatar_icon = By.ID, "com.yunmall.lc:id/iv_my_avatar_stroke"
    settings_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

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
        if_login = self.if_my_avatar_icon_exist()
        self.click_settings_button()
        return if_login

        # 写法一
        # if self.if_my_avatar_icon_exist():
        #     self.click_settings_button()
        #     return True
        # else:
        #     return False
