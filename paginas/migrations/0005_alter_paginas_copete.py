# Generated by Django 4.0.4 on 2022-06-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_alter_paginas_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paginas',
            name='copete',
            field=models.CharField(max_length=500),
        ),
    ]