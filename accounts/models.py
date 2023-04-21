from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    def profile(instance, filename):
        return f'profiles/{instance.username}/{filename}'
    image = ProcessedImageField(blank = True,
                                upload_to = profile,
                                processors= [ResizeToFill(90, 90)],
                                format='JPEG',
                                options={'quality' : 60},
                                )