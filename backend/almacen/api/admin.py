from django.contrib import admin

# Register your models here.
from .models import Categoria,Ambiente

admin.site.register(Categoria)
admin.site.register(Ambiente)