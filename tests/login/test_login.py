from selenium import webdriver
from pages.login.login_page import loginPage
import unittest
import os,time
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class loginTests(unittest.TestCase):

    #create an object of the login page class
    #use pytest fixture to define class level setup
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = loginPage(self.driver)

    #define a method for valid login that takes valid email and password as parameters
    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("testsel35","testme123")
        result = self.lp.loginSuccess()
        assert result == True

    #define a method for invalid login that can take any combination of email or password
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("testsel35","test")
        time.sleep(5)
        result = self.lp.loginFail()
        assert result == True