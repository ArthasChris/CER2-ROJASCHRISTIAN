from django.contrib import admin
from .models import Entidad,Comunicado
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import Permission
admin.site.register(Permission)
admin.site.register(Entidad)
admin.site.register(Comunicado)
