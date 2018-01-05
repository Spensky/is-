# Generated by Django 2.0 on 2018-01-05 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20180105_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='acount',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.UserProfile'),
        ),
    ]
