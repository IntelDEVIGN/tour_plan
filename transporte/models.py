#!/usr/bin/python
# -*- coding:  utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models as models
from django.db.models import *
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django_extensions.db import fields as extension_fields
from djchoices import DjangoChoices, ChoiceItem


class TipoDeVehiculo(models.Model):
    # Fields
    nombre = CharField(max_length=20)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    rendimiento = IntegerField()
    costo_por_dia = DecimalField(max_digits=10, decimal_places=2)
    costo_por_km = DecimalField(max_digits=10, decimal_places=2)
    capacidad_nominal = IntegerField()
    capacidad_real = IntegerField()
    galones_tanque = DecimalField(max_digits=6, decimal_places=2)
    activo = BooleanField(default=True)
    creado = DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Tipo de Vehículo')
        verbose_name_plural = _('Tipos de Vehículo')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_tipodevehiculo_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_tipodevehiculo_update', args=(self.slug,))


class Parametro(models.Model):
    ANNIOS = []
    for r in range(2016, (datetime.datetime.now().year + 2)):
        ANNIOS.append((r, r))
    # Fields
    annio = IntegerField(verbose_name='Año', choices=ANNIOS, default=datetime.datetime.now().year)
    nombre = CharField(max_length=25)
    valor = CharField(max_length=100)
    unidad = CharField(max_length=100)
    orden = IntegerField(default=0)
    slug = extension_fields.AutoSlugField(populate_from=('annio', 'nombre'), blank=True, overwrite=True)
    creado = DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['annio', 'orden', ]
        verbose_name = _('Parámetro')
        verbose_name_plural = _('Parámetros')
        unique_together = ('annio', 'nombre')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_parametro_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_parametro_update', args=(self.slug,))


class Item(models.Model):
    # Choices
    class TipoItem(DjangoChoices):
        Insumo = ChoiceItem("Insumo")
        Servicio = ChoiceItem("Servicio")
        Subcontratado = ChoiceItem("Subcontratado")
        Cargo = ChoiceItem("Cargo")
        Descuento = ChoiceItem("Descuento")
        Impuesto = ChoiceItem("Impuesto")
        Grupo = ChoiceItem("Grupo")

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    tipo_item = models.CharField(max_length=13,
                                 choices=TipoItem.choices,
                                 validators=[TipoItem.validator],
                                 default=TipoItem.Servicio)
    unidad = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=10, decimal_places=4)
    precio = models.DecimalField(max_digits=10, decimal_places=4)
    descripcion_compra = models.CharField(max_length=50)
    descripcion_venta = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_item_update', args=(self.slug,))


