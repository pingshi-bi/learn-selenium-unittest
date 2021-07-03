import unittest
from ddt import ddt,data,unpack,file_data
import time
import yaml

#将数据与代码分离出来，将数据从py文件中分离出来
#txt/xml/json/yaml/excel

@ddt #先表示使用ddt
class TestMyCase(unittest.TestCase):

    @file_data("phone_number.yaml")
    def test_1(self,phone):
        print("手机号测试：",phone)

    # 数据文件中的key和程序入口参数必须同名
    @file_data("login_data.yaml")  #  使用*使传入数据为每条一份
    #@unpack #解包
    def test_2(self,username,password=None):
        print(f"name:{username},pwd:{password}")

    # 数据文件中的key和程序入口参数必须同名
    @file_data("login_data.yaml")  # 使用*使传入数据为每条一份
    # @unpack #解包
    def test_2(self, **userdate):
        name = userdate.get("username")
        pwd = userdate.get("password")
        print("name:",userdate)
        print(name,pwd)

if __name__ == '__main__':
    unittest.main()


