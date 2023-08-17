from django.db import models

# Create your models here.
class menu(models.Model):
    name    = models.CharField(max_length=20, null=False)
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name