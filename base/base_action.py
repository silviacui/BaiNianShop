# -*- coding: utf-8 -*-
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
        return wait.until(lambda x: x.find_element(by, value))

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
