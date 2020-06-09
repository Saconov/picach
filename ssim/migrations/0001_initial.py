# Generated by Django 2.1.7 on 2020-06-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isStep', models.BooleanField()),
                ('isHint', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('coordinates', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Grouped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.Group')),
            ],
        ),
        migrations.CreateModel(
            name='marked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Solved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='solved',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.User'),
        ),
        migrations.AddField(
            model_name='marked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.User'),
        ),
        migrations.AddField(
            model_name='grouped',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssim.User'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='initiator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ssim.User'),
        ),
        migrations.AddField(
            model_name='cache',
            name='next_challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='ssim.Challenge'),
        ),
        migrations.AddField(
            model_name='cache',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin', to='ssim.Challenge'),
        ),
    ]
