# -*- coding: utf-8 -*-
from .home_page import *
from .mine_page import *
from .login_page import *
from .settings_page import *
from .about_bainian_page import *
from .address_page import *
from .add_address_page import *
from .cities_page import *
from .change_password_page import *


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

    @property
    def settings(self):
        return SettingsPage(self.driver)

    @property
    def about_bainian(self):
        return AboutBainianPage(self.driver)

    @property
    def address(self):
        return AddressPage(self.driver)

    @property
    def add_address(self):
        return AddAddressPage(self.driver)

    @property
    def cities(self):
        return CitiesPage(self.driver)

    @property
    def change_password(self):
        return ChangePasswordPage(self.driver)


