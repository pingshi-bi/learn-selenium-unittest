# learn-selenium-unittest
内容包括测试网页的环境搭建，对网页使用selenium进行测试，使用unittest对网页进行测试并导出报告等

## 第一部分
1 拿到压缩包并解压，右键文件夹，用pycharm将项目打开

2 file -> settings -> python interfaces 配置python运行环境 ，注意要关闭pycharm重新打开testProject

3 创建数据库，前提是要安装好mysql5.7 创建一个新的数据库，并记录名字 demodb
4 将配置写入testproject/settings

5 启动项目!!!!!!
python manage.py runserver 0.0.0.0:8001
如果报了版本过低的错误，直接注释掉即可

启动后，如果有系统检查的警告，我们执行如下命令，创建系统所需要的表
python manage.py migrate

再次启动项目 没有报警告

  打开浏览器 输入网址 http://localhost:8001/login/ 能够看到登陆页面，并且验证码能显示，就对了

6 给系统添加一个默认的用户 名字 admin 密码 123456
http://localhost:8001/addUser/

7 使用 admin 123456 登陆系统，能够正常登陆即可

8 创建order_info表 在mysql客户端运行order_info.sql

9 进入需求申请的交易，完成一笔需求的登记，并能够在需求查询交易中看到我们增加的内容就可以了

大功告成！

第二部分：



