# coding=utf-8
'''
Created on 2017-6-14
@author: 灵枢
Project:登录百度测试用例
'''
from selenium import webdriver
import unittest, time

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) #隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"

    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title=driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def test_baidu_set(self):
        u"""百度设置"""
        driver=self.driver
        driver.get(self.base_url+"/gaoji/preferences.html")
        m=driver.find_element_by_name("NR")
        time.sleep(1)
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()