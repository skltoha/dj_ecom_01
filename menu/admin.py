from django.contrib import admin
from . import models

# Register your models here.
class MenuList(admin.ModelAdmin):
    list_display = [field.name for field in models.menu._meta.fields]
    
admin.site.register(models.menu, MenuList)