import unittest
from selenium import webdriver
import time

class TestMyCase(unittest.TestCase):

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
        self.driver.close()
    #正例1.正确输入信息
    def test_1_nomal(self,username,password,randcode = None):

        self.do_input(usr = user,password = password,randcode = randcode)
        time.sleep(1)
        assertobject = self.driver.find_element_by_css_selector('body > div > div.layui-header > div')
        self.assertEqual(assertobject.text,'接口自动化测试')

    def test_2_wrong_user(self):
        user, password, randcode = "admin1","123456","1234"
        self.do_input(usr = user,password = password,randcode = randcode)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_css_selector('#layui-layer2 > div.layui-layer-content.layui-layer-padding').text
        self.assertEqual(rspmsg,'用户名或密码错误')

    def test_3_wrong_password(self):
        user, password, randcode = "admin","1234561","1234"
        self.do_input(usr = user,password = password,randcode = randcode)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_css_selector('#layui-layer2 > div.layui-layer-content.layui-layer-padding').text
        self.assertEqual(rspmsg,'用户名或密码错误')

    def test_4_without_user(self):
        password, randcode = "1234561", "1234"
        self.do_input(password=password, randcode=randcode)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_id('layui-layer1').text
        self.assertEqual(rspmsg, '请输入用户名和密码')

    def test_5_without_password(self):
        user , randcode = "admin", "1234"
        self.do_input(usr=user, randcode=randcode)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_id('layui-layer1').text
        self.assertEqual(rspmsg, '请输入用户名和密码')
    def test_6_without_randcode(self):
        user , password = "admin", "1234"
        self.do_input(usr=user, password=password)
        time.sleep(1)
        rspmsg = self.driver.find_element_by_id('layui-layer1').text
        self.assertEqual(rspmsg, '请输入验证码')
            
if __name__ == '__main__':
    unittest.main()


