from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
# from local
from .models import Order, OrderItem, Product, ProductUsage
from .utils import calculate_product_amount

# @receiver(post_save, sender=OrderItem)
# def update_product_amount_in_stock(sender, instance, created, **kwargs):
#     """Updates Product's amount in stock after OrderItem added"""
#     product = sender.product
#     product.amount_in_stock, product.measure = calculate_product_amount(product, \
#         sender.amount, sender.measure, True)
#     product.save()


# @receiver(post_save, sender=ProductUsage)
# def update_product_amount_in_stock(sender, instance, created, **kwargs):
#     """Updates Product's amount in stock after ProductUsage added"""
#     product = sender.product_collections.product
#     product.amount_in_stock, product.measure = calculate_product_amount(product, \
#         sender.product_collections.amount, sender.product_collections.measure, False)
#     product.save()

@receiver(post_save, sender=[OrderItem, ProductUsage])
def update_product_amount_in_stock(sender, instance, created, **kwargs):
    """Updates Product's amount in stock after OrderItem or ProductUsage added"""
    product = instance.product_collections.product if isinstance(instance, ProductUsage) else instance.product
    amount = instance.product_collections.amount if isinstance(instance, ProductUsage) else instance.amount
    measure = instance.product_collections.measure if isinstance(instance, ProductUsage) else instance.measure
    is_order_item = isinstance(instance, OrderItem)

    product.amount_in_stock, product.measure = calculate_product_amount(product, amount, measure, is_order_item)
    product.save()