from django.core.exceptions import ValidationError
from decimal import Decimal

def validate_amount_of_product_collection(product:object, amount:Decimal, measure:int)->None:
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
        PEACE: 1,
    } 
    product_amount = measure_values[product.measure] * product.amount_in_stock
    collection_amount = measure_values[measure] * amount

    if product_amount < collection_amount:
        raise ValidationError(f"This product's amount in stock is {product.amount_in_stock} {product.get_measure_name()}")
    

def validate_product_collection(collection: object):
    if not collection.is_exists:
        raise ValidationError(f"{collection} is already used")