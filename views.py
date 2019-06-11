from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    '''首页'''
    return HttpResponse('index')


def login(request):
    '''重定向'''
    return redirect('/index')
