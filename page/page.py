# -*- coding: utf-8 -*-
from .home_page import HomePage
from .mine_page import MinePage
from .login_page import LoginPage


class Page():

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

