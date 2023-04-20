from django.db import models
from django.conf import settings

# Create your models here.

class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_balances')
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_balances')
    select1_content = models.CharField(max_length=1000)
    select2_content = models.CharField(max_length=1000)
