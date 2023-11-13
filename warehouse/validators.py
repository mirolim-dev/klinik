from django.core.exceptions import ValidationError

# from local
# from .models import MeasureChoices
# import timeit
# def amount_calculator(amount1:float, measure1:int, amount2:float, measure2:int)->tuple:
#     MILLIGRAMM = 0
#     GRAMM = 1
#     KILOGRAMM = 2
#     TON = 3
#     MILLILITER = 4
#     LITER = 5
#     PEACE = 6

#     x, y = (measure1, measure2) if measure1 > measure2 else (measure2, measure1)
#     d = {
#         measure1: amount1,
#         measure2: amount2,
#     }
#     measure_values = {
#         MILLIGRAMM: 1,
#         GRAMM: 10**3,
#         KILOGRAMM: 10**6,
#         TON: 10**9,
#         MILLILITER: 1,
#         LITER: 10**3,
#         PEACE: 1,
#     } 

#     total = d[x]*(measure_values[x]/measure_values[y]) + d[y]
#     return (total, y)
    

# amount1 = 19.09
# measure1 = 2
# amount2 = 0.98
# measure2 = 3


# result = amount_calculator(amount1, measure1, amount2, measure2)
# print(result)


# def claculate_product_amount(product:object, amount:float, measure:int, is_ordering:False):
#     MILLIGRAMM = 0
#     GRAMM = 1
#     KILOGRAMM = 2
#     TON = 3
#     MILLILITER = 4
#     LITER = 5
#     PEACE = 6
#     p_measure = product.measure
#     x, y = (p_measure, measure) if p_measure > measure else (measure, p_measure)
#     dict_data = {
#         p_measure: product.amount_in_stock,
#         measure: amount,
#     }
#     measure_values = {
#         MILLIGRAMM: 1,
#         GRAMM: 10**3,
#         KILOGRAMM: 10**6,
#         TON: 10**9,
#         MILLILITER: 1,
#         LITER: 10**3,
#         PEACE: 1,
#     } 
#     total = 0
#     if is_ordering:
#         total = dict_data[x]*(measure_values[x]/measure_values[y]) + dict_data[y]
#     else:
#         total = dict_data[x]*(measure_values[x]/measure_values[y]) - dict_data[y]
#     return (total, y)


