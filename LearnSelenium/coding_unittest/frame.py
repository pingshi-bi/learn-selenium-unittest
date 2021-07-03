import unittest

#unittest测试框架，测试用例的编写
#testcase 测试用例
#组成和基本运行逻辑
#类和面向对象
class TestMyCase(unittest.TestCase):
    def setUp(self):
        print("---->setup")

    def tearDown(self):
        print("--->tesrdown")

    def test_assertEqual(self):
        print("assertEqual")
        a = 1
        b = 1
        self.assertEqual(a,b)
    def test_assertNotEqual(self):
        print("assertNotEqual")
        a = 1
        b = 2
        self.assertNotEqual(a,b)

    def test_assertIn(self):
        print("assertIn")
        X = 'P'
        b = 'Python'
        self.assertIn(X,b)

    def test_assertNotIn(self):
        print("assertNotIn")
        X = 'P'
        b = 'Python'
        self.assertNotIn(X, b)

    #tuple set  dict
    def test_assertListEqual(self):
        print("assertListEqual")
        X = [1,2,3,4,5]
        b = [i for i in range(1,5)]
        self.assertNotIn(X, b)

    def test_True(self):
        print("test True")
        Bool = True and 0
        self.assertTrue(Bool)
    def mydiv(self,a,b):
        return a/b

    def test_div(self):
        print("zero wrong")
        self.assertRaises(ZeroDivisionError,self.mydiv(3,0))


if __name__ == '__main__':
    unittest.main()


