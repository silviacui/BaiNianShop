# -*- coding: utf-8 -*-
import  time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, feature):
        """
        根据特征，进行查找并点击
        :param feature: 特征
        :return:
        """
        self.find_element(feature).click()

    def input(self, feature, content):
        """
        根据特征，进行查找并输入
        :param feature: 特征
        :param content: 输入内容
        :return:
        """
        self.find_element(feature).send_keys(content)

    def find_element(self, feature, timeout=5.0, poll=1.0):

        by = feature[0]
        value = feature[1]
        # 如果传过来的参数"feature[0]"等于By.XPATH,就执行下面两行代码，如果不是，就直接跳过这两行
        if by == By.XPATH:
            value = self.__make_xpath(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=5.0, poll=1.0):

        by = feature[0]
        value = feature[1]

        # 如果传过来的参数"feature[0]"等于By.XPATH,就执行下面两行代码，如果不是，就直接跳过这两行
        if by == By.XPATH:
            value = self.__make_xpath(value)
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    @staticmethod
    def __make_xpath_condition(feature):

        res_value = ""
        values = feature.split(",")
        # 输入三位参数
        if len(values) == 3:
            if values[2] == "1":
                res_value += "@%s='%s' and " % (values[0], values[1])
            elif values[2] == "0":
                res_value += "contains(@%s, '%s') and " % (values[0], values[1])

        # 输入两位参数
        elif len(values) == 2:
            res_value += "contains(@%s, '%s') and " % (values[0], values[1])

        # 输入非两位或三位参数，抛出异常
        else:
            raise Exception("输入的参数为二位或三位")

        return res_value

    def __make_xpath(self, value):

        xpath_start = "//*["
        xpath_end = "]"
        res_value = ""

        # 如果输入的参数为字符串
        if isinstance(value, str):
            if value.startswith("/"):
                return value
            else:
                res_value = self.__make_xpath_condition(value)

        # 如果输入的参数为元组
        elif isinstance(value, tuple):
            for i in value:
                res_value += self.__make_xpath_condition(i)

        # 删掉末尾多余的" and "
        value = res_value.rstrip(" and ")
        value = xpath_start + value + xpath_end
        return value

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        return self.find_element((By.XPATH, message), timeout=timeout, poll=0.1).text

        # element = WebDriverWait(self.driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
        # return element.text

    def if_toast_exist(self, message):
        """
        判断toast消息是否存在
        :param message:
        :return:
        """
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    def is_feature_enabled(self, feature):
        if self.find_element(feature).get_attribute("enabled") == "true":
            return True
        else:
            return False

    def if_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False

    def scroll_one_time(self, dir="up"):

        # 如果不等于滑动页面
        window_width = self.driver.get_window_size()["width"]
        window_height = self.driver.get_window_size()["height"]
        # 取页面尺寸的一半的值
        centre_x = window_width * 0.5
        centre_y = window_height * 0.5

        start_x, start_y, end_x, end_y = 0, 0, 0, 0

        if dir == "up" or dir == "down":
            start_x = centre_x
            start_y = window_height * 0.75
            end_x = centre_x
            end_y = window_height * 0.25

        elif dir == "left" or dir == "right":
            start_x = window_width * 0.75
            start_y = centre_y
            end_x = window_width * 0.25
            end_y = centre_y

        # 判断dir的参数值
        if dir == "up" or dir == "left":
            self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
        elif dir == "down" or dir == "left":
            self.driver.swipe(end_x, end_y, start_x, start_y, 3000)
        else:
            raise Exception("dir的参数只能是up/down/left/right")

    def if_scroll_until_feature_found(self, feature, feature_text, dir):
        """
        滑动当前页面，直到目标feature已经找到
        :param feature: 定位元素的feature
        :param feature_text: 定位元素的text
        :param dir: 滑动页面的方向，只能输入参数up/down/left/right
        :return:
        """
        old = ""
        # 无限循环
        while True:
            new = ""
            # 用find_elements定位到settings中所有的列表元素
            eles = self.find_elements(feature)
            # for循环取每个元素的text，判断是否等于“关于手机”，如果等于停止执行
            for i in eles:
                text = i.text
                # 把每一轮定位到的所有元素的text拼接到new里面
                new += text

                if text == feature_text:
                    return True

            if  old == new:
                return False
            else:
                old = new

            # 如果new不等于old，则继续滑动
            self.scroll_one_time(dir)
