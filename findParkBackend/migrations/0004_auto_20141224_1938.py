# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findParkBackend', '0003_auto_20141224_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspot',
            name='transportcode',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
