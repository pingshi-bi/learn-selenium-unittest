import unittest
from selenium import webdriver
import time
from ddt import ddt,file_data

testcase_nomal_path = 'testDate/testcase_logindata_nomal.yaml'
testcase_wrong_path = 'testDate/testcase_logindata_wrong.yaml'
testcase_without_path = 'testDate/testcase_logindata_withoutl.yaml'
# 优化使用unittest对登录界面的测试
#登录测试
@ddt()
class loginTestcase(unittest.TestCase):
    def do_input(self,usr = None,password = None,randcode = None):
        if usr:
            self.driver.find_element_by_id('LAY-user-login-username').send_keys(usr)
        if password:
            self.driver.find_element_by_id('LAY-user-login-password').send_keys(password)
        if randcode:
            self.driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
        self.driver.find_element_by_id('loginButton').click()

    def setUp(self):
        self.driver_path = r"C:\SeleniumChrome\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get("http://localhost:8001/login/ ")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
    #正例1.正确输入信息
    @file_data(testcase_nomal_path)
    def test_1_nomal(self,username,password,randcode = 111):
        '''用户登录正例'''
        print(f"username:{username},password:{password}")
        self.do_input(usr = username,password = password,randcode = randcode)
        time.sleep(1)
        assertobject = self.driver.find_element_by_css_selector('body > div > div.layui-header > div')
        self.assertEqual(assertobject.text,'接口自动化测试')

    @file_data(testcase_wrong_path)
    def test_2_wrong_user(self,username,password):
        self.do_input(usr = username,password = password,randcode = 1111)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_css_selector('#layui-layer2 > div.layui-layer-content.layui-layer-padding').text
        self.assertEqual(rspmsg,'用户名或密码错误')

    @file_data(testcase_without_path)
    def test_3_without_user(self,username,password,randcode = 111):
        print(f"username:{username},password:{password}")
        self.do_input(password=password)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_id('layui-layer1').text
        self.assertEqual(rspmsg, '请输入用户名和密码')

    # def test_6_without_randcode(self):
    #     user , password = "admin", "1234"
    #     self.do_input(usr=user, password=password)
    #     time.sleep(1)
    #     rspmsg = self.driver.find_element_by_id('layui-layer1').text
    #     self.assertEqual(rspmsg, '请输入验证码')
            
if __name__ == '__main__':
    unittest.main()


