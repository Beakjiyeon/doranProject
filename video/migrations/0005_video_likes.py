# Generated by Django 2.1.1 on 2019-08-08 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0004_upload_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
