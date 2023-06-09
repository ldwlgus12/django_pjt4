# Generated by Django 3.2.18 on 2023-04-20 04:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('balances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='image_1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='image/1/'),
        ),
        migrations.AddField(
            model_name='balance',
            name='image_2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='image/2/'),
        ),
    ]
