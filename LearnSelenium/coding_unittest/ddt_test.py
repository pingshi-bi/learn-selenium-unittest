import unittest
from ddt import ddt,data,unpack,file_data
import time

#将数据与代码分离出来，将数据从py文件中分离出来
#txt/xml/json/yaml/excel
#从文件获取电话号码
def test_phone():
    li = []
    with open("phone.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            li.append(line.strip('\n'))
    return li

#从文件获取账户及密码。
def test_login():
    li = []
    with open("user.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            li.append(line.strip('\n').split(','))
    return li

@ddt #先表示使用ddt
class TestMyCase(unittest.TestCase):

    @data(*test_phone())  #  使用*使传入数据为每条一份
    #@unpack
    def test_1(self,phone):
        print("assertEqual",phone)

    @data(*test_login())#需要两个参数时使用列表的方式传入参数
    @unpack #解包
    def test_2(self,user,password=None):
        print(user,password)

if __name__ == '__main__':
    unittest.main()


