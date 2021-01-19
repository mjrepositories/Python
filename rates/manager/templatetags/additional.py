# importing template
from django import template

# creating Library as object
register = template.Library()

# adding function as decorator to register object
@register.filter
def additional(value):
    return value.split('/')[-1]