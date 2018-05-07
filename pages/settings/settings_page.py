from base.selenium_cust_drivers import seleniumDriver
import utilities.custom_logger as cl
import logging,time
from pages.login.login_page import loginPage
from selenium.webdriver.common.keys import Keys

class settingsPage(seleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        #####LOCATORS###########
        ########################

    _settings_Menu = "//header[@id='gb']/div[2]/div[2]/div[3]/div/div/div[3]/div/content/span"
    _settings = "html/body/div[20]/div/div/content[1]/div[2]/div"
    _time_format_field = "//*[@id='YPCqFe']/div/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div[2]"
    _time_format24 = "//*[@id='YPCqFe']/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/content"
    _time_format12 = "//*[@id='YPCqFe']/div/div/div/div[1]/div[3]/div/div/div[2]/div[1]/content"
    _create_event = "//i[contains(@class,'Gw6Zhc')]"
    _meeting_start_time = "//*[@id='xStTiIn']"
    _meeting_end_time = "//input[@id='xEnTiIn']"
    _event_Title = "//*[@id='xTiIn']"
    _weekStart = "//*[@id='YPCqFe']/div/div/div[1]/div[2]/div[1]/div/div[1]/h2/div[1]"

    #Expose all locators here as an element

    def clickSettingsButton(self):
        self.elementClick(self._settings_Menu,locatorType="xpath")

    def clickSettings(self):
        self.elementClick(self._settings,locatorType="xpath")

    def selectTimeFormat(self):
        self.elementClick(self._time_format_field,locatorType="xpath")

    def clickTimeFormat24(self):
        self.elementClick(self._time_format24,locatorType="xpath")

    def clickTimeFormat12(self):
        self.elementClick(self._time_format12,locatorType="xpath")

    def createEvent(self):
        self.elementClick(self._create_event,locatorType="xpath")

    def selectStartMeetingTime(self,startTime):
        self.sendKeys(startTime,self._meeting_start_time,locatorType="xpath")
        self.sendKeys(Keys.ENTER,self._meeting_start_time,locatorType="xpath")

    def selectEndMeetingTime(self,endTime):
        self.sendKeys(endTime,self._meeting_end_time,locatorType="xpath")
        self.sendKeys(Keys.ENTER,self._meeting_end_time,locatorType="xpath")

    def eventTitle(self):
        self.elementClick(self._event_Title,locatorType="xpath")

    def weekstart(self):
        weekStart = self.getElement(self._weekStart,locatorType="xpath")
        return weekStart.text


    def time24Check(self,startTime,endTime):
        self.clickSettingsButton()
        time.sleep(3)
        self.clickSettings()
        time.sleep(3)
        self.selectTimeFormat()
        time.sleep(3)
        self.clickTimeFormat24()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.createEvent()
        self.selectStartMeetingTime(startTime)
        self.selectEndMeetingTime(endTime)
        self.eventTitle()
        time.sleep(3)









