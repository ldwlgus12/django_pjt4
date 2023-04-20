from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill



# Create your models here.

class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_balances')
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_balances')
    select1_content = models.CharField(max_length=1000)
    select2_content = models.CharField(max_length=1000)
    image_1= ProcessedImageField(blank = True,
                                upload_to = 'image/1/',
                                processors= [ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality' : 90},
                                )
    image_2= ProcessedImageField(blank = True,
                                upload_to = 'image/2/',
                                processors= [ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality' : 90},
                                )



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    content = models.TextField()