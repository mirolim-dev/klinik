from decimal import Decimal

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

    dict_data = {
        p_measure: product.amount_in_stock,
        measure: amount,
    }

    total = abs(dict_data[x] * Decimal((MEASURES[x] / MEASURES[y])) + dict_data[y] if is_ordering else dict_data[x] * Decimal((MEASURES[x] / MEASURES[y])) - dict_data[y])
    return (total, y)


# print(calculate_product_amount())