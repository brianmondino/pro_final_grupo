# Generated by Django 4.0.4 on 2022-06-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuarios_perfilid'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
    ]