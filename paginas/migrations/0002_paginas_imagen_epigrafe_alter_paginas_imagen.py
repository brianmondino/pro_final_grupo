# Generated by Django 4.0.4 on 2022-06-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginas',
            name='imagen_epigrafe',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paginas',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagenes'),
        ),
    ]