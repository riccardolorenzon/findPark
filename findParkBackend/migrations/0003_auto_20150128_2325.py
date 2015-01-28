# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('findParkBackend', '0002_auto_20150122_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspot',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 23, 25, 18, 256523), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='creation_user',
            field=models.ForeignKey(related_name='creations_user', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='last_modified_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 28, 23, 25, 18, 256601), auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parkingspot',
            name='last_modified_user',
            field=models.ForeignKey(related_name='last_modified_user', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
