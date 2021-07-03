# -*- coding:utf-8 -*-
"""
作者：zhangxl
日期：2020年08月18日
"""

from captcha.image import ImageCaptcha
import random


class Captcha_Get():
    def __init__(self,
                 CHAR_SET=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                 CAPTCHA_LEN=4):
        self.CHAR_SET = CHAR_SET
        self.CAPTCHA_LEN = CAPTCHA_LEN

    def get_captcha(self):
        captcha_list = []
        for i in range(self.CAPTCHA_LEN):
            random_choice = random.choice(self.CHAR_SET)
            captcha_list.append(random_choice)
        return captcha_list

    def get_captcha_image(self):
        image = ImageCaptcha()
        captcha_list = self.get_captcha()  # 返回一个列表
        captcha_str = ''.join(captcha_list)  # 将列表的所有内容整合成一个字符串
        captcha_image = image.generate(captcha_str)
        # captcha_image返回<_io.BytesIO object at 0x000001C8758C8728>，它是一个<class '_io.BytesIO'>
        return captcha_str, captcha_image  # 因为要和django登陆相结合所以验证码的内容也要返回
