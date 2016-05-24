from django import forms
from django.contrib import admin

from .models import TipoDeVehiculo, Parametro, Item, NivelDePrecio, Cotizacion, Cliente, Itinerario, CotizacionDetalle


class TipoDeVehiculoAdminForm(forms.ModelForm):
    class Meta:
        model = TipoDeVehiculo
        fields = '__all__'


class TipoDeVehiculoAdmin(admin.ModelAdmin):
    form = TipoDeVehiculoAdminForm
    list_display = ['nombre', 'rendimiento', 'costo_por_dia', 'costo_por_km',
                    'capacidad_nominal', 'capacidad_real', 'chofer_fijo', 'creado', 'actualizado', 'slug']
    readonly_fields = ['creado', 'actualizado', 'slug']
    search_fields = ['nombre']


admin.site.register(TipoDeVehiculo, TipoDeVehiculoAdmin)


class ParametroAdminForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = '__all__'


class ParametroAdmin(admin.ModelAdmin):
    form = ParametroAdminForm
    list_display = ['annio', 'nombre', 'valor', 'unidad', 'orden', 'creado', 'actualizado', 'slug']
    readonly_fields = ['creado', 'actualizado', 'slug']
    search_fields = ['nombre']
    list_filter = ['annio']


admin.site.register(Parametro, ParametroAdmin)


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['nombre', 'tipo_item', 'unidad', 'costo', 'precio',
                    'descripcion_compra', 'descripcion_venta', 'creado', 'actualizado', 'slug']
    readonly_fields = ['slug', 'creado', 'actualizado']
    search_fields = ['nombre', 'descripcion_compra', 'descripcion_venta']


admin.site.register(Item, ItemAdmin)


class NivelDePrecioAdminForm(forms.ModelForm):
    class Meta:
        model = NivelDePrecio
        fields = '__all__'


class NivelDePrecioAdmin(admin.ModelAdmin):
    form = NivelDePrecioAdminForm
    list_display = ['nombre', 'tipo', 'accion', 'valor', 'factor', 'creado', 'actualizado', 'slug']
    readonly_fields = ['slug', 'factor', 'creado', 'actualizado']
    search_fields = ['nombre']


admin.site.register(NivelDePrecio, NivelDePrecioAdmin)


class CotizacionAdminForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = '__all__'


class CotizacionAdmin(admin.ModelAdmin):
    form = CotizacionAdminForm
    list_display = ['nombre', 'fecha_vence', 'subtotal', 'markup', 'total', 'creado', 'actualizado', 'slug']
    readonly_fields = ['slug', 'creado', 'actualizado']
    search_fields = ['nombre']
    list_filter = ['fecha_vence']
    date_hierarchy = 'fecha_vence'


admin.site.register(Cotizacion, CotizacionAdmin)


class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ['nombre', 'contacto', 'email', 'tel', 'creado', 'actualizado', 'slug']
    readonly_fields = ['slug', 'creado', 'actualizado']
    search_fields = ['nombre', 'contacto', 'email', 'tel']


admin.site.register(Cliente, ClienteAdmin)


class ItinerarioAdminForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['cliente', 'nombre', 'fecha_desde', 'fecha_hasta', 'estatus']


class ItinerarioAdmin(admin.ModelAdmin):
    form = ItinerarioAdminForm
    list_display = ['cliente', 'nombre', 'fecha_desde', 'fecha_hasta', 'estatus', 'creado', 'actualizado',
                    'slug']
    readonly_fields = ['slug', 'creado', 'actualizado']
    search_fields = ['cliente', 'nombre', 'fecha_desde']
    list_filter = ['fecha_desde', 'fecha_hasta', 'estatus']
    ordering = ['cliente', 'fecha_desde']
    date_hierarchy = 'fecha_desde'


admin.site.register(Itinerario, ItinerarioAdmin)


class CotizacionDetalleAdminForm(forms.ModelForm):
    class Meta:
        model = CotizacionDetalle
        fields = '__all__'


class CotizacionDetalleAdmin(admin.ModelAdmin):
    form = CotizacionDetalleAdminForm
    list_display = ['descripcion', 'cantidad', 'markup', 'precio', 'monto', 'total', 'created', 'last_updated', 'slug']
    readonly_fields = ['slug', 'created', 'last_updated', 'monto', 'total']
    search_fields = ['descripcion']


admin.site.register(CotizacionDetalle, CotizacionDetalleAdmin)