class NivelDePrecio(models.Model):
    # Choices
    class Tipo(DjangoChoices):
        Porcentaje = ChoiceItem("Porcentaje")
        Valor = ChoiceItem("Valor")

    class Accion(DjangoChoices):
        Incrementa = ChoiceItem("Incrementa")
        Decrementa = ChoiceItem("Decrementa")

    # Fields
    nombre = models.CharField(max_length=50)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    tipo = models.CharField(max_length=10, choices=Tipo.choices, validators=[Tipo.validator], default=Tipo.Porcentaje)
    accion = models.CharField(max_length=10, choices=Accion.choices, validators=[Accion.validator],
                              default=Accion.Incrementa)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    _factor = models.DecimalField(max_digits=5, decimal_places=4, db_column='factor', null=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Nivel de Precio')
        verbose_name_plural = _('Niveles de Precio')

    @property
    def factor(self):
        return 1 / (1 - self.valor)

    @factor.setter
    def factor(self, value):
        self._factor = value

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_niveldeprecio_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_niveldeprecio_update', args=(self.slug,))

    @property
    def porciento(self):
        return self.valor * 100.0


class Cliente(models.Model):
    # Fields
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    email = models.EmailField(unique=True, db_index=True, null=True)
    tel = models.CharField(max_length=15, null=True)
    ciudad = models.CharField(max_length=50, default='San Pedro Sula')
    pais = models.CharField(max_length=50, default='Honduras')
    rtn = models.CharField(max_length=16)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    nivel_de_precio = models.ForeignKey(NivelDePrecio,
                                        verbose_name='nivel de precio',
                                        on_delete=models.PROTECT,
                                        default=4)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_cliente_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cliente_update', args=(self.slug,))


class Itinerario(models.Model):
    # estatus opciones
    class Status(DjangoChoices):
        Solicitado = ChoiceItem("Solicitado")
        Cotizado = ChoiceItem("Cotizado")
        Confirmado = ChoiceItem("Confirmado")
        Facturado = ChoiceItem("Facturado")
        Cerrado = ChoiceItem("Cerrado")

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    fecha_desde = models.DateField(verbose_name='inicia')
    fecha_hasta = models.DateField(verbose_name='termina')
    estatus = models.CharField(max_length=10, choices=Status.choices, validators=[Status.validator],
                               default=Status.Solicitado)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    cliente = models.ForeignKey(Cliente, on_delete=CASCADE, verbose_name='cliente')

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Itinerario')
        verbose_name_plural = _('Itinerarios')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_itinerario_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_itinerario_update', args=(self.slug,))


class Cotizacion(models.Model):
    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    fecha_vence = models.DateField(default=now)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    markup = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    itinerario = models.ForeignKey(Itinerario, on_delete=CASCADE, verbose_name='itinerario')

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Cotización')
        verbose_name_plural = _('Cotizaciones')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_cotizacion_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cotizacion_update', args=(self.slug,))


class CotizacionDetalle(models.Model):
    # Fields
    descripcion = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    _monto = models.DecimalField(max_digits=10, decimal_places=2, db_column="monto")
    markup = models.DecimalField(max_digits=5, decimal_places=2)
    _total = models.DecimalField(max_digits=10, decimal_places=2, db_column="total")
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    cotizacion = models.ForeignKey(Cotizacion, on_delete=CASCADE, verbose_name='cotizacion')
    item = models.ManyToManyField(Item, verbose_name='item')

    class Meta:
        ordering = ('-creado',)
        verbose_name = _('Detalle de Cotización')
        verbose_name_plural = _('Detalles de Cotización')

    @property
    def monto(self):
        return self.cantidad * self.precio

    @monto.setter
    def monto(self, value):
        self._monto = value

    @property
    def total(self):
        return self.monto / (1 - self.markup)

    @total.setter
    def total(self, value):
        self._total = value

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_cotizaciondetalle_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cotizaciondetalle_update', args=(self.slug,))


class Vehiculo(models.Model):
    # Fields
    nombre = models.CharField(max_length=5)
    placa = models.CharField(max_length=10)
    chofer_fijo = BooleanField()
    fecha_adquirido = models.DateField(null=True, blank=True)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    tipo = models.ForeignKey(TipoDeVehiculo, on_delete=CASCADE, verbose_name='tipo', related_name='vehiculos')

    class Meta:
        ordering = ('-creado',)

    def __unicode__(self):
        return u'%s' % self.nombre

    @property
    def tipo_nombre(self):
        return self.tipo.nombre

    @property
    def costo_por_dia(self):
        return self.tipo.costo_por_dia

    @property
    def costo_por_km(self):
        return self.tipo.costo_por_km

    @property
    def capacidad_nominal(self):
        return self.tipo.capacidad_nominal

    @property
    def capacidad_real(self):
        return self.tipo.capacidad_real

    def get_absolute_url(self):
        return reverse('transporte_vehiculo_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_vehiculo_update', args=(self.slug,))


class Lugar(models.Model):
    # Fields
    codigo = models.CharField(max_length=3, unique=True)
    slug = extension_fields.AutoSlugField(populate_from='codigo', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_lugar_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_lugar_update', args=(self.slug,))


class Tramo(models.Model):
    # Relationship Fields
    desde_lugar = models.ManyToManyField(Lugar, verbose_name='desde', related_name='desde')
    hacia_lugar = models.ManyToManyField(Lugar, verbose_name='hacia', related_name='hacia')

    # Fields
    nombre = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='codigo', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)
    codigo = models.TextField(max_length=7)
    desde_hacia = models.TextField(max_length=100)
    kms = models.IntegerField()
    hrs = models.DecimalField(max_digits=4, decimal_places=1)
    codigo_desde = models.CharField(max_length=7)
    codigo_hacia = models.CharField(max_length=7)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_tramo_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_tramo_update', args=(self.slug,))


class Conductor(models.Model):
    # Fields
    nombre = models.CharField(max_length=30)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)
    identidad = models.TextField(max_length=13)
    telefono = models.TextField(max_length=13)
    empleado = models.BooleanField()
    incentivo_por_dia = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('transporte_conductor_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_conductor_update', args=(self.slug,))
