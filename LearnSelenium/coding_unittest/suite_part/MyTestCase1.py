import unittest

#unittest测试框架，测试用例的编写
#testcase 测试用例
#组成和基本运行逻辑
#类和面向对象
class TestMyCase1(unittest.TestCase):

    def test_1(self):
        print("do1 test1")

    def test_2(self):
        print("do1 test2")

    def test_3(self):
        print("do1 test3")
        a =1
        b=2
        self.assertEqual(a,b)

    def test_4(self):
        print("do1 test4")

if __name__ == '__main__':
    unittest.main()


