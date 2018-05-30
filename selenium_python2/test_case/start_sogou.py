# coding=utf-8
'''
Created on 2017-6-14
@author: 灵枢
Project:搜狗搜索测试用例
'''
from selenium import webdriver
import unittest, time

class SogouTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) #隐性等待时间为30秒
        self.base_url = "http://www.sogou.com"

    def test_sogou(self):
        u"""搜狗搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys(u"python3")
        driver.find_element_by_id("query").submit()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, u"python2 - 搜狗搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()