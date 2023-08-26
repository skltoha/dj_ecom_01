from django.contrib import admin
from . import models
# Register your models here.

class ProductList(admin.ModelAdmin):
    list_display = [field.name for field in models.Product._meta.fields]
    
admin.site.register(models.Product, ProductList)

class ProductImage(admin.ModelAdmin):
    list_display = [field.name for field in models.ProductImage._meta.fields]
    
admin.site.register(models.ProductImage, ProductImage)


class PromotionList(admin.ModelAdmin):
    list_display = [field.name for field in models.Promotion._meta.fields]
    
admin.site.register(models.Promotion, PromotionList)