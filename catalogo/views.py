from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Bicicleta, Equipamiento
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from reserva.models import *

def catalogo(request, **kwargs):
	data = {}
	template = "catalogo.html"
	tipo_catalogo = kwargs.get("tipo_catalogo")
	data['catalogo'] = tipo_catalogo
	filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
	if tipo_catalogo == "bicicleta":
		bicicletas = Bicicleta.objects.all()
		data['objetos'] = bicicletas
		current_order_products = []
		if filtered_orders.exists():
			user_order = filtered_orders[0]
			user_order_items = user_order.items.all()
			current_order_products = [product.product for product in user_order_items]
		data['current_order_products'] = current_order_products
	elif tipo_catalogo == "equipamiento":
		equipamientos = Equipamiento.objects.all()
		data['objetos'] = equipamientos

	return render(request, template, data)

def ver_mas(request, tipo_catalogo, ver_mas, pk):
	data = {}
	template = "ver_mas.html"
	data['ver_mas'] = tipo_catalogo
	if tipo_catalogo == "bicicleta":
		bicicletas = Bicicleta.objects.get(id=pk)
		data['objetos'] = bicicletas
	elif tipo_catalogo == "equipamiento":
		equipamientos = Equipamiento.objects.get(id=pk)
		data['objetos'] = equipamientos
	return render(request, template, data)

def product_list(request):
    object_list = Bicicleta.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "product_list.html", context)
