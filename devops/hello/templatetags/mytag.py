from django import template
register = template.Library()

@register.filter
def sum(x,y):
    return int(x) + int(y)