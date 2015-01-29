# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=18, decimal_places=8)),
                ('longitude', models.DecimalField(max_digits=18, decimal_places=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Driving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appuserfield', models.ForeignKey(to='findParkBackend.appuser')),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parkingarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='parkingspot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=255)),
                ('laststatechange', models.DateTimeField(null=True, blank=True)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('transportcode', models.CharField(max_length=255, blank=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified_datetime', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('creation_user', models.CharField(max_length=255, null=True, blank=True)),
                ('last_modified_user', models.CharField(max_length=255, null=True, blank=True)),
                ('area', models.ForeignKey(default=None, blank=True, to='findParkBackend.parkingarea', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='transportclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='parking',
            name='parkingspotfield',
            field=models.ForeignKey(to='findParkBackend.parkingspot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='driving',
            name='transportclassfield',
            field=models.ForeignKey(to='findParkBackend.transportclass'),
            preserve_default=True,
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
