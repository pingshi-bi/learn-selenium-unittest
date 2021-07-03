# -*- coding: utf-8 -*-
# @Time : 2021/6/26 6:09 
# @Author : pingshi-bi
# @File : testCase——apply.py
#1. 优化完成正例代码的优化
#2. 使用数据驱动
#3. 让入口参数支持变量
#4. 反例迁移
#5.测试现场还原
import unittest
from selenium import webdriver
import  time,random,re,pymysql
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from ddt import ddt,file_data
import datetime

#字符串操作转换变量

def str_Param(param):
    for key in param:
        if param.get(key).startswith("<") and param.get(key).endswith(">"):
            value = eval(param.get(key)[1:-1])
            param[key] = value
        print(param[key])

#正则表达式转换变量
def re_lParam(param):
    for key in param:
        expr = re.search(r"<(.*)>",param.get(key))
        if expr:
            value = eval(expr.group(1))
            param[key] = value
        print(param[key])

#获取最大序号
def queryMaxid(conn):
    cursor = conn.cursor()
    sql ="select max(id) from order_info"
    result = cursor.fetchone()

    cursor.close()
    conn.commit()
    return result[0]

def clearTestdata(conn,Max_id):
    cursor = conn.cursor()
    sql = f"delete from order_info where id>{Max_id}"
    result = cursor.fetchone()

    cursor.close()
    conn.commit()
    return result[0]
@ddt
class testCase_apply(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='testdb'
        )
        cls.max_order_id =  queryMaxid(cls.conn)
        #获取最大序号
        print("获取最大序号",cls.max_order_id)
        # -----------------先置条件--------------
        cls.driver_path = r"C:\SeleniumChrome\chromedriver.exe"
        cls.driver = webdriver.Chrome(executable_path=cls.driver_path)
        cls.driver.get("http://localhost:8001/login/ ")
        cls.driver.implicitly_wait(30)

        user, password, randcode = "admin", "123456", "1234"

        # 定位输入
        cls.driver.find_element_by_id('LAY-user-login-username').send_keys(user)
        cls.driver.find_element_by_id('LAY-user-login-password').send_keys(password)
        cls.driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
        cls.driver.find_element_by_id('loginButton').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        clearTestdata(cls.conn,cls.max_oder_id)
        cls.conn.close()
    def setUp(self):
        self.Gotopage('需求申请')
    def tearDown(self):
        self.driver.refresh()

    def Gotopage(self,page_name):

        self.driver.find_element_by_css_selector('body > div > div.layui-side.layui-bg-cyan > div > ul > li > a').click()
        self.driver.find_element_by_link_text(page_name).click()
        #self.driver.find_element_by_link_text('需求申请').click()
        self.driver.switch_to.frame(self.driver.find_element_by_id('mainframe'))
        time.sleep(1)

    def doFormInput(self,params):
        # -------------测试正例-----------
        # 申请部门选择
        self.driver.find_element_by_css_selector( '#addForm > div:nth-child(2) > div.layui-input-inline > div > div > input').click()
        # driver.find_element_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd:nth-child(2)').click()
        eles = self.driver.find_elements_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd')
        for ele in eles:
                if ele.text == params['dept']:
                        ele.click()
                        break
        # 日期选择
        self.driver.find_element_by_css_selector('#order_date').send_keys(params['date'])
        self.driver.find_element_by_css_selector('#addForm > div:nth-child(2)').click()
        # driver.find_element_by_css_selector('#layui-laydate1 > div.layui-laydate-main.laydate-main-list-0 > div.layui-laydate-content > table > tbody > tr:nth-child(4) > td.layui-this').click()
        # 需求名称

        self.driver.find_element_by_id('order_name').send_keys(params['name'])
        # 关联部门
        self.driver.find_element_by_id('order_sys').send_keys(params['refersys'])
        # 需求类型
        type_list = ['新增需求', '需求变更', '系统优化']
        self.driver.find_element_by_xpath('//*[@id="addForm"]/div[5]/div/div[%d]/i' %(type_list.index(params['type']) + 1)).click()
        # for ele in eles:
        #         if ele == params['type']:
        #                 ele.click()
        #                 break
        # driver.find_element_by_css_selector('#addForm > div:nth-child(6) > div > div:nth-child(6) > i').click()
        # 需求描述
        self.driver.find_element_by_id('order_desc').send_keys(params['decs'])
        # 提交
        self.driver.find_element_by_id('submitBtn').click()

    def assertSuccess(self):
        time.sleep(0.5)
        rspmsg = ''
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, 'layui-layer2'))
            )
            rspmsg = element.text
        except Exception as e:
            print('......>',e)
        self.assertEqual(rspmsg,'需求登记成功.')
        time.sleep(1)

    def assertFaillocal(self,input_msg):

        time.sleep(2)
        rspmsg = ''
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, 'layui-layer1'))
            )
            rspmsg = element.text
        except Exception as e:
            print(e)
        self.assertEqual(rspmsg,input_msg)

    # @file_data('./testDate/testdata_apply_nomal.yaml')
    # def test_1_nomal(self,**case_params):
    #     # ------------正例1------------
    #
    #     #print('正例1：今天的日期',)
    #     # ------------录入------------
    #     #str_Param(case_params)#字符串操作转换变量
    #     re_lParam(case_params)#正则表达式转换变量
    #     self.doFormInput(case_params)
    #     # ------------断言------------
    #     self.assertSuccess()
    #     time.sleep(1)


    @file_data('./testDate/testdata_apply_wrong.yaml')
    def test_2_error(self, **case_params):
        # ------------反例1------------

        # print('正例1：今天的日期',)
        # ------------录入------------
        # str_Param(case_params)#字符串操作转换变量
        re_lParam(case_params)  # 正则表达式转换变量
        self.doFormInput(case_params)
        # ------------断言------------
        self.assertFaillocal('需求名称必输')
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()