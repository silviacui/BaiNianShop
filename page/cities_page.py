# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction
import random


class CitiesPage(BaseAction):

    # 地区的feature
    region_feature = By.ID, "com.yunmall.lc:id/area_title"
    # 保存按钮
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    def random_choose_region(self):
        region_string = ""
        for i in range(2):
            self.random_choose_one_feature_click(self.region_feature)
        if not self.if_save_button_exist:
            self.random_choose_one_feature_click(self.region_feature)

    # 随机选取一个元素并点击
    def random_choose_one_feature_click(self, feature):
        # 获取页面所有的同类型的eles列表
        feature_list = self.find_elements(feature)
        # 随机抽取列表中一个元素，并点击
        random.sample(feature_list, 1)[0].click()

    @property
    def if_save_button_exist(self):
        return self.if_feature_exist(self.save_button)
