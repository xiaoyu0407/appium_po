from appium import webdriver

from page.profile_page import ProfilePage
from page.search_page import SearchPage



class XueqiuPage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(25)
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        el1.click()

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return  SearchPage(self.driver)

    def goto_profile(self):
        return  ProfilePage()

    def get_ads(self):
        return False