# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-20 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_comment_project_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_posted']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.AddField(
            model_name='project',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
