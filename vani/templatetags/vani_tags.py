from django import template

register = template.Library()

@register.filter(name='lastValue')
def lastValue(value):
    return value.split('/')[-2]
