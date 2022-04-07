from selenium import webdriver

from Seleniumlab.locators.Demolocater import demolocate


class demoPage():
    def __init__(self, driver):
        # driver = webdriver.Edge(executable_path="C:/Driver/edgedriver_win64/msedgedriver.exe")
        self.driver = driver
        self.a = demolocate.Sign_up_ID
        self.b = demolocate.Username_ID
        self.c = demolocate.Password_ID
        self.d = demolocate.Sign_up_XP
        self.f = demolocate.Close_XP
        self.g = demolocate.Log_in_LT
        self.h = demolocate.Username2_ID
        self.i = demolocate.Password2_ID
        self.j = demolocate.Log_in_XP
        # self.k = demolocate.Phone_LT
        self.k = demolocate.phone_XP
        self.l = demolocate.Addtocart_LT
        self.m = demolocate.Cartbtn_ID
        self.n = demolocate.Checkcart_XP
        self.o = demolocate.logout_ID
        self.p = demolocate.button_XP
        self.q = demolocate.name_ID
        self.r = demolocate.country_ID
        self.s = demolocate.city_ID
        self.t = demolocate.Creditcard_ID
        self.u = demolocate.Month_ID
        self.v = demolocate.Year_ID
        self.w = demolocate.Purchase_XP
        self.x = demolocate.Thanks_XP
        self.y = demolocate.Laptop_LT
        self.z = demolocate.Sony_LT
        self.aa = demolocate.sony_Head_XP
        self.ab = demolocate.Monitors_LT
        self.ac = demolocate.Apple_LT
        self.ad = demolocate.moni_head_XP

    def entersign(self):
        self.driver.find_element_by_id(self.a).click()

    def entername(self, b):
        self.driver.find_element_by_id(self.b).send_keys(b)

    def enterpass(self, c):
        self.driver.find_element_by_id(self.c).send_keys(c)

    def entersignup(self):
        self.driver.find_elements_by_xpath(self.d)[5].click()

    def enterclose(self):
        self.driver.find_elements_by_xpath(self.f)[4].click()

    def enterlogin(self):
        self.driver.find_element_by_link_text(self.g).click()

    def enteruser(self, h):
        self.driver.find_element_by_id(self.h).send_keys(h)

    def enterpass1(self, i):
        self.driver.find_element_by_id(self.i).send_keys(i)

    def enterlog(self):
        self.driver.find_elements_by_xpath(self.j)[8].click()

    def Phonenokia(self):
        self.driver.find_elements_by_xpath(self.k)[1].click()

    def Addtocart(self):
        self.driver.find_element_by_link_text(self.l).click()

    def Cartbutton(self):
        self.driver.find_element_by_id(self.m).click()

    def chekcart(self):
        n = self.driver.find_elements_by_xpath(self.n)[1].text
        return n

    def logouting(self):
        o = self.driver.find_element_by_id(self.o).text
        return o

    def buttonpress(self):
        self.driver.find_elements_by_xpath(self.p)[29].click()

    def name(self, q):
        self.driver.find_element_by_id(self.q).send_keys(q)

    def country(self, r):
        self.driver.find_element_by_id(self.r).send_keys(r)

    def city(self, s):
        self.driver.find_element_by_id(self.s).send_keys(s)

    def credit(self, t):
        self.driver.find_element_by_id(self.t).send_keys(t)

    def month(self, u):
        self.driver.find_element_by_id(self.u).send_keys(u)

    def year(self, v):
        self.driver.find_element_by_id(self.v).send_keys(v)

    def purchase(self):
        self.driver.find_elements_by_xpath(self.w)[8].click()

    def thankyou(self):
        val3 = self.driver.find_elements_by_xpath(self.x)[2].text
        return val3

    def lap(self):
        self.driver.find_element_by_link_text(self.y).click()

    def sony(self):
        self.driver.find_element_by_link_text(self.z).click()

    def head(self):
        val4 = self.driver.find_elements_by_xpath(self.aa)[0].text
        return val4

    def moni(self):
        self.driver.find_element_by_link_text(self.ab).click()

    def app(self):
        self.driver.find_element_by_link_text(self.ac).click()

    def head1(self):
        val4 = self.driver.find_elements_by_xpath(self.ad)[0].text
        return val4
