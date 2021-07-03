import unittest

#unittest测试框架，测试用例的编写
#testcase 测试用例
#组成和基本运行逻辑
#类和面向对象
class TestMyCase2(unittest.TestCase):

    def test_1(self):
        print("do2 test1")
        
    def test_2(self):
        print("do2test2")
        
    def test_3(self):
        print("do2 test3")

    def test_4(self):
        print("do2 test4")
if __name__ == '__main__':
    unittest.main()


