from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Bus, Parametro, Item, Tipo_Item, Nivel_De_Precio, Cotizacion, Cliente, Itinerario, Cotizacion_Detalle
from .forms import BusForm, ParametroForm, ItemForm, Tipo_ItemForm, Nivel_De_PrecioForm, CotizacionForm, ClienteForm, ItinerarioForm, Cotizacion_DetalleForm


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


class Tipo_ItemListView(ListView):
    model = Tipo_Item


class Tipo_ItemCreateView(CreateView):
    model = Tipo_Item
    form_class = Tipo_ItemForm


class Tipo_ItemDetailView(DetailView):
    model = Tipo_Item


class Tipo_ItemUpdateView(UpdateView):
    model = Tipo_Item
    form_class = Tipo_ItemForm


class Nivel_De_PrecioListView(ListView):
    model = Nivel_De_Precio


class Nivel_De_PrecioCreateView(CreateView):
    model = Nivel_De_Precio
    form_class = Nivel_De_PrecioForm


class Nivel_De_PrecioDetailView(DetailView):
    model = Nivel_De_Precio


class Nivel_De_PrecioUpdateView(UpdateView):
    model = Nivel_De_Precio
    form_class = Nivel_De_PrecioForm


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


class Cotizacion_DetalleListView(ListView):
    model = Cotizacion_Detalle


class Cotizacion_DetalleCreateView(CreateView):
    model = Cotizacion_Detalle
    form_class = Cotizacion_DetalleForm


class Cotizacion_DetalleDetailView(DetailView):
    model = Cotizacion_Detalle


class Cotizacion_DetalleUpdateView(UpdateView):
    model = Cotizacion_Detalle
    form_class = Cotizacion_DetalleForm

