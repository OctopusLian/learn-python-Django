'''
Author: your name
Date: 2021-06-04 17:34:40
LastEditTime: 2021-06-04 17:37:19
LastEditors: your name
Description: In User Settings Edit
FilePath: \learn-python-Django\mysite\polls\views.py
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello,world.You're at polls index.")