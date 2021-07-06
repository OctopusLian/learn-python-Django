'''
Author: your name
Date: 2021-06-16 13:41:41
LastEditTime: 2021-07-06 11:45:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \learn-python-Django\mysite\polls\urls.py
'''
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/   
    path('',views.IndexView.as_view(),name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),
]