from selenium import webdriver
import  time, random
import datetime
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

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
def login():
        assertobject = driver.find_element_by_css_selector('body > div > div.layui-header > div')
        if assertobject and assertobject.text == '接口自动化测试':
                print('登录 成功')

        else:
                print('登录失败')
login()
total=0
pass_count=0
fail_count=0
def Gotopage(page_name):
        driver.find_element_by_link_text('需求管理').click()
        driver.find_element_by_link_text('需求申请').click()
        driver.switch_to.frame(driver.find_element_by_id('mainframe'))
        time.sleep(1)
def doFormInput(params):
        # 申请部门选择
        if 'dept' in params:
                driver.find_element_by_css_selector( '#addForm > div:nth-child(2) > div.layui-input-inline > div > div > input').click()
                # driver.find_element_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd:nth-child(2)').click()
                eles = driver.find_elements_by_css_selector('#addForm > div:nth-child(2) > div.layui-input-inline > div > dl > dd')
                for ele in eles:
                        if ele.text == params['dept']:
                                ele.click()
                                break
        # 日期选择
        if 'date' in params:
                driver.find_element_by_css_selector('#order_date').send_keys(params['date'])
                driver.find_element_by_css_selector('#addForm > div:nth-child(2)').click()
                # driver.find_element_by_css_selector('#layui-laydate1 > div.layui-laydate-main.laydate-main-list-0 > div.layui-laydate-content > table > tbody > tr:nth-child(4) > td.layui-this').click()
                # 需求名称
        if 'name' in params:
                driver.find_element_by_id('order_name').send_keys(params['name'])
        # 关联部门
        if 'nrefersys' in params:
                driver.find_element_by_id('order_sys').send_keys(params['refersys'])
        # 需求类型
        if 'type' in params:
                type_list = ['新增需求', '需求变更', '系统优化']
                driver.find_element_by_xpath('//*[@id="addForm"]/div[5]/div/div[%d]/i' %(type_list.index(params['type']) + 1)).click()
        # for ele in eles:
        #         if ele == params['type']:
        #                 ele.click()
        #                 break
        # driver.find_element_by_css_selector('#addForm > div:nth-child(6) > div > div:nth-child(6) > i').click()
        # 需求描述
        if 'decs' in params:
                driver.find_element_by_id('order_desc').send_keys(params['decs'])
        # 提交
        driver.find_element_by_id('submitBtn').click()
def assertSuccess():
        global total  # 测试用例数
        global pass_count  # 测试用例通过数
        global fail_count  # 测试用例未通过数
        time.sleep(2)
        total+=1
        rspmsg = ''
        try:
                element = WebDriverWait(driver, 10).until(
                        expected_conditions.presence_of_element_located((By.ID, 'layui-layer2'))
                )
                rspmsg = element.text
        except Exception as e:
                print(e)
        if rspmsg == '需求登记成功.':
                print('测试通过')
                pass_count += 1
        else:
                print('测试失败')
                #print(rspmsg)
                fail_count += 1
def assertFaillocal(input_msg):
        global total  # 测试用例数
        global pass_count  # 测试用例通过数
        global fail_count  # 测试用例未通过数
        time.sleep(2)
        total+=1
        rspmsg = ''
        try:
                element = WebDriverWait(driver, 10).until(
                        expected_conditions.presence_of_element_located((By.ID, 'layui-layer1'))
                )
                rspmsg = element.text
        except Exception as e:
                print(e)
        if rspmsg == input_msg:
                print('测试通过')
                pass_count += 1
        else:
                print('测试失败')
                #print(rspmsg)
                fail_count += 1


#------------打开菜单------------
Gotopage('需求申请')
#------------正例1------------
print('正例1：今天的日期', end = '...')
case_params = {
        "dept":"人力部门",
        "date":datetime.date.today().strftime('%Y-%m-%d'),
        "name":"测试需求名称",
        "refersys":"关联的应用系统",
        "decs":"需求描述的具体内容",
        "type":"需求变更",
}
#------------录入------------
doFormInput(case_params)
#------------断言------------
assertSuccess()
driver.refresh()
time.sleep(1)

#------------正例2------------
#------------打开菜单------------
Gotopage('需求申请')
print('正例2：第7天的日期', end = '...')
#------------打开菜单------------
case_params = {
        "dept":"人力部门",
        "date":(datetime.date.today()+datetime.timedelta(days=6)).strftime('%Y-%m-%d'),
        "name":"测试需求名称",
        "refersys":"关联的应用系统",
        "decs":"需求描述的具体内容",
        "type":"需求变更",
}
#------------录入------------
doFormInput(case_params)
#------------断言------------
assertSuccess()
driver.refresh()
time.sleep(1)

#------------正例3------------
#------------打开菜单------------
Gotopage('需求申请')
print('正例3：第n天的日期', end = '...')
#------------打开菜单------------
forday = random.randint(1,5)
case_params = {
        "dept":"人力部门",
        "date":(datetime.date.today()+datetime.timedelta(forday)).strftime('%Y-%m-%d'),
        "name":"测试需求名称",
        "refersys":"关联的应用系统",
        "decs":"需求描述的具体内容",
        "type":"需求变更",
}
#------------录入------------
doFormInput(case_params)
#------------断言------------
assertSuccess()
driver.refresh()
time.sleep(1)

#------------用例四-需求名称未输入------------
#------------打开菜单------------
Gotopage('需求申请')
print('用例四-反例...需求名称未输入', end = '...')
#------------打开菜单------------
forday = random.randint(1,5)
case_params = {
        "dept":"人力部门",
        "date":datetime.date.today().strftime('%Y-%m-%d'),
        #"name":"测试需求名称",
        "refersys":"关联的应用系统",
        "decs":"需求描述的具体内容",
        "type":"需求变更",
}
#------------录入------------
doFormInput(case_params)
#------------断言------------
assertFaillocal('需求名称必输')
driver.refresh()
time.sleep(1)
#------------用例五-日期未输入------------
#------------打开菜单------------
Gotopage('需求申请')
print('用例四-反例...日期未输入入', end = '...')
#------------打开菜单------------
forday = random.randint(1,5)
case_params = {
        "dept":"人力部门",
        "date":datetime.date.today().strftime('%Y-%m-%d'),
        #"name":"测试需求名称",
        "refersys":"关联的应用系统",
        "decs":"需求描述的具体内容",
        "type":"需求变更",
}
#------------录入------------
doFormInput(case_params)
#------------断言------------
assertFaillocal('需求名称必输')
driver.refresh()
time.sleep(1)

#刷新
driver.refresh()
print(f'执行了{total}个用例,通过了{pass_count}个,失败了{fail_count}个.')