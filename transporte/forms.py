from django import forms

from .models import Bus, Parametro, Item, NivelDePrecio, Cotizacion, Cliente, Itinerario, \
    CotizacionDetalle


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['nombre', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real',
                  'activo', 'chofer_fijo']


class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = ['nombre', 'valor', 'unidad', 'orden']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'unidad', 'costo', 'precio', 'descripcion_compra', 'descripcion_venta', 'tipo_item']


class NivelDePrecioForm(forms.ModelForm):
    class Meta:
        model = NivelDePrecio
        fields = ['nombre', 'tipo', 'accion', 'valor', '_factor']


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre', 'fecha_vence', 'subtotal', 'markup', 'total', 'cotizacion_itinerario']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'contacto', 'email', 'tel', 'cliente_niveldeprecio']


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['nombre', 'fecha_desde', 'fecha_hasta', 'estatus', 'itinerario_cliente']


class CotizacionDetalleForm(forms.ModelForm):
    class Meta:
        model = CotizacionDetalle
        fields = ['descripcion', 'cantidad', 'markup', 'precio', 'detalle_cotizacion', 'detalle_item']
