# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Conjunto,Plano,Material,Montaje

admin.site.register(Conjunto)
admin.site.register(Plano)
admin.site.register(Material)
admin.site.register(Montaje)
