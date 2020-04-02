from django.urls import path, re_path

from . import views


urlpatterns = {
    # path('hello/', views.index1, name='index1'),
    path('', views.index3, name='index3'),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index2, name= 'index2'),
    path('list/', views.userlist, name= 'userlist'),
    re_path('update/(?P<id>[0-9])',views.modifydata, name='update'),
    re_path('delete/(?P<id>[0-9])',views.deletelist, name='delete'),
    re_path('update/update/?', views.modifydata, name='modifydata'),
    re_path('create/?', views.createdata, name='createdata'),
}
