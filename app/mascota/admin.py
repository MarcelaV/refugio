# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from app.mascota.models import Mascota, Vacuna

admin.site.register(Vacuna)
admin.site.register(Mascota)
