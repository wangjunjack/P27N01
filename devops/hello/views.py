from django.http import HttpResponse, request
from django.shortcuts import render
from django.core.paginator import Paginator
from hello.models import User
import logging
ForMat = "%(asctime)s %(message)s"
logging.basicConfig(format=ForMat, level=logging.INFO)

def userlist(request):
    """
    页面展示首页 index.html页
    :param request:
    :return:
    """
    users = User.objects.all()
    logging.info(users)
    return render(request, 'userlist.html', {'users': users})

def createdata(request,**kwargs):
    """
    GET 返回创建页面
    POST 创建新用户
    :param request:
    :return:
    """
    print(request.method)
    if request.method == "GET":
        return render(request,'create.html')
    else:
        u = User()
        u.username = request.POST['username']
        u.passwd = request.POST['passwd']
        u.sex = request.POST['sex']
        try:
            u.save()
            return HttpResponse("执行结果成功")
        except Exception as e:
            logging.info('创建失败',e)


def modifydata(request,**kwargs):
    """
    更新表单数据
    :param request:
    :return: 更新成功提交
    """

    if request.method == "GET":
        print(request)
        print(kwargs)
        id = kwargs.get("id")
        u = User.objects.get(id = id)
        username = u.username
        passwd = u.passwd
        sex = u.get_sex_display
        return render(request,"update.html",{"id":id,"username":username,"passwd":passwd,"sex":sex})
    username = request.POST['username']
    passwd = request.POST['passwd']
    sex = request.POST['sex']
    code = User.objects.filter(id = request.POST['id']).update(username = username, passwd = passwd, sex = sex)
    return HttpResponse("执行结果 {}".format(code))

def deletelist(request, **kwargs):
    """
    删除数据
    :param request: 数据体
    :param kwargs:  数据
    :return:
    """
    u = User.objects.filter(id = kwargs.get('userid')).delete()
    return HttpResponse('记录 id 为 {}, 已经删除成功'.format(u))
