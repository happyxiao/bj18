from django.http import HttpResponse


def index(request):
    '''首页'''
    return HttpResponse('index')
