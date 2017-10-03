# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ofertas', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField()),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_offer', to='ofertas.Offer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_product', to='productos.Product')),
            ],
        ),
    ]
