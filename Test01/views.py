from django.http import HttpResponse


#在Django中的视图处理函数中必须有一个参数，名称叫request
def show(request):
    return HttpResponse("我的第一个Django程序")

def show03(request,year,month,day):
    date = "%s-%s-%s"%(year,month,day)
    return HttpResponse(date)