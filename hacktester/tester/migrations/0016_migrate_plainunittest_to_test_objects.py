# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:02
from __future__ import unicode_literals

import uuid

from django.db import migrations, transaction
from django.core.files.base import ContentFile


class Migration(migrations.Migration):

    def migrate_plainunittest_to_test_objects(apps, schema_editor):
        PlainUnittest = apps.get_model('tester', 'PlainUnittest')
        Test = apps.get_model('tester', 'Test')

        with transaction.atomic():
            for plain_test in PlainUnittest.objects.all():
                test_file = ContentFile(content=plain_test.tests, name=str(uuid.uuid4()))

                test = Test()
                test.file = test_file
                test.save()

    dependencies = [
        ('tester', '0015_auto_20170327_0944'),
    ]

    operations = [
        migrations.RunPython(migrate_plainunittest_to_test_objects)
    ]
