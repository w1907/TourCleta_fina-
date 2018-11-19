from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
	#path('', views.catalogo, name='view.catalogo'),
	path('bicicleta_list/', views.BicicletaList.as_view(), name='bicicleta_list'),
	path('equipamiento_list/', views.EquipamientoList.as_view(), name='equipamiento_list'),
	#path('<str:tipo_catalogo>', views.catalogo, name="view.catalogo"),
	#path('<str:tipo_catalogo>/<str:ver_mas>/<int:pk>', views.ver_mas, name="view.ver_mas"),
	path('new_bicicleta/', views.BicicletaCreate.as_view(), name='bicicleta_new'),
	path('edit_bicicleta/<int:pk>', views.BicicletaUpdate.as_view(), name='bicicleta_edit'),
	path('delete_bicicleta/<int:pk>', views.BicicletaDelete.as_view(), name='bicicleta_delete'),
	path('new_equipamiento/', views.EquipamientoCreate.as_view(), name='equipamiento_new'),
	path('edit_equipamiento/<int:pk>', views.EquipamientoUpdate.as_view(), name='equipamiento_edit'),
	path('delete_equipamiento/<int:pk>', views.EquipamientoDelete.as_view(), name='equipamiento_delete'),
]