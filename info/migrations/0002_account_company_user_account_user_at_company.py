# Generated by Django 2.0 on 2018-01-04 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('balance', models.IntegerField()),
                ('income', models.IntegerField()),
                ('expenses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Adress')),
            ],
        ),
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.User')),
            ],
        ),
        migrations.CreateModel(
            name='user_at_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.User')),
            ],
        ),
    ]
