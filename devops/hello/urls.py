from django.urls import path, re_path

from . import views


urlpatterns = {
    path('list/', views.userlist, name= 'userlist'),
    re_path('update/(?P<id>[0-9]{10})',views.modifydata, name='update'),
    re_path('delete/(?P<id>[0-9]{10})',views.deletelist, name='delete'),
    re_path('update/update/?', views.modifydata, name='modifydata'),
    re_path('create/?', views.createdata, name='createdata'),
}
