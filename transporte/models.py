from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models as models
from django.db.models import *
from django.utils.translation import ugettext as _
from django_extensions.db import fields as extension_fields
from djchoices import DjangoChoices, ChoiceItem


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
    activo = BooleanField(default=True)
    creado = DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Vehículo')
        verbose_name_plural = _('Vehículos')

    def __str__(self):
        return self.nombre

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
        ordering = ['orden', ]
        verbose_name = _('Parámetro')
        verbose_name_plural = _('Parámetros')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_parametro_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_parametro_update', args=(self.slug,))


class Item(models.Model):
    # Choices
    class TipoItem(DjangoChoices):
        Insumo = ChoiceItem("INS")
        Servicio = ChoiceItem("SER")
        Subcontratado = ChoiceItem("SUB")
        Cargo = ChoiceItem("CAR")
        Descuento = ChoiceItem("DES")
        Impuesto = ChoiceItem("IMP")
        Grupo = ChoiceItem("GRU")

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    tipo_item = models.CharField(max_length=3, choices=TipoItem.choices, validators=[TipoItem.validator], default='SER')
    unidad = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
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
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_item_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_item_update', args=(self.slug,))


class NivelDePrecio(models.Model):
    # Choices
    class Tipo(DjangoChoices):
        Porcentaje = ChoiceItem("FI")
        Valor = ChoiceItem("VA")

    class Accion(DjangoChoices):
        Incrementa = ChoiceItem("INC")
        Decrementa = ChoiceItem("DEC")

    # Fields
    nombre = models.CharField(max_length=50)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    tipo = models.CharField(max_length=2, choices=Tipo.choices, validators=[Tipo.validator], default=Tipo.Porcentaje)
    accion = models.CharField(max_length=3, choices=Accion.choices, validators=[Accion.validator],
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
        return u'%s' % self.slug

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
    cliente_niveldeprecio = models.ForeignKey(NivelDePrecio, verbose_name='nivel de precio', on_delete=models.PROTECT)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_cliente_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_cliente_update', args=(self.slug,))


class Itinerario(models.Model):
    # estatus opciones
    class Status(DjangoChoices):
        Solicitado = ChoiceItem("SOL")
        Cotizado = ChoiceItem("COT")
        Confirmado = ChoiceItem("CON")
        Facturado = ChoiceItem("FAC")

    # Fields
    nombre = models.CharField(max_length=100)
    slug = extension_fields.AutoSlugField(populate_from='nombre', blank=True)
    fecha_desde = models.DateField(verbose_name='inicia')
    fecha_hasta = models.DateField(verbose_name='termina')
    estatus = models.CharField(max_length=3, choices=Status.choices, validators=[Status.validator],
                               default=Status.Solicitado)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    itinerario_cliente = models.ForeignKey(Cliente, on_delete=CASCADE, verbose_name='cliente')

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Itinerario')
        verbose_name_plural = _('Itinerarios')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('transporte_itinerario_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('transporte_itinerario_update', args=(self.slug,))


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
    cotizacion_itinerario = models.ForeignKey(Itinerario, on_delete=CASCADE, verbose_name='itinerario')

    class Meta:
        ordering = ('-id',)
        verbose_name = _('Cotización')
        verbose_name_plural = _('Cotizaciones')

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%s' % self.slug

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
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    detalle_cotizacion = models.ForeignKey(Cotizacion, on_delete=CASCADE, verbose_name='cotizacion')
    detalle_item = models.ManyToManyField(Item, verbose_name='item')

    class Meta:
        ordering = ('-created',)
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
