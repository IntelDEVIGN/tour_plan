from django.core.urlresolvers import reverse
from django.db.models import *
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Bus(models.Model):

    # Fields
    nombre = CharField(max_length=20)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    rendimiento = IntegerField()
    costo_por_dia = DecimalField(max_digits=10, decimal_places=2)
    costo_por_km = DecimalField(max_digits=10, decimal_places=2)
    capacidad_nominal = IntegerField()
    capacidad_real = IntegerField()
    chofer_fijo = BooleanField()
    creado = DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_bus_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_bus_update', args=(self.slug,))


class Parametro(models.Model):

    # Fields
    nombre = CharField(max_length=25)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    valor = CharField(max_length=100)
    unidad = CharField(max_length=100)
    orden = IntegerField(default=0)
    creado = DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_parametro_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_parametro_update', args=(self.slug,))


class Item(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    unidad = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_compra = models.CharField(max_length=50)
    descripcion_venta = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    tipo_item = models.ForeignKey('transporte.Tipo_Item', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_item_update', args=(self.slug,))


class Tipo_Item(models.Model):

    # Fields
    nombre = models.CharField(max_length=50)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_tipo_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_tipo_item_update', args=(self.slug,))


class Nivel_De_Precio(models.Model):

    # Fields
    nombre = models.CharField(max_length=50)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    tipo = models.CharField(max_length=30)
    accion = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_nivel_de_precio_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_nivel_de_precio_update', args=(self.slug,))


class Cotizacion(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    fecha_vence = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    markup = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    cotizacion_itinerario = models.ForeignKey('transporte.Itinerario', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_cotizacion_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cotizacion_update', args=(self.slug,))


class Cliente(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    cliente_nivel_de_precio = models.ForeignKey('transporte.Nivel_De_Precio', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_cliente_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cliente_update', args=(self.slug,))


class Itinerario(models.Model):

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    estatus = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    itinerario_cliente = models.ForeignKey('transporte.Cliente', )

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_itinerario_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_itinerario_update', args=(self.slug,))


class Cotizacion_Detalle(models.Model):

    # Fields
    descripcion = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    markup = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    detalle_cotizacion = models.ForeignKey('transporte.Cotizacion', )
    detalle_item = models.ManyToManyField('transporte.Item', )

    class Meta:
        ordering = ('-created',)

    @property
    def monto(self):
        return self.cantidad * self.precio

    @property
    def total(self):
        return self.monto / (1 - self.markup)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_cotizacion_detalle_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cotizacion_detalle_update', args=(self.slug,))


