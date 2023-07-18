from django import template
register = template.Library()


@register.filter
def mult(val, arg):
    return val * arg
