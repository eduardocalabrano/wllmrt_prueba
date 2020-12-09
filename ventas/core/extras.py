from django import template

register = template.Library()

@register.filter
def calcular_precio_descuento(value):
    try:
        value = int(value)
        value = value * 0.5
    except Exception as e:
        print('EXCEPTION {}'.formart(str(e)))
        pass
    return int(value)
