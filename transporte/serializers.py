import models

from rest_framework import serializers


class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bus
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
            'chofer_fijo', 
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
            'creado', 
            'actualizado', 
            'unidad', 
            'costo', 
            'precio', 
            'descripcion_compra', 
            'descripcion_venta', 
        )


class Tipo_ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tipo_Item
        fields = (
            'slug', 
            'nombre', 
            'creado', 
            'actualizado', 
        )


class Nivel_De_PrecioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Nivel_De_Precio
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


class Cotizacion_DetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cotizacion_Detalle
        fields = (
            'slug', 
            'descripcion', 
            'created', 
            'last_updated', 
            'cantidad', 
            'markup', 
            'precio', 
            'monto', 
            'total', 
        )


