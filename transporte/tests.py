import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Bus, Parametro, Item, Tipo_Item, Nivel_De_Precio, Cotizacion, Cliente, Itinerario, Cotizacion_Detalle
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_bus(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["rendimiento"] = "rendimiento"
    defaults["costo_por_dia"] = "costo_por_dia"
    defaults["costo_por_km"] = "costo_por_km"
    defaults["capacidad_nominal"] = "capacidad_nominal"
    defaults["capacidad_real"] = "capacidad_real"
    defaults["chofer_fijo"] = "chofer_fijo"
    defaults.update(**kwargs)
    return Bus.objects.create(**defaults)


def create_parametro(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["valor"] = "valor"
    defaults["unidad"] = "unidad"
    defaults["orden"] = "orden"
    defaults.update(**kwargs)
    return Parametro.objects.create(**defaults)


def create_item(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["unidad"] = "unidad"
    defaults["costo"] = "costo"
    defaults["precio"] = "precio"
    defaults["descripcion_compra"] = "descripcion_compra"
    defaults["descripcion_venta"] = "descripcion_venta"
    defaults.update(**kwargs)
    if "tipo_item" not in defaults:
        defaults["tipo_item"] = create_tipo_item()
    return Item.objects.create(**defaults)


def create_tipo_item(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults.update(**kwargs)
    return Tipo_Item.objects.create(**defaults)


def create_nivel_de_precio(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["tipo"] = "tipo"
    defaults["accion"] = "accion"
    defaults["valor"] = "valor"
    defaults.update(**kwargs)
    return Nivel_De_Precio.objects.create(**defaults)


def create_cotizacion(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["fecha_vence"] = "fecha_vence"
    defaults["subtotal"] = "subtotal"
    defaults["markup"] = "markup"
    defaults["total"] = "total"
    defaults.update(**kwargs)
    if "cotizacion_itinerario" not in defaults:
        defaults["cotizacion_itinerario"] = create_itinerario()
    return Cotizacion.objects.create(**defaults)


def create_cliente(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults.update(**kwargs)
    if "cliente_nivel_de_precio" not in defaults:
        defaults["cliente_nivel_de_precio"] = create_nivel_de_precio()
    return Cliente.objects.create(**defaults)


def create_itinerario(**kwargs):
    defaults = {}
    defaults["nombre"] = "nombre"
    defaults["fecha_desde"] = "fecha_desde"
    defaults["fecha_hasta"] = "fecha_hasta"
    defaults["estatus"] = "estatus"
    defaults.update(**kwargs)
    if "itinerario_cliente" not in defaults:
        defaults["itinerario_cliente"] = create_cliente()
    return Itinerario.objects.create(**defaults)


def create_cotizacion_detalle(**kwargs):
    defaults = {}
    defaults["descripcion"] = "descripcion"
    defaults["cantidad"] = "cantidad"
    defaults["markup"] = "markup"
    defaults["precio"] = "precio"
    defaults["monto"] = "monto"
    defaults["total"] = "total"
    defaults.update(**kwargs)
    if "detalle_cotizacion" not in defaults:
        defaults["detalle_cotizacion"] = create_cotizacion()
    if "detalle_item" not in defaults:
        defaults["detalle_item"] = create_item()
    return Cotizacion_Detalle.objects.create(**defaults)


class BusViewTest(unittest.TestCase):
    '''
    Tests for Bus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_bus(self):
        url = reverse('transporte_bus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bus(self):
        url = reverse('transporte_bus_create')
        data = {
            "nombre": "nombre",
            "rendimiento": "rendimiento",
            "costo_por_dia": "costo_por_dia",
            "costo_por_km": "costo_por_km",
            "capacidad_nominal": "capacidad_nominal",
            "capacidad_real": "capacidad_real",
            "chofer_fijo": "chofer_fijo",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bus(self):
        bus = create_bus()
        url = reverse('transporte_bus_detail', args=[bus.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bus(self):
        bus = create_bus()
        data = {
            "nombre": "nombre",
            "rendimiento": "rendimiento",
            "costo_por_dia": "costo_por_dia",
            "costo_por_km": "costo_por_km",
            "capacidad_nominal": "capacidad_nominal",
            "capacidad_real": "capacidad_real",
            "chofer_fijo": "chofer_fijo",
        }
        url = reverse('transporte_bus_update', args=[bus.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ParametroViewTest(unittest.TestCase):
    '''
    Tests for Parametro
    '''
    def setUp(self):
        self.client = Client()

    def test_list_parametro(self):
        url = reverse('transporte_parametro_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_parametro(self):
        url = reverse('transporte_parametro_create')
        data = {
            "nombre": "nombre",
            "valor": "valor",
            "unidad": "unidad",
            "orden": "orden",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_parametro(self):
        parametro = create_parametro()
        url = reverse('transporte_parametro_detail', args=[parametro.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_parametro(self):
        parametro = create_parametro()
        data = {
            "nombre": "nombre",
            "valor": "valor",
            "unidad": "unidad",
            "orden": "orden",
        }
        url = reverse('transporte_parametro_update', args=[parametro.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItemViewTest(unittest.TestCase):
    '''
    Tests for Item
    '''
    def setUp(self):
        self.client = Client()

    def test_list_item(self):
        url = reverse('transporte_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        url = reverse('transporte_item_create')
        data = {
            "nombre": "nombre",
            "unidad": "unidad",
            "costo": "costo",
            "precio": "precio",
            "descripcion_compra": "descripcion_compra",
            "descripcion_venta": "descripcion_venta",
            "tipo_item": create_tipo_item().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_item(self):
        item = create_item()
        url = reverse('transporte_item_detail', args=[item.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_item(self):
        item = create_item()
        data = {
            "nombre": "nombre",
            "unidad": "unidad",
            "costo": "costo",
            "precio": "precio",
            "descripcion_compra": "descripcion_compra",
            "descripcion_venta": "descripcion_venta",
            "tipo_item": create_tipo_item().id,
        }
        url = reverse('transporte_item_update', args=[item.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class Tipo_ItemViewTest(unittest.TestCase):
    '''
    Tests for Tipo_Item
    '''
    def setUp(self):
        self.client = Client()

    def test_list_tipo_item(self):
        url = reverse('transporte_tipo_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tipo_item(self):
        url = reverse('transporte_tipo_item_create')
        data = {
            "nombre": "nombre",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tipo_item(self):
        tipo_item = create_tipo_item()
        url = reverse('transporte_tipo_item_detail', args=[tipo_item.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tipo_item(self):
        tipo_item = create_tipo_item()
        data = {
            "nombre": "nombre",
        }
        url = reverse('transporte_tipo_item_update', args=[tipo_item.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class Nivel_De_PrecioViewTest(unittest.TestCase):
    '''
    Tests for Nivel_De_Precio
    '''
    def setUp(self):
        self.client = Client()

    def test_list_nivel_de_precio(self):
        url = reverse('transporte_nivel_de_precio_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_nivel_de_precio(self):
        url = reverse('transporte_nivel_de_precio_create')
        data = {
            "nombre": "nombre",
            "tipo": "tipo",
            "accion": "accion",
            "valor": "valor",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_nivel_de_precio(self):
        nivel_de_precio = create_nivel_de_precio()
        url = reverse('transporte_nivel_de_precio_detail', args=[nivel_de_precio.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_nivel_de_precio(self):
        nivel_de_precio = create_nivel_de_precio()
        data = {
            "nombre": "nombre",
            "tipo": "tipo",
            "accion": "accion",
            "valor": "valor",
        }
        url = reverse('transporte_nivel_de_precio_update', args=[nivel_de_precio.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CotizacionViewTest(unittest.TestCase):
    '''
    Tests for Cotizacion
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cotizacion(self):
        url = reverse('transporte_cotizacion_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cotizacion(self):
        url = reverse('transporte_cotizacion_create')
        data = {
            "nombre": "nombre",
            "fecha_vence": "fecha_vence",
            "subtotal": "subtotal",
            "markup": "markup",
            "total": "total",
            "cotizacion_itinerario": create_itinerario().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cotizacion(self):
        cotizacion = create_cotizacion()
        url = reverse('transporte_cotizacion_detail', args=[cotizacion.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cotizacion(self):
        cotizacion = create_cotizacion()
        data = {
            "nombre": "nombre",
            "fecha_vence": "fecha_vence",
            "subtotal": "subtotal",
            "markup": "markup",
            "total": "total",
            "cotizacion_itinerario": create_itinerario().id,
        }
        url = reverse('transporte_cotizacion_update', args=[cotizacion.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ClienteViewTest(unittest.TestCase):
    '''
    Tests for Cliente
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cliente(self):
        url = reverse('transporte_cliente_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cliente(self):
        url = reverse('transporte_cliente_create')
        data = {
            "nombre": "nombre",
            "cliente_nivel_de_precio": create_nivel_de_precio().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cliente(self):
        cliente = create_cliente()
        url = reverse('transporte_cliente_detail', args=[cliente.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cliente(self):
        cliente = create_cliente()
        data = {
            "nombre": "nombre",
            "cliente_nivel_de_precio": create_nivel_de_precio().id,
        }
        url = reverse('transporte_cliente_update', args=[cliente.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItinerarioViewTest(unittest.TestCase):
    '''
    Tests for Itinerario
    '''
    def setUp(self):
        self.client = Client()

    def test_list_itinerario(self):
        url = reverse('transporte_itinerario_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_itinerario(self):
        url = reverse('transporte_itinerario_create')
        data = {
            "nombre": "nombre",
            "fecha_desde": "fecha_desde",
            "fecha_hasta": "fecha_hasta",
            "estatus": "estatus",
            "itinerario_cliente": create_cliente().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_itinerario(self):
        itinerario = create_itinerario()
        url = reverse('transporte_itinerario_detail', args=[itinerario.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_itinerario(self):
        itinerario = create_itinerario()
        data = {
            "nombre": "nombre",
            "fecha_desde": "fecha_desde",
            "fecha_hasta": "fecha_hasta",
            "estatus": "estatus",
            "itinerario_cliente": create_cliente().id,
        }
        url = reverse('transporte_itinerario_update', args=[itinerario.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class Cotizacion_DetalleViewTest(unittest.TestCase):
    '''
    Tests for Cotizacion_Detalle
    '''
    def setUp(self):
        self.client = Client()

    def test_list_cotizacion_detalle(self):
        url = reverse('transporte_cotizacion_detalle_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cotizacion_detalle(self):
        url = reverse('transporte_cotizacion_detalle_create')
        data = {
            "descripcion": "descripcion",
            "cantidad": "cantidad",
            "markup": "markup",
            "precio": "precio",
            "monto": "monto",
            "total": "total",
            "detalle_cotizacion": create_cotizacion().id,
            "detalle_item": create_item().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cotizacion_detalle(self):
        cotizacion_detalle = create_cotizacion_detalle()
        url = reverse('transporte_cotizacion_detalle_detail', args=[cotizacion_detalle.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cotizacion_detalle(self):
        cotizacion_detalle = create_cotizacion_detalle()
        data = {
            "descripcion": "descripcion",
            "cantidad": "cantidad",
            "markup": "markup",
            "precio": "precio",
            "monto": "monto",
            "total": "total",
            "detalle_cotizacion": create_cotizacion().id,
            "detalle_item": create_item().id,
        }
        url = reverse('transporte_cotizacion_detalle_update', args=[cotizacion_detalle.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


