import time
import allure
import moment
from selenium import webdriver
import pytest
from pages.loginPage import Loginpage
from pages.homePage import HomePage
from utils import utils as utils


# def pytest_(adoption(parser):
#  parser.adoption("--browser", action="store", def(ult="chrome", help="Type in browser name e.g.chrome OR firefox")
#
#     browser = request.config.getoption("--browser")
#
#     if browser == 'chrome':
#         driver = webdriver.Chrome(
#             executable_path=r"C:/Users/PC/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe"))
#     elif browser ='firefox'
#             driver = webdriver.Firefox())


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = Loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login(driver)

    def test_logout(self):

        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
            time.sleep(1)
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoami()
            schreenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_schreenshot_as_png(), name=schreenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_schreenshot_as_file("C:/Users/PC/PycharmProjects/AutomationFramework_1/schreenshots"
                                           + schreenshotName + ".png")
            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoami()
            schreenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_schreenshot_as_png(), name=schreenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        else:
            print("No exception occurred")
        finally:
            print("I am inside finally block")
# @pytest.fixture(scope="class")
#     def test_setup(self):
#         global driver
#         driver = webdriver.Chrome(
#             executable_path=r"C:/Users/PC/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
#         driver.implicitly_wait(5)
#         driver.maximize_window()
#         yield
#         driver.close()
#         driver.quit()
#         print("Test Completed")
