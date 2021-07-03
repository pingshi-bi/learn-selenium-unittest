from selenium import webdriver
import  time


#---------------断言——--------------------
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
time.sleep(1)
assertobject = driver.find_element_by_css_selector('body > div > div.layui-header > div')
if assertobject and assertobject.text = '接口自动化测试':
        print('测试通过')
else:
        print('测试失败')
        




