from django.urls import path, re_path

# from . import views
from hello.views import userlist

urlpatterns = {
    # path('hello/', views.index, name='index'),
    # path('', views.index, name='index'),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name= 'index'),
    path('list/', userlist, name= 'userlist'),
}