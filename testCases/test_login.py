from pageObjects.loginPage import LoginPage
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    # this will return a logger object to access loggen() method present inside customLogger.py file
    # Now, by using logger object we can send log msgs to our log file (i.e. automation.log)

    def test_homePageTitle(self, setup):


        self.logger.info("********** Test_001_Login **********")  # first step is to add testCase ID
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        self.driver.implicitly_wait(10)
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title test is Passed **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page Title test is Failed **********")
            assert False

    def test_login(self, setup):

        self.logger.info("********** Verifying Login Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.implicitly_wait(5)
            self.lp.clickLogout()
            self.driver.close()
            self.logger.info("********** Login test is Passed **********")
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.error("********** Login test is Failed **********")
            assert False
