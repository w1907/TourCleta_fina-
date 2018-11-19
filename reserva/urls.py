from django.urls import path
from django.conf.urls import url
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    success,
    deleteOrder,
    update_transaction_records
)

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    path('borrar/<int:order_id>', deleteOrder, name='order_delete2'),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/(?P<order_id>[-\w]+)/$', update_transaction_records, name='checkout')
 ]
'''
urlpatterns = [
	path('', views.reserva, name="view.reserva"),
]
'''