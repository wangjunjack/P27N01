from django.shortcuts import render
from django.http import HttpResponse, QueryDict, request

from .models import User


def userlist(request):

    return render(request, 'userlist.html', {'users': users})