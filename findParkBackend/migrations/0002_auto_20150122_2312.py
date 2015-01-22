# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findParkBackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appuserfield', models.ForeignKey(to='findParkBackend.appuser')),
                ('transportclassfield', models.ForeignKey(to='findParkBackend.transportclass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appuserfield', models.ForeignKey(to='findParkBackend.appuser')),
                ('parkingspotfield', models.ForeignKey(to='findParkBackend.parkingspot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appuser',
            name='parkingspots',
            field=models.ManyToManyField(to='findParkBackend.parkingspot', through='findParkBackend.Parking', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appuser',
            name='transportclasses',
            field=models.ManyToManyField(to='findParkBackend.transportclass', through='findParkBackend.Driving', blank=True),
            preserve_default=True,
        ),
    ]
