# Generated by Django 2.1.3 on 2018-11-19 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20181117_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=20, null=True)),
                ('ubicacion_sede', models.CharField(max_length=20, null=True)),
                ('descripcion_sede', models.TextField()),
                ('imagen_sede', models.ImageField(blank=True, null=True, upload_to='imagenes_sedes')),
            ],
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='descripcion_bicicleta',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='estado_bicicleta',
            field=models.CharField(blank=True, choices=[('DISPONIBLE', 'Disponible'), ('NO DISPONIBLE', 'No diponible'), ('RESERVADO', 'Reservado')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='descripcion_equipamiento',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='estado_equipamiento',
            field=models.CharField(blank=True, choices=[('DISPONIBLE', 'Disponible'), ('NO DISPONIBLE', 'No diponible'), ('RESERVADO', 'Reservado')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='sede_bicicleta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Sede'),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='sede_equipamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Sede'),
        ),
    ]
