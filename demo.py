# -*-  coding:utf-8 -*-

from appium import webdriver


# server启动参数
desired_caps = {}

# 设备参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'MDQNW17331025978'

# app参数
desired_caps['appPackage'] = 'com.yunmall.lc'
desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

# 解决输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
