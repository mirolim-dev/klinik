from decimal import Decimal
from django.core.exceptions import ValidationError

def calculate_product_amount(product: object, amount, measure: int, is_ordering: bool)->tuple:
    """
        product: Object of product
        amount: amount of item
        measure: measure of item
        is_ordering: Is item ordering or being taken from warehouse
    """
    MEASURES = {
        0: 1,      # MILLIGRAMM
        1: 10**3,  # GRAMM
        2: 10**6,  # KILOGRAMM
        3: 10**9,  # TON
        4: 1,      # MILLILITER
        5: 10**3,  # LITER
        6: 1       # PEACE
    }

    p_measure = product.measure
    x, y = sorted([p_measure, measure], reverse=True)

    amount_data = {
        p_measure: product.amount_in_stock,
        measure: amount,
    }
    total = 0
    if is_ordering:
        total = amount_data[x]*Decimal(MEASURES[x]/MEASURES[y]) + amount_data[y]
    else:
        total = amount_data[x]*Decimal(MEASURES[x]/MEASURES[y]) - amount_data[y]
        print(total, y)
        
    # total = abs(amount_data[x] * Decimal((MEASURES[x] / MEASURES[y])) + amount_data[y] if is_ordering else amount_data[x] * Decimal((MEASURES[x] / MEASURES[y])) - amount_data[y])
    return (total, y)


# print(calculate_product_amount())