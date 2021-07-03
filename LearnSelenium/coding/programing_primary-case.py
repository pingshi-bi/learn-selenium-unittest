from selenium import webdriver
import  time

from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
total = 0               #测试用例数
pass_count = 0          #测试用例通过数
fail_count = 0          #测试用例未通过数

#模拟登录：
#-----------------先置条件--------------
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin","123456","1234"

#定位输入
driver.find_element_by_id('LAY-user-login-username').send_keys(user)
driver.find_element_by_id('LAY-user-login-password').send_keys(password)
driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

#增加断言
#total+= 1
time.sleep(1)
assertobject = driver.find_element_by_css_selector('body > div > div.layui-header > div')
if assertobject and assertobject.text == '接口自动化测试':
        print('登录 成功')
        #pass_count+=1
else:
        print('登录失败')
        #fail_count+=1
#------------打开菜单------------
driver.find_element_by_link_text('需求管理').click()
driver.find_element_by_link_text('需求申请').click()
driver.switch_to.frame(driver.find_element_by_id('mainframe'))
time.sleep(1)
#-------------测试正例-----------
driver.find_element_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > div > input').click()
driver.find_element_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd:nth-child(2)').click()
driver.find_element_by_css_selector('#order_date').click()
driver.find_element_by_css_selector('#layui-laydate1 > div.layui-laydate-main.laydate-main-list-0 > div.layui-laydate-content > table > tbody > tr:nth-child(4) > td.layui-this').click()
driver.find_element_by_id('order_name').send_keys("正例需求名称1")
driver.find_element_by_id('order_sys').send_keys('正例关联部门1')
driver.find_element_by_css_selector('#addForm > div:nth-child(6) > div > div:nth-child(4) > i').click()
driver.find_element_by_id('order_desc').send_keys("这是正例描述的第一次演示")
driver.find_element_by_id('submitBtn').click()

#断言
#第一种：
#time.sleep(1)
#assertobject = driver.find_element_by_id('layui-layer2').text
# if assertobject and assertobject.text == '需求登记成功.':
#         print('测试通过')
#         pass_count+=1
# else:
#         print('测试失败')
#         fail_count+=1
#第二种
rspmsg = ''
try:
        element = WebDriverWait(driver,10).until(
                expected_conditions.presence_of_element_located((By.ID,'layui-layer2'))
        )
        rspmsg = element.text
except Exception as e :
        print(e)
if rspmsg == '需求登记成功.':
        print('测试通过')
        pass_count+=1
else:
        print('测试失败')
        print(rspmsg)
        fail_count+=1


print(f'执行了{total},通过了{pass_count},失败了{fail_count}.')