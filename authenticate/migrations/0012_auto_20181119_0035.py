# Generated by Django 2.1.3 on 2018-11-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0011_auto_20181119_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bicicletas',
            field=models.ManyToManyField(blank=True, to='catalogo.Bicicleta'),
        ),
    ]
