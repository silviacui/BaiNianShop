# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from base import BaseAction


class AddressPage(BaseAction):

    # 新增地址按钮
    add_address_button = By.XPATH, ("text,新增地址", "resource-id,com.yunmall.lc:id/address_add_new_btn")
    # 编辑按钮
    edit_button = By.XPATH, "text,编辑"
    # 删除按钮列表
    delete_button_list = By.XPATH, ("resource-id,com.yunmall.lc:id/delete", "text,删除")
    # 确认删除按钮
    confirm_delete_button = By.XPATH, ("text,确认", "resource-id,com.yunmall.lc:id/ymdialog_left_button")

    def click_add_address_button(self):
        self.click(self.add_address_button)

    def generate_address_feature(self, new_address_text):
        first_feature = "resource-id,com.yunmall.lc:id/receipt_address"
        second_feature = "text," + new_address_text
        return By.XPATH, (first_feature, second_feature)

    # 点击新增地址, 判断是否有toast"最多保存10个地址"存在
    def if_address_amount_more_than_10(self):
        self.click_add_address_button()
        if self.if_toast_exist("最多保存10个地址"):
            # 点击编辑按钮
            self.click_edit_button()
            # 点击删除按钮，删除一个地址记录
            self.click_delete_button()
            self.click_confirm_delete_button()
            self.click_add_address_button()

    def click_edit_button(self):
        self.click(self.edit_button)

    def click_delete_button(self):
        self.find_element(self.delete_button_list).click()

    def click_confirm_delete_button(self):
        self.click(self.confirm_delete_button)


