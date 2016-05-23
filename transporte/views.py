from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .forms import BusForm, ParametroForm, ItemForm, NivelDePrecioForm, CotizacionForm, ClienteForm, \
    ItinerarioForm, CotizacionDetalleForm
from .models import Bus, Parametro, Item, NivelDePrecio, Cotizacion, Cliente, Itinerario, \
    CotizacionDetalle


def indice(request):
    """
    :param request:
    :return: Listado de Buses
    """

    buses = Bus.objects.all()

    context = {
        'buses': buses,
    }

    return render(request, "index.html", context)


class ItinerarioDataTable(ListView):
    model = Itinerario
    template_name = 'itinerario_datatable.html'

    def get_queryset(self):
        return Itinerario.objects.all()


class BusListView(ListView):
    model = Bus


class BusCreateView(CreateView):
    model = Bus
    form_class = BusForm


class BusDetailView(DetailView):
    model = Bus


class BusUpdateView(UpdateView):
    model = Bus
    form_class = BusForm


class ParametroListView(ListView):
    model = Parametro


class ParametroCreateView(CreateView):
    model = Parametro
    form_class = ParametroForm


class ParametroDetailView(DetailView):
    model = Parametro


class ParametroUpdateView(UpdateView):
    model = Parametro
    form_class = ParametroForm


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm


class ItemDetailView(DetailView):
    model = Item


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm


class NivelDePrecioListView(ListView):
    model = NivelDePrecio


class NivelDePrecioCreateView(CreateView):
    model = NivelDePrecio
    form_class = NivelDePrecioForm


class NivelDePrecioDetailView(DetailView):
    model = NivelDePrecio


class NivelDePrecioUpdateView(UpdateView):
    model = NivelDePrecio
    form_class = NivelDePrecioForm


class CotizacionListView(ListView):
    model = Cotizacion


class CotizacionCreateView(CreateView):
    model = Cotizacion
    form_class = CotizacionForm


class CotizacionDetailView(DetailView):
    model = Cotizacion


class CotizacionUpdateView(UpdateView):
    model = Cotizacion
    form_class = CotizacionForm


class ClienteListView(ListView):
    model = Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm


class ItinerarioListView(ListView):
    model = Itinerario


class ItinerarioCreateView(CreateView):
    model = Itinerario
    form_class = ItinerarioForm


class ItinerarioDetailView(DetailView):
    model = Itinerario


class ItinerarioUpdateView(UpdateView):
    model = Itinerario
    form_class = ItinerarioForm


class CotizacionDetalleListView(ListView):
    model = CotizacionDetalle


class CotizacionDetalleCreateView(CreateView):
    model = CotizacionDetalle
    form_class = CotizacionDetalleForm


class CotizacionDetalleDetailView(DetailView):
    model = CotizacionDetalle


class CotizacionDetalleUpdateView(UpdateView):
    model = CotizacionDetalle
    form_class = CotizacionDetalleForm
