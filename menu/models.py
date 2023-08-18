from django.db import models
from django.core.cache import cache
from django.core.exceptions import ValidationError

# Create your models here.
class menu(models.Model):
    name    = models.CharField(max_length=20, null=False)
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    # url = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if not self.parent_menu and menu.objects.filter(parent_menu=None).count() >= 15:
            raise ValidationError("You cannot have more than 15 entries without a parent menu.")
    
    
    @classmethod
    def get_menus(cls):
        # Try to get the menus from the cache
        cached_menus = cache.get('cached_menus')
        
        if cached_menus is None:
            # Cache miss, fetch menus from the database and store in cache
            menus = list(cls.objects.all())
            cache.set('cached_menus', menus)
            return menus
        else:
            return cached_menus