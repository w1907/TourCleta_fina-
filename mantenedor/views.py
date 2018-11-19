from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Bicicleta, Equipamiento
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def catalogo(request, tipo_catalogo):
	data = {}
	template = "catalogo/catalogo.html"
	data['catalogo'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = Bicicleta.objects.all()
		print(bicicletas)
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = Equipamiento.objects.all()
		data['objetos'] = equipamientos

	return render(request, template, data)

def ver_mas(request, tipo_catalogo, ver_mas, pk):
	data = {}
	template = "catalogo/ver_mas.html"
	data['ver_mas'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = Bicicleta.objects.get(id=pk)
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = Equipamiento.objects.get(id=pk)
		data['objetos'] = equipamientos
	return render(request, template, data)

class BicicletaList(ListView):
    model = Bicicleta

class BicicletaCreate(CreateView):
    model = Bicicleta
    fields = ['sede_bicicleta', 'modelo', 'marca', 'aro', 'precio', 'estado_bicicleta', 'descripcion_bicicleta','imagen_bicicleta']
    success_url = reverse_lazy('catalogo:bicicleta_list')

class BicicletaUpdate(UpdateView):
    model = Bicicleta
    fields = ['sede_bicicleta', 'modelo', 'marca', 'aro', 'precio', 'estado_bicicleta', 'descripcion_bicicleta','imagen_bicicleta']
    success_url = reverse_lazy('catalogo:bicicleta_list')

class BicicletaDelete(DeleteView):
    model = Bicicleta
    success_url = reverse_lazy('catalogo:bicicleta_list')

#CRUD EQUIPAMIENTO
class EquipamientoList(ListView):
    model = Equipamiento

class EquipamientoCreate(CreateView):
	model = Equipamiento
	fields = ['sede_equipamiento', 'nombre', 'precio', 'estado_equipamiento','descripcion_equipamiento', 'imagen_equipamiento']
	success_url = reverse_lazy('catalogo:equipamiento_list')

class EquipamientoUpdate(UpdateView):
    model = Equipamiento
    fields = ['sede_equipamiento', 'nombre', 'precio', 'estado_equipamiento','descripcion_equipamiento', 'imagen_equipamiento']
    success_url = reverse_lazy('catalogo:equipamiento_list')

class EquipamientoDelete(DeleteView):
    model = Equipamiento
    success_url = reverse_lazy('catalogo:equipamiento_list')