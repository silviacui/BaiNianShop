# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction

class SettingsPage(BaseAction):

    # 地址管理按钮
    manage_address_button = By.XPATH, "text,地址管理"
    # 关于百年里奥按钮
    about_bainian_button = By.XPATH, "text,关于百年里奥"
    feature_list = By.XPATH, "package,com.yunmall.lc"

    def click_manage_address_button(self):
        self.click(self.manage_address_button)

    # def if_find_about_bainian_button(self):
    #     return self.if_scroll_until_feature_found(self.feature_list, "关于百年里奥","up")
    #
    # def click_about_bainian_button(self):
    #     self.click(self.about_bainian_button)

