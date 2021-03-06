# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0012_auto_20161028_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivetest',
            name='archive_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tester.ArchiveType'),
        ),
        migrations.AlterField(
            model_name='runresult',
            name='status',
            field=model_utils.fields.StatusField(default='ok', max_length=100, no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='status',
            field=model_utils.fields.StatusField(db_index=True, default='pending', max_length=100, no_check_for_status=True),
        ),
    ]
