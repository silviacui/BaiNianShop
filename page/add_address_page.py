# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class AddAddressPage(BaseAction):

    # 收件人姓名
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    # 收件人 手机号
    mobile_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    # 收件人 详细地址
    detail_address_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    # 地区按钮
    region_button = By.ID, "com.yunmall.lc:id/address_province"
    # 保存按钮
    save_button = By.ID,"com.yunmall.lc:id/button_send"

    def input_receiver_name(self, name):
        self.input(self.name_edit_text, name)

    def input_mobile_number(self, mobile):
        self.input(self.mobile_edit_text, mobile)

    def input_detail_address(self, address):
        self.input(self.detail_address_edit_text, address)

    def click_region_button(self):
        self.click(self.region_button)

    def click_save_button(self):
        self.click(self.save_button)

    @property
    def get_region_text(self):
        return self.find_element(self.region_button).text





