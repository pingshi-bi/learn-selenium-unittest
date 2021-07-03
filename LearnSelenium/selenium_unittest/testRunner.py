# -*- coding: utf-8 -*-
# @Time : 2021/6/25 21:33 
# @Author : pingshi-bi
# @File : Testrunner.py

import os
import unittest
from    HTMLTestRunner import HTMLTestRunner
from testcase_login import  loginTestcase
from testCase_apply import testCase_apply



report_dir = './reports/'
report_file =report_dir + 'testproject_reports.html'
#判断reports文件夹是否存在，不存在自动创建

if not os.path.exists(report_dir):
    os.mkdir(report_dir)
#打开测试报告文件，写入测试报告内容
with open(report_file,"wb") as rf:
    module_path = './'
    suite = unittest.TestSuite()

    #获取文件名：#解决被ddt装饰器，如何来按需写入
    for t in unittest.TestLoader().getTestCaseNames(loginTestcase):
        if t.startswith("test_1"):
            suite.addTest(loginTestcase(t))
    #使用装载器
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(loginTestcase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCase_apply))
    #discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern='testcase_login.py')
    #使用html执行器
    runner = HTMLTestRunner(title= 'testCase UI自动化测试报告',description='需求填写正例',stream= rf, )
    runner.run(suite)