
import  unittest
from MyTestCase1 import TestMyCase1
from MyTestCase2 import TestMyCase2
import MyTestCase_module
import os
from   HTMLTestRunner import HTMLTestRunner
#测试套件必须在独立的文件中
#测试套件和执行器
suite = unittest.TestSuite()

# 1. 实例化测试套件
suite.addTest(TestMyCase1('test_1'))
suite.addTest(TestMyCase1('test_2'))
suite.addTest(TestMyCase2('test_3'))
suite.addTest(TestMyCase2('test_4'))
#2. 多个测试用例
suite.addTests([TestMyCase1('test_1'),TestMyCase1('test_2'),TestMyCase2('test_3'),TestMyCase2('test_3')])

#3. 使用变量,使用了列表保证数据的顺序
cases = [
    TestMyCase1('test_1'),
    TestMyCase1('test_2'),
    TestMyCase2('test_3'),
    TestMyCase2('test_3')
]
suite.addTests(cases)
#4.使用装载器--等同于使用了原测试用例下的main()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMyCase1))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMyCase2))

#使用名字方法
suite.addTests(unittest.TestLoader().loadTestsFromName("MyTestCase1.TestMyCase1"))
suite.addTests(unittest.TestLoader().loadTestsFromNames(["MyTestCase2.TestMyCase2","MyTestCase2.TestMyCase2"]))
suite.addTests(unittest.TestLoader().loadTestsFromModule(MyTestCase_module))
#使用模块
runner  = unittest.TextTestRunner()
runner.run(suite)


#载入多个模块
module_path = './'
discover = unittest.defaultTestLoader.discover(start_dir=module_path,pattern= 'MyTestCase*.py')

runner = unittest.TextTestRunner()
runner.run(discover)

#通过网络下载HTMLTestRunner
# http://tungwaiyip.info/software/HTMLTestRunner.html

report_dir = './reports/'
report_file = 'html_reports.html'
#判断reports文件夹是否存在，不存在自动创建

if not os.path.exists(report_dir):
    os.mkdir(report_dir)
#打开测试报告文件，写入测试报告内容
with open(report_file,"wb") as rf:
    module_path = './'
    discover = unittest.defaultTestLoader.discover(start_dir=module_path, pattern='MyTestCase*.py')
    #使用html执行器
    runner = HTMLTestRunner(title= '测试标题',description='描述这一次测试的大致内容',stream= rf )
    runner.run(discover)













