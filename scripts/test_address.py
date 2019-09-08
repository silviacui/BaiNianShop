# -*- coding: utf-8 -*-
import pytest
from base import data_analyze
from base import init_driver
from page import Page
import time

class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", data_analyze("test_address_success"))
    # def test_address_success(self, args):
    #
    #     name = args["name"]
    #     phone_number = args["phone_number"]
    #     detail_address = args["detail_address"]
    #
    #     # 主页，点击我的按钮
    #     self.page.home.click_mine_icon()
    #     # 我的页面，判断是否登录
    #     # 如果未登录
    #     if not self.page.mine.if_login():
    #         # 执行登录
    #         self.page.mine.click_login_button()
    #         self.page.login.login()
    #         time.sleep(1)
    #     # 我的页面，点击设置按钮
    #     self.page.mine.click_settings_button()
    #     time.sleep(1)
    #     # 滑动查找"地址管理"按钮，如果不存在，直接退出
    #     if not self.page.settings.if_feature_exist_scroll_page(self.page.settings.manage_address_button, "up"):
    #         assert False
    #     # 如果存在
    #     # 设置页面，点击地址管理按钮
    #     self.page.settings.click_manage_address_button()
    #     # 点击新增地址, 判断是否有toast"最多保存10个地址"存在
    #     self.page.address.if_address_amount_more_than_10()
    #     # 新增地址页面，输入收件人名
    #     time.sleep(1)
    #     self.page.add_address.input_receiver_name(name)
    #     # 新增地址页面，输入电话
    #     time.sleep(1)
    #     self.page.add_address.input_mobile_number(phone_number)
    #     # 点击地区按钮
    #     time.sleep(1)
    #     self.page.add_address.click_region_button()
    #     # 地区页面，随机点击
    #     self.page.cities.random_choose_region()
    #     # 完成后，回到新增地址页面,记录新增地址的text
    #     time.sleep(1)
    #     new_address_text = self.page.add_address.get_region_text
    #     # 新增地址页面，输入详细地址
    #     self.page.add_address.input_detail_address(detail_address)
    #     new_address_text += detail_address
    #     # 点击保存
    #     self.page.add_address.click_save_button()
    #     # 地址管理页面查看新增的地址是否存在
    #     time.sleep(1)
    #     assert self.page.add_address.if_feature_exist_scroll_page(self.page.address.generate_address_feature(new_address_text),"up")

    # 添加地址失败
    @pytest.mark.parametrize("args", data_analyze("test_address_fail"))
    def test_address_fail(self, args):

        name = args["name"]
        phone_number = args["phone_number"]
        detail_address = args["detail_address"]
        message_text = args["message"]

        # 主页，点击我的按钮
        self.page.home.click_mine_icon()
        # 我的页面，判断是否登录
        # 如果未登录
        if not self.page.mine.if_login():
            # 执行登录
            self.page.mine.click_login_button()
            self.page.login.login()
            time.sleep(1)
        # 我的页面，点击设置按钮
        self.page.mine.click_settings_button()
        time.sleep(1)
        # 滑动查找"地址管理"按钮，如果不存在，直接退出
        if not self.page.settings.if_feature_exist_scroll_page(self.page.settings.manage_address_button, "up"):
            assert False
        # 如果存在
        # 设置页面，点击地址管理按钮
        self.page.settings.click_manage_address_button()
        time.sleep(1)
        # 点击新增地址, 判断是否有toast"最多保存10个地址"存在
        self.page.address.if_address_amount_more_than_10()
        # 新增地址页面，输入收件人名
        time.sleep(1)
        self.page.add_address.input_receiver_name(name)
        # 新增地址页面，输入电话
        time.sleep(1)
        self.page.add_address.input_mobile_number(phone_number)
        # 点击地区按钮
        time.sleep(1)
        self.page.add_address.click_region_button()
        # 地区页面，随机点击
        self.page.cities.random_choose_region()
        time.sleep(1)
        # 新增地址页面，输入详细地址
        self.page.add_address.input_detail_address(detail_address)
        # 点击保存
        time.sleep(1)
        self.page.add_address.click_save_button()
        # 保存失败之后，确认弹的toast是否符合预期的
        assert self.page.add_address.if_toast_exist(message_text)

