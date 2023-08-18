from django.db import models
from menu.models import menu
from django.utils.text import slugify


# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


# class Collection(models.Model):
#     title = models.CharField(max_length=255)
#     feature_product = models.ForeignKey(
#         'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True,)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotion)
    as_menu = models.ForeignKey(menu, on_delete=models.SET_NULL, null=True)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title