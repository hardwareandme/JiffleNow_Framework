from base.selenium_cust_drivers import seleniumDriver
import utilities.custom_logger as cl
import logging,time
#Define a class to login to Calendar
#Inherit our own custom selenium driver class

class loginPage(seleniumDriver):

    #Call logger to log for login page and store logs in our path (calendarAutomation.log)

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    #Define all Locators to get all web elements in Login Page
    #If any element changes, than just update  / add / delete locator from here

    #####LOCATORS###########
    ########################

    _email_field = 'identifierId'
    _email_next = 'identifierNext'
    _password_field = "//div[@id='password']/div[1]/div/div[1]/input"
    _password_next = 'passwordNext'
    _login_success_criteria = "//header[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span"
    _login_failed_criteria = "//div[contains(text(),'Wrong password.')]"

    #call our apis to enter email, click next , enterpassword and click password

    def enterUsername(self,email):
        self.sendKeys(email,self._email_field)

    def clickEmailNext(self):
        self.elementClick(self._email_next)

    def enterPasswordField(self,password):
        self.sendKeys(password,self._password_field,locatorType="xpath")

    def clickPasswordNext(self):
        self.elementClick(self._password_next)

    #define login method and sequence to login user successfully

    def login(self,email="",password=""):
        self.enterUsername(email)
        self.clickEmailNext()
        self.enterPasswordField(password)
        time.sleep(5)
        self.clickPasswordNext()

    #Define method for Login Success criteria
    def loginSuccess(self):
        result = self.isElementPresent(self._login_success_criteria,locatorType="xpath")
        return result

    #Define a method for Login Failure criteria

    def loginFail(self):
        result = self.isElementPresent(self._login_failed_criteria,locatorType="xpath")
        return result