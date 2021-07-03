# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年09月04日
"""
from django.db import models


class OrderInfo(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=11)
    dep = models.CharField(max_length=255)
    date = models.DateField()
    system = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'order_info'
