from rest_framework import serializers

from . import models


class TipoDeVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoDeVehiculo
        fields = (
            'slug', 
            'nombre', 
            'creado', 
            'actualizado', 
            'rendimiento', 
            'costo_por_dia', 
            'costo_por_km',
            'capacidad_nominal',
            'capacidad_real',
        )


class ParametroSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Parametro
        fields = (
            'slug', 
            'nombre', 
            'valor', 
            'unidad', 
            'orden', 
            'creado', 
            'actualizado', 
        )


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = (
            'slug',
            'nombre',
            'tipo_item',
            'creado', 
            'actualizado', 
            'unidad', 
            'costo', 
            'precio', 
            'descripcion_compra', 
            'descripcion_venta', 
        )


class NivelDePrecioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NivelDePrecio
        fields = (
            'slug', 
            'nombre', 
            'creado', 
            'actualizado', 
            'tipo', 
            'accion', 
            'valor', 
        )


class CotizacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cotizacion
        fields = (
            'slug', 
            'nombre', 
            'creado', 
            'actualizado', 
            'fecha_vence', 
            'subtotal', 
            'markup', 
            'total', 
        )


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cliente
        fields = (
            'slug',
            'nombre',
            'email',
            'tel',
            'creado', 
            'actualizado', 
        )


class ItinerarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Itinerario
        fields = (
            'slug', 
            'nombre', 
            'creado', 
            'actualizado', 
            'fecha_desde', 
            'fecha_hasta', 
            'estatus', 
        )


class CotizacionDetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CotizacionDetalle
        fields = (
            'slug',
            'descripcion',
            'creado',
            'actualizado', 
            'cantidad', 
            'markup', 
            'precio', 
            'monto',
            'total',
        )


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehiculo
        fields = (
            'slug',
            'nombre',
            'chofer_fijo',
            'fecha_adquirido',
            'creado',
            'actualizado',
            'placa',
        )


