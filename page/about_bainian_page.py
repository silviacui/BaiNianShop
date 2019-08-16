# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from base import BaseAction

class AboutBainianPage(BaseAction):

    app_version = By.ID, "com.yunmall.lc:id/about_version_text"

    def get_app_version_text(self):
        return self.find_element(self.app_version).text