# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Conjunto(models.Model):
    conj_name = models.CharField(max_length = 250);
    field1 = models.CharField(max_length = 250);
    field2 = models.CharField(max_length = 250);
    field3 = models.CharField(max_length = 250);
    field4 = models.CharField(max_length = 250);

class Plano(models.Model):
    plan_name = models.CharField(max_length = 250);
    field1 = models.CharField(max_length = 250);
    field2 = models.CharField(max_length = 250);
    field3 = models.CharField(max_length = 250);
    field4 = models.CharField(max_length = 250);

class Material(models.Model):
    mate_name = models.CharField(max_length = 250);
    field1 = models.CharField(max_length = 250);
    field2 = models.CharField(max_length = 250);
    field3 = models.CharField(max_length = 250);
    field4 = models.CharField(max_length = 250);

class Montaje(models.Model):
    conj_name = models.CharField(max_length = 250);
    conjunto = models.ForeignKey(Conjunto,on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)
