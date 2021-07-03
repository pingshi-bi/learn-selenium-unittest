import unittest

#unittest测试框架，测试用例的编写
#testcase 测试用例
#组成和基本运行逻辑
#类和面向对象
class TestMyCase3(unittest.TestCase):

    def test_1(self):
        print("do3 test1")
        
    def test_2(self):
        print("do3 test2")
        
    def test_3(self):
        print("do3 test3")

    def test_4(self):
        print("do3 test4")


class TestMyCase4(unittest.TestCase):

    def test_1(self):
        print("do4 test1")

    def test_2(self):
        print("do4 test2")

    def test_3(self):
        print("do4 test3")

    def test_4(self):
        print("do4 test4")

if __name__ == '__main__':
    unittest.main()


