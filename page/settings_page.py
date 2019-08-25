# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction

class SettingsPage(BaseAction):

    # 地址管理按钮
    manage_address_button = By.XPATH, ("package,com.yunmall.lc", "text,地址管理")
    # 关于百年里奥按钮
    about_bainian_button = By.XPATH, "text,关于百年奥莱"
    # 用两种参数定位该元素，确保一定能找到它
    feature_list = By.XPATH, ("package,com.yunmall.lc", "text,关于百年奥莱")

    def click_manage_address_button(self):
        self.click(self.manage_address_button)

    def click_about_bainian_button(self):
        self.click(self.about_bainian_button)

