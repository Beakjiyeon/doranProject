# Generated by Django 2.1.1 on 2019-08-08 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_auto_20190808_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(default='작성자', max_length=200, null=True),
        ),
    ]