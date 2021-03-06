# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('microfeed', '0002_eventpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPostTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='eventpost',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='eventposttime',
            name='event_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microfeed.EventPost'),
        ),
    ]
