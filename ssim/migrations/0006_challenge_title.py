# Generated by Django 2.1.7 on 2020-06-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssim', '0005_image_gps'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]