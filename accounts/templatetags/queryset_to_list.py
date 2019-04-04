from django import template

register = template.Library()


@register.filter(name='_list')
def to_list(value):
    return list(value)
