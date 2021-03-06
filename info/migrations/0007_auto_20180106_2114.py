# Generated by Django 2.0 on 2018-01-06 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20180105_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
