from django.contrib import admin
from . import models
# Register your models here.
class PromotionList(admin.ModelAdmin):
    list_display = [field.name for field in models.Promotion._meta.fields]
    
admin.site.register(models.Promotion, PromotionList)

# class CollectionList(admin.ModelAdmin):
#     list_display = [field.name for field in models.Collection._meta.fields]
    
# admin.site.register(models.Collection, CollectionList)

class ProductList(admin.ModelAdmin):
    list_display = [field.name for field in models.Product._meta.fields]
    
admin.site.register(models.Product, ProductList)