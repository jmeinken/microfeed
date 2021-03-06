# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20161022_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagelink',
            options={'ordering': ['order', 'id'], 'verbose_name': 'Page Link', 'verbose_name_plural': 'Page Links'},
        ),
        migrations.AlterField(
            model_name='page',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='page',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.CharField(choices=[('restaurant', 'restaurant'), ('local_destination', 'local_destination'), ('regional_destination', 'regional_destination'), ('housing', 'housing'), ('shopping', 'shopping'), ('medical', 'medical'), ('transportation', 'transportation'), ('education', 'education')], default='restaurant', max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='page',
            name='teaser',
            field=models.TextField(blank=True, null=True, verbose_name='teaser'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='url',
            field=models.CharField(max_length=500, verbose_name='url'),
        ),
    ]
