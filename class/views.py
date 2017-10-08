# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello world</h1>")

def detail(request,montaje_id):
    return HttpResponse("<h2>details of the montaje id:" + str(montaje_id) + "</h2>");
