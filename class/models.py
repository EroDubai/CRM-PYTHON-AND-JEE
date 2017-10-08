# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Conjunto(models.Model):
    conjunto_name = models.CharField(max_length = 250)
    field1 = models.CharField(max_length = 250)
    field2 = models.CharField(max_length = 250)

    def __str__(self):
        return self.conjunto_name

class Plano(models.Model):
    plano_name = models.CharField(max_length = 250)
    field1 = models.CharField(max_length = 250)
    field2 = models.CharField(max_length = 250)

    def __str__(self):
        return self.plano_name

class Material(models.Model):
    material_name = models.CharField(max_length = 250)
    field1 = models.CharField(max_length = 250)
    field2 = models.CharField(max_length = 250)

    def __str__(self):
        return self.material_name

class Montaje(models.Model):
    motaje_name = models.CharField(max_length = 250);
    conjunto = models.ForeignKey(Conjunto,on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano,on_delete=models.CASCADE)
    material = models.ForeignKey(Material,on_delete=models.CASCADE)

    def __str__(self):
        return self.motaje_name
