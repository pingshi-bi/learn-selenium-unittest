# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2021年01月28日
"""
import datetime
if __name__ == '__main__':
    today = datetime.date.today().strftime('%Y-%m-%d')
    day7 = (datetime.date.today() + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
    day = "2021-01-01"
    print(day < today)