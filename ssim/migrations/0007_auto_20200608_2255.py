# Generated by Django 2.1.7 on 2020-06-08 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssim', '0006_challenge_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(default='Mystery', max_length=50),
        ),
    ]
