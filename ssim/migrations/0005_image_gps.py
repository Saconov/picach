# Generated by Django 2.1.7 on 2020-06-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssim', '0004_auto_20200608_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='gps',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
