# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class ChangePasswordPage(BaseAction):

    # 旧密码输入框
    edit_old_password = By.ID, "com.yunmall.lc:id/text_setting_old_pwd"
    # 新密码输入框
    edit_new_password = By.ID, "com.yunmall.lc:id/text_setting_new_pwd"
    # 确认密码输入框
    edit_confirm_password = By.ID, "com.yunmall.lc:id/text_setting_repwd"
    # 保存按钮
    save_button = By.XPATH, "text,保存"

    def input_old_password(self, old_password):
        self.input(self.edit_old_password, old_password)

    def input_new_password(self, new_password):
        self.input(self.edit_new_password, new_password)

    def input_confirm_password(self, confirm_password):
        self.input(self.edit_confirm_password, confirm_password)

    def click_save_button(self):
        self.click(self.save_button)