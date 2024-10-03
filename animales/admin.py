from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Animal)
admin.site.register(Protectora)
admin.site.register(Colaborador)