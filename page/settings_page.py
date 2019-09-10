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
    # 退出按钮
    logout_button_feature = By.XPATH, ("text,退出", "resource-id,com.yunmall.lc:id/setting_logout")
    # 修改密码按钮
    change_password_button = By.XPATH, "text,修改密码"
    # 退出确认按钮
    logout_confirm_button = By.XPATH, ("resource-id,com.yunmall.lc:id/ymdialog_right_button", "text,确认")

    def click_manage_address_button(self):
        self.click(self.manage_address_button)

    def click_about_bainian_button(self):
        self.click(self.about_bainian_button)

    def click_change_password_button(self):
        self.click(self.change_password_button)

    def click_logout_button_feature(self):
        self.click(self.logout_button_feature)

    def click_logout_confirm_button(self):
        self.click(self.logout_confirm_button)