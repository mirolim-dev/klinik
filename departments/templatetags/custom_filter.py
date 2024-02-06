from django import template

register = template.Library()

@register.filter
def display_position(position):
    POSITION_CHOICES = (
        (0, "Junior"),
        (1, "Senior"),
        (2, "Consultant"),
        (3, "Surgeon"),
        (4, "Head Doctor"),
    )
    return dict(POSITION_CHOICES).get(position, '')


@register.filter
def display_gender(position):
    GENDER_CHOICES = (
        (0, "Female"),
        (1, "Male"),
    )
    return dict(GENDER_CHOICES).get(position, '')

@register.filter
def display_currency(position):
    CURRENCY_CHOICES = (
        (0, 'UZS'),
        (1, 'USD'),
        (2, 'EUR')
    )
    return dict(CURRENCY_CHOICES).get(position, '')