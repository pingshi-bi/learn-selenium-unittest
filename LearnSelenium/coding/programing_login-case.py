from selenium import webdriver
import  time


total = 0
pass_count = 0
fail_count = 0
#-----------------用例1：正常用例--------------
print('用例1：正例')
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
total+= 1
time.sleep(1)
assertobject = driver.find_element_by_css_selector('body > div > div.layui-header > div')
if assertobject and assertobject.text == '接口自动化测试':
        print('测试通过')
        pass_count+=1
else:
        print('测试失败')
        fail_count+=1
driver.close()

#-----------------用例2：错误的用户名 - -------------
total+= 1
print('用例2：错误的用户名')
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin1", "123456", "1234"

# 定位输入
driver.find_element_by_id('LAY-user-login-username').send_keys(user)
driver.find_element_by_id('LAY-user-login-password').send_keys(password)
driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

# 增加断言
time.sleep(1)

rspmsg = driver.find_element_by_css_selector('#layui-layer2 > div.layui-layer-content.layui-layer-padding').text
if rspmsg == '用户名或密码错误':
        print('测试通过')
        pass_count += 1
else:
        print('测试失败')
        fail_count+=1
        print(rspmsg)
driver.close()
#print('元素定位错误')

#-----------------用例3：错误的密码 - -------------
total+= 1
print('用例2：错误的密码')
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin", "1234567", "1234"

# 定位输入
driver.find_element_by_id('LAY-user-login-username').send_keys(user)
driver.find_element_by_id('LAY-user-login-password').send_keys(password)
driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

# 增加断言
time.sleep(1)

rspmsg = driver.find_element_by_css_selector('#layui-layer2 > div.layui-layer-content.layui-layer-padding').text
if rspmsg == '用户名或密码错误':
        print('测试通过')
        pass_count += 1
else:
        print('测试失败')
        print(rspmsg)
        fail_count+=1
driver.close()

#-----------------用例4：用户名未输入 - -------------
total+= 1
print('用例4：用户名未输入')
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin", "1234567", "1234"

# 定位输入
#driver.find_element_by_id('LAY-user-login-username').send_keys(user)
driver.find_element_by_id('LAY-user-login-password').send_keys(password)
driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

# 增加断言
time.sleep(1)

rspmsg = driver.find_element_by_id('layui-layer1').text
if rspmsg == '请输入用户名和密码':
        print('测试通过')
        pass_count += 1
else:
        print('测试失败')
        print(rspmsg)
        fail_count+=1
driver.close()

#-----------------用例5：密码未输入 - -------------
total+= 1
print('用例5：密码未输入')
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin", "123456", "1234"

# 定位输入
driver.find_element_by_id('LAY-user-login-username').send_keys(user)
#driver.find_element_by_id('LAY-user-login-password').send_keys(password)
driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

# 增加断言
time.sleep(1)

rspmsg = driver.find_element_by_id('layui-layer1').text
if rspmsg == '请输入用户名和密码':
        print('测试通过')
        pass_count += 1
else:
        print('测试失败')
        print(rspmsg)
        fail_count+=1
driver.close()

#-----------------用例6：验证码未输入 - -------------
total+= 1
print('用例6：验证码未输入')
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://localhost:8001/login/ ")
driver.implicitly_wait(30)

user, password, randcode = "admin", "123456", "1234"

# 定位输入
driver.find_element_by_id('LAY-user-login-username').send_keys(user)
driver.find_element_by_id('LAY-user-login-password').send_keys(password)
#driver.find_element_by_id('LAY-user-login-vercode').send_keys(randcode)
driver.find_element_by_id('loginButton').click()

# 增加断言
time.sleep(1)

rspmsg = driver.find_element_by_id('layui-layer1').text
if rspmsg == '请输入验证码':
        print('测试通过')
        pass_count += 1
else:
        print('测试失败')
        print(rspmsg)
        fail_count+=1
driver.close()






print(f'执行了{total},通过了{pass_count},失败了{fail_count}.')