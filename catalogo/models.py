from django.db import models
from django.urls import reverse
from catalogo.defines import ESTADO_BICI_CHOICES
'''
class bicicleta(models.Model):
	marca = models.CharField(max_length=20, null=True)
	aro = models.IntegerField(null=True)
	precio = models.IntegerField(null=True)
	imagen_bicicleta = models.ImageField(upload_to = 'imagenes_bicicletas', null=True, blank=True)

	def __str__(self):
		return "marca:'%s', aro:'%s', precio:'%s', self:'%s'" % (self.marca, self.aro, self.precio, self.imagen_bicicleta)

class equipamiento(models.Model):
	nombre = models.CharField(max_length=20, null=True)
	precio = models.IntegerField(null=True)
	imagen_equipamiento = models.ImageField(upload_to = 'imagenes_equipamiento', null=True, blank=True)

	def __str__(self):
		return self.nombre
'''

class Sede(models.Model):
	nombre_sede = models.CharField(max_length = 20, null=True)
	ubicacion_sede = models.CharField(max_length = 20, null=True)
	descripcion_sede = models.TextField()
	imagen_sede = models.ImageField(upload_to = 'imagenes_sedes', null=True, blank=True)

	def __str__(self):
		return self.nombre_sede

class Bicicleta(models.Model):
	sede_bicicleta = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
	modelo = models.CharField(max_length=20, null=True)
	marca = models.CharField(max_length=20, null=True)
	aro = models.IntegerField(null=True)
	precio = models.IntegerField(null=True)
	estado_bicicleta = models.CharField(max_length = 20, null=True, blank=True, choices = ESTADO_BICI_CHOICES)
	descripcion_bicicleta = models.TextField(null = True)
	imagen_bicicleta = models.ImageField(upload_to = 'imagenes_bicicletas', null=True, blank=True)

	def __str__(self):
		#return "marca:'%s', aro:'%s', precio:'%s', self:'%s'" % (self.marca, self.aro, self.precio, self.imagen_bicicleta)
		return self.marca

	def get_absolute_url(self):
		return reverse('catalogo:bicicleta_edit', kwargs={'pk': self.pk})


class Equipamiento(models.Model):
	sede_equipamiento = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
	nombre = models.CharField(max_length=20, null=True)
	precio = models.IntegerField(null=True)
	estado_equipamiento = models.CharField(max_length = 20, null=True, blank=True, choices = ESTADO_BICI_CHOICES)
	descripcion_equipamiento = models.TextField(null = True)
	imagen_equipamiento = models.ImageField(upload_to = 'imagenes_equipamiento', null=True, blank=True)

	def __str__(self):
		return self.nombre
		
	def get_absolute_url(self):
		return reverse('catalogo:equipamiento_edit', kwargs={'pk': self.pk})