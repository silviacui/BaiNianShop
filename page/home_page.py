# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class HomePage(BaseAction):

    mine_icon = By.XPATH, ("text,我", "resource-id,com.yunmall.lc:id/tab_me")

    @allure.step(title="主页点击我的按钮")
    def click_mine_icon(self):

        self.click(self.mine_icon)


