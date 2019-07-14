# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class MinePage(BaseAction):

    login_button = By.XPATH, "text,已有账号"

    @allure.step(title="我的页面点击'已有账户，去登录'按钮")
    def click_login_button(self):

        self.click(self.login_button)
