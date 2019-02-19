from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, alteration):
    return value.replace(alteration, ' ')
