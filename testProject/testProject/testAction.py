# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年09月02日
"""
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import logging
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .captcha_image import *
from .models import OrderInfo
import datetime
import json
import os

logger = logging.getLogger()


def auth_code_port(request):
    """
      生成验证码的接口
      :param request:
      :return: 图片的对象
    """
    captcha_str, image_64 = Captcha_Get().get_captcha_image()
    # logger.debug(captcha_str)
    request.session['captcha_str'] = captcha_str
    # image = 'data:image/png;base64,'+image_64
    resp = HttpResponse(image_64, content_type='image/png')
    return resp


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        raise SystemError("method error: post")


def dologin(request):
    jsonData = {}
    try:
        if request.method == 'POST':
            username = request.POST["username"] if "username" in request.POST else None
            password = request.POST['pwd'] if "pwd" in request.POST else None
            if not username or not password:
                jsonData['code'] = 10
                raise ValueError("用户名和密码必输.")
            randomCode = request.POST['randomCode']
            # print(randomCode)
            # print(request.session['captcha_str'])
           # if randomCode != request.session['captcha_str']:
            #    raise RuntimeError("验证码错误")
            logger.debug(username)
            logger.debug(password)
            user_obj = auth.authenticate(username=username, password=password)
            print(user_obj)
            if user_obj:
                auth.login(request, user_obj)
                user_obj.last_login = timezone.now()
                user_obj.save()
            else:
                jsonData['code'] = 11
                raise RuntimeError("用户名或密码错误")
        else:
            raise TypeError("method type may be post.")

        jsonData['code'] = 0
    except Exception as e:
        logger.exception(e)
        if 'code' not in jsonData:
            jsonData['code'] = -1
        jsonData['msg'] = str(e)

    logger.info("response json: %s", jsonData)
    return JsonResponse(jsonData)


def logout(request):
    ppp = auth.logout(request)
    print(ppp)
    return redirect("/login/")


def addUser(request):
    jsonData = {}
    try:
        #User.objects.create_superuser(username='admin', password='123456', email='123456@qq.com')
        User.objects.create_superuser(username='sniper', password='111111', email='111111@qq.com')
        jsonData['code'] = 0
    except Exception as e:
        logger.exception(e)
        jsonData['code'] = -1
        jsonData['msg'] = str(e)

    logger.info("response json: %s", jsonData)
    return JsonResponse(jsonData)


@login_required(login_url="/login/")
def homepage(request):
    logger.info("载入主页面...")
    ctx = {'user': request.user}
    return render(request, 'main.html', ctx)


@login_required(login_url="/login/")
def orderAdd(request):
    return render(request, 'orderAdd.html')


@login_required(login_url="/login/")
def orderAddCommit(request):
    if request.method == "POST":
        jsonData = {}
        try:
            order_name = request.POST['order_name']
            order_dep = request.POST['order_dep']
            order_type = request.POST['order_type']
            order_date = request.POST['order_date']

            # 检查日期
            today = datetime.date.today().strftime('%Y-%m-%d')
            day7 = (datetime.date.today() + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
            if order_date < today or order_date > day7:
                raise Exception("日期不在允许范围内")

            order_sys = request.POST['order_sys']
            order_desc = request.POST['order_desc']
            params = {
                'name': order_name,
                'type': order_type,
                'dep': order_dep,
                'date': order_date,
                'system': order_sys,
                'desc': order_desc,
                'status': '0',
            }

            order = OrderInfo(**params)
            order.save()
        except Exception as e:
            logger.exception(e)
            if 'code' not in jsonData or not jsonData['code']:
                jsonData['code'] = -1
            jsonData['msg'] = str(e)
        else:
            jsonData['code'] = 0
            jsonData['order_id'] = order.id

        print(jsonData)
        return JsonResponse(jsonData)


@login_required(login_url="/login/")
def orderAddCommit1(request):
    if request.method == "POST":
        jsonData = {}
        try:
            order_name = request.POST['order_name']
            if 'order_dep' in request.POST and request.POST['order_dep']:
                order_dep = request.POST['order_dep']
            else:
                jsonData['code'] = 10
                raise ValueError("需求部门不能为空")

            if order_dep not in ['001', '002', '003', '004', '005', '006', '007']:
                raise ValueError("需求部门不存在")

            order_type = request.POST['order_type']
            order_date = request.POST['order_date']
            order_sys = request.POST['order_sys']
            order_desc = request.POST['order_desc']
            params = {
                'name': order_name,
                'type': order_type,
                'dep': order_dep,
                'date': order_date,
                'system': order_sys,
                'desc': order_desc,
                'status': '0',
            }

            order = OrderInfo(**params)
            order.save()
        except Exception as e:
            logger.exception(e)
            if 'code' not in jsonData:
                jsonData['code'] = -1
            jsonData['msg'] = str(e)
        else:
            jsonData['code'] = 0
            jsonData['order_id'] = order.id

        print(jsonData)
        return JsonResponse(jsonData)


@login_required(login_url="/login/")
def orderList(request):
    if "data" in request.GET and request.GET['data'] == 'json':
        page = int(request.GET['page'])
        limit = int(request.GET['limit'])
        queryFilter = {'status': 0}
        if 'order_name' in request.GET and request.GET['order_name']:
            queryFilter['name'] = request.GET['order_name']
        if 'order_type' in request.GET and request.GET['order_type']:
            queryFilter['type'] = request.GET['order_type']
        if 'order_dep' in request.GET and request.GET['order_dep']:
            queryFilter['dep'] = request.GET['order_dep']
        if 'order_date' in request.GET and request.GET['order_date']:
            queryFilter['date'] = request.GET['order_date']
        logger.debug(page)
        logger.debug(limit)
        count = OrderInfo.objects.filter(**queryFilter).count()
        begin = limit * (page - 1)
        end = begin + limit
        logger.debug(begin)
        logger.debug(end)
        studentObjList = OrderInfo.objects.filter(**queryFilter)[begin:end]
        dataList = [{'id': o.id, 'name': o.name, 'type': o.type, 'dep': o.dep,
                     'date': o.date, 'system': o.system,
                     'desc': o.desc, 'status': o.status} for o in studentObjList]
        jsonData = {'code': 0, 'msg': "", "count": count, "data": dataList}
        return JsonResponse(jsonData)
    else:
        return render(request, 'orderList.html')


@login_required(login_url="/login/")
def orderInfo(request):
    oid = request.GET['oid']
    order = OrderInfo.objects.get(id=oid)
    ctx = {"order": order}
    return render(request, 'orderInfo.html', ctx)


def orderQueryApi(request):
    if request.method == "POST":
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
        page = json_data.get('page')
        limit = json_data.get('limit')
        jsonData = {}
        queryFilter = {'status': 0}
        if 'order_name' in json_data and json_data['order_name']:
            queryFilter['name'] = json_data['order_name']
        if 'order_type' in json_data and json_data['order_type']:
            queryFilter['type'] = json_data['order_type']
        if 'order_dep' in json_data and json_data['order_dep']:
            queryFilter['dep'] = json_data['order_dep']
        if 'order_date' in json_data and json_data['order_date']:
            queryFilter['date'] = json_data['order_date']
        logger.debug(page)
        logger.debug(limit)
        print(queryFilter)
        count = OrderInfo.objects.filter(**queryFilter).count()
        begin = limit * (page - 1)
        end = begin + limit
        logger.debug(begin)
        logger.debug(end)
        studentObjList = OrderInfo.objects.filter(**queryFilter)[begin:end]
        dataList = [{'id': o.id, 'name': o.name, 'type': o.type, 'dep': o.dep,
                     'date': o.date, 'system': o.system,
                     'desc': o.desc, 'status': o.status} for o in studentObjList]
        jsonData = {'code': 0, 'msg': "查询成功", "count": count, "data": dataList}

        print(jsonData)
        return JsonResponse(jsonData)


def upload(request):
    file = request.FILES["baidu_logo"]
    print(f"文件信息: {file.name}, 大小{file.size}, 文件标识{file.field_name}")

    upload_path = "upload"
    if not os.path.exists(upload_path):
        os.mkdir(upload_path)
    with open(upload_path + "/" + file.name, "wb") as bf:
        bf.write(file.file.read())

    jsonData = {'code': 0, 'msg': "上传成功", "size": file.size, "name": file.name, "field_name": file.field_name}
    return JsonResponse(jsonData)
