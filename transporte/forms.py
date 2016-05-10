from django import forms
from .models import Bus, Parametro, Item, Tipo_Item, Nivel_De_Precio, Cotizacion, Cliente, Itinerario, Cotizacion_Detalle


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['nombre', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real', 'chofer_fijo']


class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = ['nombre', 'valor', 'unidad', 'orden']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'unidad', 'costo', 'precio', 'descripcion_compra', 'descripcion_venta', 'tipo_item']


class Tipo_ItemForm(forms.ModelForm):
    class Meta:
        model = Tipo_Item
        fields = ['nombre']


class Nivel_De_PrecioForm(forms.ModelForm):
    class Meta:
        model = Nivel_De_Precio
        fields = ['nombre', 'tipo', 'accion', 'valor']


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre', 'fecha_vence', 'subtotal', 'markup', 'total', 'cotizacion_itinerario']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'cliente_nivel_de_precio']


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['nombre', 'fecha_desde', 'fecha_hasta', 'estatus', 'itinerario_cliente']


class Cotizacion_DetalleForm(forms.ModelForm):
    class Meta:
        model = Cotizacion_Detalle
        fields = ['descripcion', 'cantidad', 'markup', 'precio', 'monto', 'total', 'detalle_cotizacion', 'detalle_item']


