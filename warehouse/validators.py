from django.core.exceptions import ValidationError

# from local
from .models import MeasureChoices


def validate_measure_type(product:object, measure:int):
    measures = MeasureChoices.measure_types[product.get_measure_type()]
    if measure not in measures:
        raise ValidationError(f"measure should be one of these {measures}")
