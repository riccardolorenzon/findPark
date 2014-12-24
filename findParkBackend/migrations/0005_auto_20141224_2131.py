# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findParkBackend', '0004_auto_20141224_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingspot',
            old_name='state',
            new_name='status',
        ),
    ]
