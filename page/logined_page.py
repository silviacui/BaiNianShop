# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from base import BaseAction


class LoginedPage(BaseAction):

    my_avatar_icon = By.ID, "com.yunmall.lc:id/iv_my_avatar_stroke"

    def is_my_avatar_icon_enabled(self):
        """
        判断人头图像是否enabled
        :return:
        """
        return self.is_feature_enabled(self.my_avatar_icon)