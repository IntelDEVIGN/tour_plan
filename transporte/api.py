import models
import serializers
from rest_framework import viewsets, permissions


class BusViewSet(viewsets.ModelViewSet):
    """ViewSet for the Bus class"""

    queryset = models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
    permission_classes = [permissions.IsAuthenticated]


class ParametroViewSet(viewsets.ModelViewSet):
    """ViewSet for the Parametro class"""

    queryset = models.Parametro.objects.all()
    serializer_class = serializers.ParametroSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the Item class"""

    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class Tipo_ItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the Tipo_Item class"""

    queryset = models.Tipo_Item.objects.all()
    serializer_class = serializers.Tipo_ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class Nivel_De_PrecioViewSet(viewsets.ModelViewSet):
    """ViewSet for the Nivel_De_Precio class"""

    queryset = models.Nivel_De_Precio.objects.all()
    serializer_class = serializers.Nivel_De_PrecioSerializer
    permission_classes = [permissions.IsAuthenticated]


class CotizacionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cotizacion class"""

    queryset = models.Cotizacion.objects.all()
    serializer_class = serializers.CotizacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClienteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cliente class"""

    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItinerarioViewSet(viewsets.ModelViewSet):
    """ViewSet for the Itinerario class"""

    queryset = models.Itinerario.objects.all()
    serializer_class = serializers.ItinerarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class Cotizacion_DetalleViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cotizacion_Detalle class"""

    queryset = models.Cotizacion_Detalle.objects.all()
    serializer_class = serializers.Cotizacion_DetalleSerializer
    permission_classes = [permissions.IsAuthenticated]


