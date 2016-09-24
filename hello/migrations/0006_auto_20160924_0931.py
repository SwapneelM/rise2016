# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 09:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0005_auto_20160923_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='coder',
            name='user',
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.RemoveField(
            model_name='helper',
            name='user',
        ),
        migrations.DeleteModel(
            name='Coder',
        ),
        migrations.DeleteModel(
            name='Helper',
        ),
    ]
