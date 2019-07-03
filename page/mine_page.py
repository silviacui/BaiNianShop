# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from base import BaseAction


class MinePage(BaseAction):

    login_button = By.XPATH, "text,已有账号"

    def click_login_button(self):

        self.click(self.login_button)
