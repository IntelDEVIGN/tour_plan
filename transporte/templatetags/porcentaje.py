from django import template

register = template.Library()


@register.filter
def porciento(numero):
    return format(numero, "%")


register.simple_tag(porciento, takes_context=True)
