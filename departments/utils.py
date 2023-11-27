from decimal import Decimal

# from warehouse.models import MeasureChoices

def calculate_product_amount_in_storage(amount_in_storage:Decimal, measure_in_storage:str, 
                                amount_of_incoming_product:Decimal, measure_of_incoming_product):
    MILLIGRAMM = 0
    GRAMM = 1
    KILOGRAMM = 2
    TON = 3
    MILLILITER = 4
    LITER = 5
    PEACE = 6

    measure_values = {
        MILLIGRAMM: 1,
        GRAMM: 10**3,
        KILOGRAMM: 10**6,
        TON: 10**9,
        MILLILITER: 1,
        LITER: 10**3,
        PEACE:1,
    }
    total_amount, result_measure = 0, measure_in_storage
    if measure_of_incoming_product == measure_in_storage:
        total_amount = amount_in_storage + amount_of_incoming_product
    elif measure_in_storage > measure_of_incoming_product:
        total_amount = amount_in_storage * \
            (measure_values[measure_in_storage]/measure_values[measure_of_incoming_product])\
            +measure_of_incoming_product
        result_measure = measure_of_incoming_product
    else:
        total_amount = amount_of_incoming_product * \
            (measure_values[measure_of_incoming_product]/measure_values[measure_in_storage])\
            +measure_in_storage
        result_measure = measure_in_storage
    return (total_amount, result_measure)

