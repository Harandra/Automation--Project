import time
import unittest

from selenium import webdriver

from Seleniumlab.Utilities.ExcelOperation import ExcelUtil
from Seleniumlab.pages.Demopage import demoPage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path="C:/Driver/edgedriver_win64 (2)/msedgedriver.exe")
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()

    def test_demo1(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/harandra.jb/Desktop/New folder/TestData_python.xlsx")
        v = demoPage(self.driver)
        v.entersign()
        time.sleep(3)
        for i in range(2, exl.rowCount()):
            v.entername(exl.readData(i, 1))
            v.enterpass(exl.readData(i, 2))
            v.entersignup()
            time.sleep(3)
            self.driver.switch_to.alert.accept()
            time.sleep(3)

    def test_demo6(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/harandra.jb/Desktop/New folder/TestData_python.xlsx")
        v2 = demoPage(self.driver)
        for i in range(2, exl.rowCount()):
            v2.enterlogin()
            time.sleep(3)
            v2.enteruser(exl.readData(i, 1))
            v2.enterpass1(exl.readData(i, 2))
            time.sleep(3)
            v2.enterlog()
            time.sleep(5)
            act1 = v2.logouting()
            exp1 = "Log out"
            self.assertEqual(exp1, act1)

    def test_demo2(self):
        vv = demoPage(self.driver)
        time.sleep(2)
        vv.Phonenokia()
        time.sleep(5)
        vv.Addtocart()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        vv.Cartbutton()
        time.sleep(5)
        exp2 = vv.chekcart()
        act2 = "Nokia lumia 1520"
        self.assertEqual(exp2, act2)

    def test_demo3(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/harandra.jb/Desktop/New folder/TestData_python.xlsx")
        vvv = demoPage(self.driver)
        time.sleep(2)
        vvv.Phonenokia()
        time.sleep(5)
        vvv.Addtocart()
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        vvv.Cartbutton()
        time.sleep(3)
        vvv.buttonpress()
        time.sleep(3)
        for i in range(2,exl.rowCount()):
            vvv.name(exl.readData(i, 3))
            vvv.country(exl.readData(i, 4))
            vvv.city(exl.readData(i, 5))
            vvv.credit(exl.readData(i, 6))
            vvv.month(exl.readData(i, 7))
            vvv.year(exl.readData(i, 8))
            time.sleep(3)
            vvv.purchase()
            time.sleep(3)
            act3 = vvv.thankyou()
            exp3 = "Thank you for your purchase!"
            self.assertEqual(exp3, act3)

    def test_demo4(self):
        exl = ExcelUtil()
        exl.loadfile("C:/Users/harandra.jb/Desktop/New folder/TestData_python.xlsx")
        print(exl.rowCount())
        vvvv = demoPage(self.driver)
        vvvv.lap()
        time.sleep(3)
        vvvv.sony()
        time.sleep(3)
        exp4 = vvvv.head()
        act4 = "Sony vaio i5"
        self.assertEqual(exp4, act4)

    def test_demo5(self):
        v1 = demoPage(self.driver)
        v1.moni()
        time.sleep(3)
        v1.app()
        time.sleep(3)
        exp5 = v1.head1()
        act5 = "Apple monitor 24"
        self.assertEqual(exp5, act5)

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
