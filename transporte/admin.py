from django.contrib import admin
from django import forms
from .models import Bus, Parametro, Item, Tipo_Item, Nivel_De_Precio, Cotizacion, Cliente, Itinerario, Cotizacion_Detalle

class BusAdminForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = '__all__'


class BusAdmin(admin.ModelAdmin):
    form = BusAdminForm
    list_display = ['nombre', 'creado', 'actualizado', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real', 'chofer_fijo', 'slug']
    readonly_fields = ['nombre', 'creado', 'actualizado', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real', 'chofer_fijo', 'slug']

admin.site.register(Bus, BusAdmin)


class ParametroAdminForm(forms.ModelForm):

    class Meta:
        model = Parametro
        fields = '__all__'


class ParametroAdmin(admin.ModelAdmin):
    form = ParametroAdminForm
    list_display = ['nombre', 'valor', 'unidad', 'orden', 'creado', 'actualizado', 'slug']
    readonly_fields = ['nombre', 'valor', 'unidad', 'orden', 'creado', 'actualizado', 'slug']

admin.site.register(Parametro, ParametroAdmin)


class ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'unidad', 'costo', 'precio', 'descripcion_compra', 'descripcion_venta']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado', 'unidad', 'costo', 'precio', 'descripcion_compra', 'descripcion_venta']

admin.site.register(Item, ItemAdmin)


class Tipo_ItemAdminForm(forms.ModelForm):

    class Meta:
        model = Tipo_Item
        fields = '__all__'


class Tipo_ItemAdmin(admin.ModelAdmin):
    form = Tipo_ItemAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado']

admin.site.register(Tipo_Item, Tipo_ItemAdmin)


class Nivel_De_PrecioAdminForm(forms.ModelForm):

    class Meta:
        model = Nivel_De_Precio
        fields = '__all__'


class Nivel_De_PrecioAdmin(admin.ModelAdmin):
    form = Nivel_De_PrecioAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'tipo', 'accion', 'valor']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado', 'tipo', 'accion', 'valor']

admin.site.register(Nivel_De_Precio, Nivel_De_PrecioAdmin)


class CotizacionAdminForm(forms.ModelForm):

    class Meta:
        model = Cotizacion
        fields = '__all__'


class CotizacionAdmin(admin.ModelAdmin):
    form = CotizacionAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_vence', 'subtotal', 'markup', 'total']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_vence', 'subtotal', 'markup', 'total']

admin.site.register(Cotizacion, CotizacionAdmin)


class ClienteAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado']

admin.site.register(Cliente, ClienteAdmin)


class ItinerarioAdminForm(forms.ModelForm):

    class Meta:
        model = Itinerario
        fields = '__all__'


class ItinerarioAdmin(admin.ModelAdmin):
    form = ItinerarioAdminForm
    list_display = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_desde', 'fecha_hasta', 'estatus']
    readonly_fields = ['nombre', 'slug', 'creado', 'actualizado', 'fecha_desde', 'fecha_hasta', 'estatus']

admin.site.register(Itinerario, ItinerarioAdmin)


class Cotizacion_DetalleAdminForm(forms.ModelForm):

    class Meta:
        model = Cotizacion_Detalle
        fields = '__all__'


class Cotizacion_DetalleAdmin(admin.ModelAdmin):
    form = Cotizacion_DetalleAdminForm
    list_display = ['descripcion', 'slug', 'created', 'last_updated', 'cantidad', 'markup', 'precio', 'monto', 'total']
    readonly_fields = ['descripcion', 'slug', 'created', 'last_updated', 'cantidad', 'markup', 'precio', 'monto', 'total']

admin.site.register(Cotizacion_Detalle, Cotizacion_DetalleAdmin)


