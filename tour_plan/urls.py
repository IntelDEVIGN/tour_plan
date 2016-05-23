from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from transporte import api
from transporte import views
from transporte.views import indice

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'bus', api.BusViewSet)
router.register(r'parametro', api.ParametroViewSet)
router.register(r'item', api.ItemViewSet)
router.register(r'niveldeprecio', api.NivelDePrecioViewSet)
router.register(r'cotizacion', api.CotizacionViewSet)
router.register(r'cliente', api.ClienteViewSet)
router.register(r'itinerario', api.ItinerarioViewSet)
router.register(r'cotizaciondetalle', api.CotizacionDetalleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', indice, name='home'),
    url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^tabla/$', views.ItinerarioDataTable.as_view(), name='transporte_itinerario_table'),
]

urlpatterns += [
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
]

urlpatterns += [
    # urls for Bus
    url(r'^transporte/bus/$', views.BusListView.as_view(), name='transporte_bus_list'),
    url(r'^transporte/bus/create/$', views.BusCreateView.as_view(), name='transporte_bus_create'),
    url(r'^transporte/bus/detail/(?P<slug>\S+)/$', views.BusDetailView.as_view(),
        name='transporte_bus_detail'),
    url(r'^transporte/bus/update/(?P<slug>\S+)/$', views.BusUpdateView.as_view(),
        name='transporte_bus_update'),
]

urlpatterns += [
    # urls for Parametro
    url(r'^transporte/parametro/$', views.ParametroListView.as_view(),
        name='transporte_parametro_list'),
    url(r'^transporte/parametro/create/$', views.ParametroCreateView.as_view(),
        name='transporte_parametro_create'),
    url(r'^transporte/parametro/detail/(?P<slug>\S+)/$', views.ParametroDetailView.as_view(),
        name='transporte_parametro_detail'),
    url(r'^transporte/parametro/update/(?P<slug>\S+)/$', views.ParametroUpdateView.as_view(),
        name='transporte_parametro_update'),
]

urlpatterns += [
    # urls for Item
    url(r'^transporte/item/$', views.ItemListView.as_view(), name='transporte_item_list'),
    url(r'^transporte/item/create/$', views.ItemCreateView.as_view(),
        name='transporte_item_create'),
    url(r'^transporte/item/detail/(?P<slug>\S+)/$', views.ItemDetailView.as_view(),
        name='transporte_item_detail'),
    url(r'^transporte/item/update/(?P<slug>\S+)/$', views.ItemUpdateView.as_view(),
        name='transporte_item_update'),
]

urlpatterns += [
    # urls for NivelDePrecio
    url(r'^transporte/niveldeprecio/$', views.NivelDePrecioListView.as_view(),
        name='transporte_niveldeprecio_list'),
    url(r'^transporte/niveldeprecio/create/$', views.NivelDePrecioCreateView.as_view(),
        name='transporte_niveldeprecio_create'),
    url(r'^transporte/niveldeprecio/detail/(?P<slug>\S+)/$',
        views.NivelDePrecioDetailView.as_view(), name='transporte_niveldeprecio_detail'),
    url(r'^transporte/niveldeprecio/update/(?P<slug>\S+)/$',
        views.NivelDePrecioUpdateView.as_view(), name='transporte_niveldeprecio_update'),
]

urlpatterns += [
    # urls for Cotizacion
    url(r'^transporte/cotizacion/$', views.CotizacionListView.as_view(),
        name='transporte_cotizacion_list'),
    url(r'^transporte/cotizacion/create/$', views.CotizacionCreateView.as_view(),
        name='transporte_cotizacion_create'),
    url(r'^transporte/cotizacion/detail/(?P<slug>\S+)/$', views.CotizacionDetailView.as_view(),
        name='transporte_cotizacion_detail'),
    url(r'^transporte/cotizacion/update/(?P<slug>\S+)/$', views.CotizacionUpdateView.as_view(),
        name='transporte_cotizacion_update'),
]

urlpatterns += [
    # urls for Cliente
    url(r'^transporte/cliente/$', views.ClienteListView.as_view(), name='transporte_cliente_list'),
    url(r'^transporte/cliente/create/$', views.ClienteCreateView.as_view(),
        name='transporte_cliente_create'),
    url(r'^transporte/cliente/detail/(?P<slug>\S+)/$', views.ClienteDetailView.as_view(),
        name='transporte_cliente_detail'),
    url(r'^transporte/cliente/update/(?P<slug>\S+)/$', views.ClienteUpdateView.as_view(),
        name='transporte_cliente_update'),
]

urlpatterns += [
    # urls for Itinerario
    url(r'^transporte/itinerario/$', views.ItinerarioListView.as_view(),
        name='transporte_itinerario_list'),
    url(r'^transporte/itinerario/create/$', views.ItinerarioCreateView.as_view(),
        name='transporte_itinerario_create'),
    url(r'^transporte/itinerario/detail/(?P<slug>\S+)/$', views.ItinerarioDetailView.as_view(),
        name='transporte_itinerario_detail'),
    url(r'^transporte/itinerario/update/(?P<slug>\S+)/$', views.ItinerarioUpdateView.as_view(),
        name='transporte_itinerario_update'),
]

urlpatterns += [
    # urls for CotizacionDetalle
    url(r'^transporte/cotizaciondetalle/$', views.CotizacionDetalleListView.as_view(),
        name='transporte_cotizaciondetalle_list'),
    url(r'^transporte/cotizaciondetalle/create/$', views.CotizacionDetalleCreateView.as_view(),
        name='transporte_cotizaciondetalle_create'),
    url(r'^transporte/cotizaciondetalle/detail/(?P<slug>\S+)/$',
        views.CotizacionDetalleDetailView.as_view(), name='transporte_cotizaciondetalle_detail'),
    url(r'^transporte/cotizaciondetalle/update/(?P<slug>\S+)/$',
        views.CotizacionDetalleUpdateView.as_view(), name='transporte_cotizaciondetalle_update'),
]
