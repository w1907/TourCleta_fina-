# Generated by Django 2.1.3 on 2018-11-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_auto_20181118_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bicicletas',
            field=models.ManyToManyField(blank=True, to='catalogo.bicicleta'),
        ),
    ]
