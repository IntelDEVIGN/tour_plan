from functools import partial

from datetimewidget.widgets import DateWidget
from django import forms
from django.forms.utils import ErrorList

from .models import TipoDeVehiculo, Parametro, Item, NivelDePrecio, Cotizacion, Cliente, Itinerario, \
    CotizacionDetalle, Vehiculo


class TipoDeVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoDeVehiculo
        fields = ['nombre', 'rendimiento', 'costo_por_dia', 'costo_por_km', 'capacidad_nominal', 'capacidad_real',
                  'activo']


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
        fields = ['nombre', 'tipo', 'accion', 'valor']


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fecha_vence = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
        fields = ['nombre', 'fecha_vence', 'subtotal', 'markup', 'total', 'itinerario']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'contacto', 'email', 'tel', 'nivel_de_precio']


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = ['nombre', 'fecha_desde', 'fecha_hasta', 'estatus', 'cliente']

        fecha_desde = forms.DateField(widget=DateInput())
        fecha_hasta = forms.DateField(widget=DateInput())

    def clean(self):
        if self.cleaned_data['fecha_desde'] > self.cleaned_data['fecha_hasta']:
            msg = 'La fecha de inicio no puede ser mayor que la fecha de final.'
            self._errors['fecha_desde'] = ErrorList([msg])
            del self.cleaned_data['fecha_desde']

        return self.cleaned_data


class CotizacionDetalleForm(forms.ModelForm):
    class Meta:
        model = CotizacionDetalle
        fields = ['descripcion', 'cantidad', 'markup', 'precio', 'cotizacion', 'item']


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['nombre', 'placa', 'tipo', 'chofer_fijo', 'fecha_adquirido']
