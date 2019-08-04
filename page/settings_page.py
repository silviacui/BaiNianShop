# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction

class SettingsPage(BaseAction):

    # 地址管理按钮
    manage_address_button = By.XPATH, "text,地址管理"

    def click_manage_address_button(self):
        self.click(self.manage_address_button)
