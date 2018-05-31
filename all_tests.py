#coding=utf-8
'''
Created on 2017-6-14
@author: 灵枢
Project:通过测试套件执行多个测试用例，并生成报告
'''
import HTMLTestRunner
import unittest
import os
import time


def createsuite1():
    tc_path = os.path.join('selenium_python2', 'test_case')
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        tc_path, pattern='start_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    out_path = os.path.join('selenium_python2', 'report')
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    fn = os.path.join(out_path, now + "_result.html")
    fp = open(fn, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'搜索功能测试报告',
        description=u'用例执行情况：')

    runner.run(createsuite1())

    #关闭文件流，不关的话生成的报告是空的
    fp.close()
