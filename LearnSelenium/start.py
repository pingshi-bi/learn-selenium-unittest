
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = r"C:\Users\86180\AppData\Local\Google\Chrome\Application\chrome.exe"
driver_path = r"C:\SeleniumChrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("http://www.baidu.com ")


# 有id先用id
# 有name先用name
# 再有class_name使用class_name
#元素定位
#driver.find_element_by_id("kw").send_keys("Selenium")   #非动态id

#driver.find_element_by_name("wd").send_keys("Selenium_name")    #name

#driver.find_element_by_class_name("s_ipt").send_keys("Selenium_class")     #class_name
#链接
#driver.find_element_by_link_text("新闻").click()      #模糊查询

#CSS定位
#driver.find_element_by_css_selector("#kw").send_keys("Selenium")
#driver.find_element_by_css_selector('input[name = "wd"]').send_keys("selenium_css")

driver.find_element_by_css_selector(".s_ipt").send_keys("学习selenium")
driver.find_element_by_id("su").click()
#XPATH 定位选择使用xpth
driver.find_element_by_xpath()









