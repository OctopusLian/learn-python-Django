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
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #template = loader.get_template('polls/index.html')
    #context = {
        #'latest_question_list': latest_question_list,
    #}
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello,world.You're at polls index.")
    # return HttpResponse(output)
    #return HttpResponse(template.render(context, request))

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)