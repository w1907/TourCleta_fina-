from django.conf.urls import url
from django.urls import path
from catalogo import views


urlpatterns = [
	path("", views.catalogo, name="catalogo_lista"),
	path('<str:tipo_catalogo>/', views.catalogo, name="catalogoBicicletas"),
	#path('<str:tipo_catalogo>/', views.catalogo, name="view.catalogo"),
    #url(r'^', views.product_list, name='product-list'),
	path('<str:tipo_catalogo>/<str:ver_mas>/<int:pk>', views.ver_mas, name="view.ver_mas"),
] 