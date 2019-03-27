from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from index.models import Author


def index(request):
    return HttpResponse("这是index中的index/访问路径")

def login(request):
    return HttpResponse("这是index中的login")

def register(request):
    return HttpResponse("这是index中的register")

def addauthor(request):
    #使用Entry.objects.create()增加数据
    Author.objects.create(name='wy',age=20,email = '1234@qq.com')
    return HttpResponse("<script>alert('增加数据成功');</script>")

def queryauthor(request):
    authors = Author.objects.all()
    return render(request,'authorlist.html',locals())