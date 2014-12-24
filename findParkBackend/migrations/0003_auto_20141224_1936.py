# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findParkBackend', '0002_auto_20141221_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='latitude',
            field=models.DecimalField(max_digits=18, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='longitude',
            field=models.DecimalField(max_digits=18, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkingspothistory',
            name='latitude',
            field=models.DecimalField(max_digits=18, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkingspothistory',
            name='longitude',
            field=models.DecimalField(max_digits=18, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parkingspothistory',
            name='transportcode',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
