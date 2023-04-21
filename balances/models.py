from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone


# Create your models here.

class Balance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_balances')
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
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    def time_since_created(self):
        time_difference = timezone.now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60
        if days >= 1:
            return '{}일'.format(days)
        elif hours >= 1:
            return '{}시간'.format(hours)
        elif minutes >= 1:
            return " {}분".format(minutes)
        else:
            return '방금 '



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.ForeignKey(Balance, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def time_since_created(self):
        time_difference = timezone.now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60
        if days >= 1:
            return '{}일'.format(days)
        elif hours >= 1:
            return '{}시간'.format(hours)
        elif minutes >= 1:
            return " {}분".format(minutes)
        else:
            return '방금 '