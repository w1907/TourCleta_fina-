# Generated by Django 2.1.3 on 2018-11-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20181117_0310'),
        ('authenticate', '0008_auto_20181118_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bicicletas',
        ),
        migrations.AddField(
            model_name='profile',
            name='bicicletas',
            field=models.ManyToManyField(null=True, to='catalogo.bicicleta'),
        ),
    ]
