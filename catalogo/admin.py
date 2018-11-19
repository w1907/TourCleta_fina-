from django.contrib import admin
from catalogo.models import Bicicleta, Equipamiento, Sede

'''
@admin.register(Bicicleta)
class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('sede_bicicleta', 'marca', 'aro', 'precio', 'estado_bicicleta', 'descripcion_bicicleta', 'imagen_bicicleta', )

@admin.register(Equipamiento)
class EquipamientoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio',)
'''

admin.site.register(Bicicleta)
admin.site.register(Equipamiento)
admin.site.register(Sede)