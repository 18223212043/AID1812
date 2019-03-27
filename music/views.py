from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def show(request):
    return HttpResponse('这是music中的show')

def index(request):
    return HttpResponse('这是music中的index')

def template(request):
    # #通过loader响应模板
    # t = loader.get_template('template.html')
    # html = t.render()
    # return HttpResponse(html)
    uname = 'wy'
    uage = 18
    user_list = ['wy','kk']
    dic = {'uname':'qq'}

    return render(request,'template.html',locals())