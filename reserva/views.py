from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from reserva.models import *
from .extras import generate_order_id

from authenticate.models import Profile
from catalogo.models import *

from django.views.generic.edit import DeleteView

import datetime

'''
def reserva(request):
	data = {}
	template = "yyy.html"
	if request.method == 'POST':
		form = reservaForm(request.POST)
		if form.is_valid():
			reserva_register = form.save(commit=False)
			reserva_register.save()
			return HttpResponseRedirect(reverse('core.index'))
	else:
		form = reservaForm()
	return render(request, template, {'form':form})
'''

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def add_to_cart(request, **kwargs):
    print("ENTRE")
    tipo = kwargs.get("item_id", "tipo_catalogo")
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Bicicleta.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.bicicletas.all():
        messages.info(request, 'Ya reservaste este producto')
        return redirect('/catalog/bicicleta/') 
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "Item agregado")
    return redirect('/catalog/bicicleta/')


def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item borrado")
    return HttpResponseRedirect(reverse('order_summary'))

'''
class OrderDelete(DeleteView):
    model = Order
    template_name = "order_confirm_delete.html"
    success_url = reverse_lazy('product-list')
'''

def deleteOrder(request, order_id):
    data = {}
    template = "order_confirm_delete.html"
    print(":D")
    ORDENES = Order.objects.get(pk=order_id)
    print(ORDENES.owner)
    a = ORDENES.get_cart_items()
    if request.POST:
        for i in a:
            Profile.bicicletas.through.objects.filter(bicicleta_id=i.product, profile_id=ORDENES.owner.pk).delete()
        ORDENES.delete()
        return HttpResponseRedirect(reverse("catalogo_lista"))
    return render(request, template, {'order': ORDENES})



def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)

def update_transaction_records(request, order_id):
    # get the order being processed
    order_to_purchase = Order.objects.filter(pk=order_id).first()

    # update the placed order
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()
    
    # get all items in the order - generates a queryset
    order_items = order_to_purchase.items.all()

    # update order items
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    # Add products to user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # get the products from the items
    order_products = [item.product for item in order_items]
    user_profile.bicicletas.add(*order_products)
    user_profile.save()

    # send an email to the customer
    # look at tutorial on how to send emails with sendgrid
    messages.info(request, "Se realizo la reserva con exito!")
    return HttpResponseRedirect(reverse('my_profile'))
    
def success(request, **kwargs):
    # a view signifying the transcation was successful
    return render(request, 'shopping_cart/purchase_success.html', {})