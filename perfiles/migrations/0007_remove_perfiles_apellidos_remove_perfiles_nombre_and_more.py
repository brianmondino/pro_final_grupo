# Generated by Django 4.0.5 on 2022-06-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0006_perfiles_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiles',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='perfiles',
            name='nombre',
        ),
        migrations.AddField(
            model_name='perfiles',
            name='telefono',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]
