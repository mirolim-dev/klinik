from django import template

register = template.Library()

@register.filter
def display_invoice_service_name():
    pass