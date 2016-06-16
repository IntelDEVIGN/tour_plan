from rest_framework import viewsets, permissions

from . import models
from . import serializers


class TipoDeVehiculoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoDeVehiculo class"""

    queryset = models.TipoDeVehiculo.objects.all()
    serializer_class = serializers.TipoDeVehiculoSerializer
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


class NivelDePrecioViewSet(viewsets.ModelViewSet):
    """ViewSet for the NivelDePrecio class"""

    queryset = models.NivelDePrecio.objects.all()
    serializer_class = serializers.NivelDePrecioSerializer
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


class CotizacionDetalleViewSet(viewsets.ModelViewSet):
    """ViewSet for the CotizacionDetalle class"""

    queryset = models.CotizacionDetalle.objects.all()
    serializer_class = serializers.CotizacionDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehiculoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Vehiculo class"""

    queryset = models.Vehiculo.objects.all()
    serializer_class = serializers.VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]
