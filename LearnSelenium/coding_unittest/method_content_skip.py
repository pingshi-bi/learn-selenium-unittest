import unittest

#方法关联与跳过
#类方法----夹具
#方法关联--@classmethod     def setupClass(cls):
#方法跳过--@unittestskip    def test_n(slef):
#类和对象，类方法，类属性，成员方法，成员属性，实例方法，实例属性！！！
#使用装饰器
class TestMyCase(unittest.TestCase):
    result = {"m" : False }

    @classmethod
    def setUpClass(cls):
        cls.name = "aaaa"
     #！！！！！！！！！！！！！！111
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print("---->setup")

    def tearDown(self):
        print("--->tesrdown")

    # 跳过
    @unittest.skip("这里填写跳过原因")
    def test_1(self):
        print("assertEqual",TestMyCase.name)   #调用类方法直接使用类名.方法
    #不可以这么写： @unittest.skipIf(TestMyCase.result['m'],"休息一下")
    def test_2(self):
        if  TestMyCase.result['m'] ==0  #内部直接跳过---虽然显示测试，但是不对内容进行测试
        print("assertEqual",TestMyCase.result['m'])
if __name__ == '__main__':
    unittest.main()


