from django.shortcuts import render
from django.http import HttpResponse, QueryDict, request

from hello.models import User

def userlist(request):
    users = User.objects.all()
    print(users)
    return render(request, 'userlist.html', {'users': users})
def index(request):
    return render(request, 'hello.html',)

def index1(request):
    # 设置默认值的⽅式获取数据更更优雅
    year = request.GET.get("year","2020")
    # 直接获取数据，没有传会报错，不建议
    month = request.GET.get("month", "03")
    return HttpResponse("year is {},month is %{}".format(year,month))

def index2(request, year, month):
    return HttpResponse("year is %s,month is %s" % (year,month))
def index3(request):
    print(request.scheme) #获取访问协议
    print(request.method) #获取访问方式 GET or POST
    print(request.path) #获取访问路径url
    data = request.GET
    year = data.get('year',"2019")
    month = data.get('month', "03")
    if request.method == "POST":
        year = data.get('year', "2020")
        month = data.get("month", "03")
    return HttpResponse("year is %s,month is %s" % (year,month))
#
# def index2(request, year=2020, month=3):
#     return HttpResponse("year is %s,month is %s" % (year,month))

