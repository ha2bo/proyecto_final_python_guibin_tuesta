from django.contrib import admin
from .models import Sede, usuarios_contactados, usuarios_gimnasio

# Register your models here.

admin.site.register(Sede)
admin.site.register(usuarios_contactados)
admin.site.register(usuarios_gimnasio)