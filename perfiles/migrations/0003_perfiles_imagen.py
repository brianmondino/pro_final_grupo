# Generated by Django 4.0.4 on 2022-06-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_perfiles_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiles',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
    ]
