from django.urls import path, re_path

from . import views


urlpatterns = {
    # path('hello/', views.index1, name='index1'),
    path('', views.index3, name='index3'),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index2, name= 'index2'),
    path('list/', views.userlist, name= 'userlist'),
}