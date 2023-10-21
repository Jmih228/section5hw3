from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def mediapath(object_title):
    return mark_safe(f'/media/{object_title}')

@register.simple_tag()
def mediapath_tag(object_title):
    return f'/media/{object_title}'
