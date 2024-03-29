import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _user_settings_icon = "//*[@id='navbar']/div/div/div/ul/li[4]/ul/li[5]/a"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        # self.waitForElement(self._user_settings_icon,
        #                     locatorType="xpath")
        self.waitForElement("//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        result = self.isElementPresent(locator="//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        # result = self.isElementPresent(locator=self._user_settings_icon,
        #                               locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator="//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        #logoutLinkElement = self.waitForElement(self._user_settings_icon,
        #                                        locatorType="xpath", pollFrequency=1)

        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                            locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=logoutLinkElement)

        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']", locatorType="xpath")
        # self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
