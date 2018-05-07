from selenium import webdriver
from pages.settings.settings_page import settingsPage
import unittest
import os,time
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class settingsTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = settingsPage(self.driver)

    # def test_24hFormat(self):
    #     result = self.sp.time24Check("11","13")
    def test(self):
        result = self.sp.weekstart()
        print(result)

