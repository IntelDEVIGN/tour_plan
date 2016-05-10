from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'bus', api.BusViewSet)
router.register(r'parametro', api.ParametroViewSet)
router.register(r'item', api.ItemViewSet)
router.register(r'tipo_item', api.Tipo_ItemViewSet)
router.register(r'nivel_de_precio', api.Nivel_De_PrecioViewSet)
router.register(r'cotizacion', api.CotizacionViewSet)
router.register(r'cliente', api.ClienteViewSet)
router.register(r'itinerario', api.ItinerarioViewSet)
router.register(r'cotizacion_detalle', api.Cotizacion_DetalleViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for Bus
    url(r'^transporte/bus/$', views.BusListView.as_view(), name='transporte_bus_list'),
    url(r'^transporte/bus/create/$', views.BusCreateView.as_view(), name='transporte_bus_create'),
    url(r'^transporte/bus/detail/(?P<slug>\S+)/$', views.BusDetailView.as_view(), name='transporte_bus_detail'),
    url(r'^transporte/bus/update/(?P<slug>\S+)/$', views.BusUpdateView.as_view(), name='transporte_bus_update'),
)

urlpatterns += patterns('',
    # urls for Parametro
    url(r'^transporte/parametro/$', views.ParametroListView.as_view(), name='transporte_parametro_list'),
    url(r'^transporte/parametro/create/$', views.ParametroCreateView.as_view(), name='transporte_parametro_create'),
    url(r'^transporte/parametro/detail/(?P<slug>\S+)/$', views.ParametroDetailView.as_view(), name='transporte_parametro_detail'),
    url(r'^transporte/parametro/update/(?P<slug>\S+)/$', views.ParametroUpdateView.as_view(), name='transporte_parametro_update'),
)

urlpatterns += patterns('',
    # urls for Item
    url(r'^transporte/item/$', views.ItemListView.as_view(), name='transporte_item_list'),
    url(r'^transporte/item/create/$', views.ItemCreateView.as_view(), name='transporte_item_create'),
    url(r'^transporte/item/detail/(?P<slug>\S+)/$', views.ItemDetailView.as_view(), name='transporte_item_detail'),
    url(r'^transporte/item/update/(?P<slug>\S+)/$', views.ItemUpdateView.as_view(), name='transporte_item_update'),
)

urlpatterns += patterns('',
    # urls for Tipo_Item
    url(r'^transporte/tipo_item/$', views.Tipo_ItemListView.as_view(), name='transporte_tipo_item_list'),
    url(r'^transporte/tipo_item/create/$', views.Tipo_ItemCreateView.as_view(), name='transporte_tipo_item_create'),
    url(r'^transporte/tipo_item/detail/(?P<slug>\S+)/$', views.Tipo_ItemDetailView.as_view(), name='transporte_tipo_item_detail'),
    url(r'^transporte/tipo_item/update/(?P<slug>\S+)/$', views.Tipo_ItemUpdateView.as_view(), name='transporte_tipo_item_update'),
)

urlpatterns += patterns('',
    # urls for Nivel_De_Precio
    url(r'^transporte/nivel_de_precio/$', views.Nivel_De_PrecioListView.as_view(), name='transporte_nivel_de_precio_list'),
    url(r'^transporte/nivel_de_precio/create/$', views.Nivel_De_PrecioCreateView.as_view(), name='transporte_nivel_de_precio_create'),
    url(r'^transporte/nivel_de_precio/detail/(?P<slug>\S+)/$', views.Nivel_De_PrecioDetailView.as_view(), name='transporte_nivel_de_precio_detail'),
    url(r'^transporte/nivel_de_precio/update/(?P<slug>\S+)/$', views.Nivel_De_PrecioUpdateView.as_view(), name='transporte_nivel_de_precio_update'),
)

urlpatterns += patterns('',
    # urls for Cotizacion
    url(r'^transporte/cotizacion/$', views.CotizacionListView.as_view(), name='transporte_cotizacion_list'),
    url(r'^transporte/cotizacion/create/$', views.CotizacionCreateView.as_view(), name='transporte_cotizacion_create'),
    url(r'^transporte/cotizacion/detail/(?P<slug>\S+)/$', views.CotizacionDetailView.as_view(), name='transporte_cotizacion_detail'),
    url(r'^transporte/cotizacion/update/(?P<slug>\S+)/$', views.CotizacionUpdateView.as_view(), name='transporte_cotizacion_update'),
)

urlpatterns += patterns('',
    # urls for Cliente
    url(r'^transporte/cliente/$', views.ClienteListView.as_view(), name='transporte_cliente_list'),
    url(r'^transporte/cliente/create/$', views.ClienteCreateView.as_view(), name='transporte_cliente_create'),
    url(r'^transporte/cliente/detail/(?P<slug>\S+)/$', views.ClienteDetailView.as_view(), name='transporte_cliente_detail'),
    url(r'^transporte/cliente/update/(?P<slug>\S+)/$', views.ClienteUpdateView.as_view(), name='transporte_cliente_update'),
)

urlpatterns += patterns('',
    # urls for Itinerario
    url(r'^transporte/itinerario/$', views.ItinerarioListView.as_view(), name='transporte_itinerario_list'),
    url(r'^transporte/itinerario/create/$', views.ItinerarioCreateView.as_view(), name='transporte_itinerario_create'),
    url(r'^transporte/itinerario/detail/(?P<slug>\S+)/$', views.ItinerarioDetailView.as_view(), name='transporte_itinerario_detail'),
    url(r'^transporte/itinerario/update/(?P<slug>\S+)/$', views.ItinerarioUpdateView.as_view(), name='transporte_itinerario_update'),
)

urlpatterns += patterns('',
    # urls for Cotizacion_Detalle
    url(r'^transporte/cotizacion_detalle/$', views.Cotizacion_DetalleListView.as_view(), name='transporte_cotizacion_detalle_list'),
    url(r'^transporte/cotizacion_detalle/create/$', views.Cotizacion_DetalleCreateView.as_view(), name='transporte_cotizacion_detalle_create'),
    url(r'^transporte/cotizacion_detalle/detail/(?P<slug>\S+)/$', views.Cotizacion_DetalleDetailView.as_view(), name='transporte_cotizacion_detalle_detail'),
    url(r'^transporte/cotizacion_detalle/update/(?P<slug>\S+)/$', views.Cotizacion_DetalleUpdateView.as_view(), name='transporte_cotizacion_detalle_update'),
)

