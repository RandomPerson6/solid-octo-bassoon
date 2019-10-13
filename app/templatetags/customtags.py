from django import template
register = template.Library()

@register.filter
def substract(var, arg):
    return var - arg
