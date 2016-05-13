from django import forms
from django.contrib import admin

from .models import Bus, Parametro, Item, NivelDePrecio, Cotizacion, Cliente, Itinerario, CotizacionDetalle


class BusAdminForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = '__all__'


class BusAdmin(admin.ModelAdmin):
    form = BusAdminForm
    list_display = ['nombre', 'creado', 'actualizado', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real', 'chofer_fijo', 'slug']
    readonly_fields = ['creado', 'actualizado', 'slug']

admin.site.register(Bus, BusAdmin)


class ParametroAdminForm(forms.ModelForm):

    class Meta:
        model = Parametro
        fields = '__all__'


class ParametroAdmin(admin.ModelAdmin):
    form = ParametroAdminForm
    list_display = ['nombre', 'valor', 'unidad', 'orden', 'creado', 'actualizado', 'slug']
    readonly_fields = ['creado', 'actualizado', 'slug']

admin.site.register(Parametro, ParametroAdmin)


class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['nombre', 'slug', 'tipo_item', 'creado', 'actualizado', 'unidad', 'costo', 'precio',
                    'descripcion_compra', 'descripcion_venta']
    readonly_fields = ['slug', 'creado', 'actualizado']

admin.site.register(Item, ItemAdmin)


class NivelDePrecioAdminForm(forms.ModelForm):

    class Meta:
        model = NivelDePrecio
        fields = '__all__'


class NivelDePrecioAdmin(admin.ModelAdmin):
    form = NivelDePrecioAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'tipo', 'accion', 'valor', 'factor']
    readonly_fields = ['slug', 'factor', 'creado', 'actualizado']


admin.site.register(NivelDePrecio, NivelDePrecioAdmin)


class CotizacionAdminForm(forms.ModelForm):

    class Meta:
        model = Cotizacion
        fields = '__all__'


class CotizacionAdmin(admin.ModelAdmin):
    form = CotizacionAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_vence', 'subtotal', 'markup', 'total']
    readonly_fields = ['slug', 'creado', 'actualizado']

admin.site.register(Cotizacion, CotizacionAdmin)


class ClienteAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'email', 'tel']
    readonly_fields = ['slug', 'creado', 'actualizado']

admin.site.register(Cliente, ClienteAdmin)


class ItinerarioAdminForm(forms.ModelForm):

    class Meta:
        model = Itinerario
        fields = '__all__'


class ItinerarioAdmin(admin.ModelAdmin):
    form = ItinerarioAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_desde', 'fecha_hasta', 'estatus']
    readonly_fields = ['slug', 'creado', 'actualizado']

admin.site.register(Itinerario, ItinerarioAdmin)


class CotizacionDetalleAdminForm(forms.ModelForm):

    class Meta:
        model = CotizacionDetalle
        fields = '__all__'


class CotizacionDetalleAdmin(admin.ModelAdmin):
    form = CotizacionDetalleAdminForm
    list_display = ['descripcion', 'slug', 'created', 'last_updated', 'cantidad', 'markup', 'precio', 'monto', 'total']
    readonly_fields = ['slug', 'created', 'last_updated', 'monto', 'total']


admin.site.register(CotizacionDetalle, CotizacionDetalleAdmin)
