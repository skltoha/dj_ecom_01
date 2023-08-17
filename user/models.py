from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    isActive = models.BooleanField(null=False, default=False)
    isVerified = models.BooleanField(null=False, default=False)
    verified_code = models.CharField(max_length=10, null=False, blank=False)
    expired = models.DateField(null=True, blank=True)

    def set_password(self, password):
        self.password = make_password(password)
        self.save()

    def check_password(self, password):
        return check_password(password, self.password)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})
