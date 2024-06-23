from django.contrib import admin
from .models import Sede, usuarios_contactados

# Register your models here.

admin.site.register(Sede)
admin.site.register(usuarios_contactados)