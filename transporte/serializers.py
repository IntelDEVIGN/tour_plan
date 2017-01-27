from rest_framework import serializers

from . import models


class TipoDeVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoDeVehiculo
        fields = (
            'slug',
            'nombre',
            'rendimiento',
            'costo_por_dia', 
            'costo_por_km',
            'capacidad_nominal',
            'capacidad_real',
            'galones_tanque',
            'creado',
            'actualizado',
        )


class ParametroSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Parametro
        fields = (
            'slug',
            'annio',
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
    tipo_nombre = serializers.ReadOnlyField()
    costo_por_dia = serializers.ReadOnlyField()
    costo_por_km = serializers.ReadOnlyField()
    capacidad_nominal = serializers.ReadOnlyField()
    capacidad_real = serializers.ReadOnlyField()
    galones_tanque = serializers.ReadOnlyField()

    class Meta:
        model = models.Vehiculo
        fields = (
            'slug',
            'nombre',
            'chofer_fijo',
            'fecha_adquirido',
            'placa',
            'tipo',
            'tipo_nombre',
            'costo_por_dia',
            'costo_por_km',
            'capacidad_nominal',
            'capacidad_real',
            'galones_tanque',
            'creado',
            'actualizado',
        )


class TramoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tramo
        fields = (
            'slug',
            'nombre',
            'creado',
            'actualizado',
            'codigo',
            'desde_hacia',
            'kms',
            'hrs',
            'codigo_desde',
            'codigo_hacia',
        )


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lugar
        fields = (
            'slug',
            'codigo',
            'creado',
            'actualizado',
            'nombre',
            'pais',
        )


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conductor
        fields = (
            'slug',
            'nombre',
            'creado',
            'actualizado',
            'identidad',
            'telefono',
            'empleado',
            'incentivo_por_dia',
        )
