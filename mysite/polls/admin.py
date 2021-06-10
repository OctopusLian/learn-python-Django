'''
Author: neozhang
Date: 2021-06-04 17:34:40
LastEditTime: 2021-06-10 17:52:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \learn-python-Django\mysite\polls\admin.py
'''
from django.contrib import admin

from .models import Question

# Register your models here.

admin.site.register(Question)  #向管理页面注册了问题 Question 类。Django 知道它应该被显示在索引页里
