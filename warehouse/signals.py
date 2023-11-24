from django.db.models.signals import pre_save, post_save, m2m_changed
#from django.db.models.signals import 
from django.dispatch import receiver
# from local
from .models import Order, OrderItem, Product, ProductUsage, ProductsCollection
from .utils import calculate_product_amount
from .validators import validate_product_collection

@receiver(post_save, sender=OrderItem)
def update_product_amount_in_stock(sender, instance, created, **kwargs):
    """Updates Product's amount in stock after OrderItem or ProductUsage added"""
    if created:
        # print("Signal working")
        product = instance.product
        amount = instance.amount
        measure = instance.measure
        product.amount_in_stock, product.measure = calculate_product_amount(product, amount, measure, True)
        product.save()


@receiver(m2m_changed, sender=ProductUsage.collections.through)
def update_product_amount_in_stock(sender, instance, action, **kwargs):
    """Updates Product's amount in stock after ProductUsage product_collections are added"""
    if action == "post_add":
        # print("Signal working", instance.collections.all())
        for collection in instance.collections.all():
            validate_product_collection(collection)
            product = collection.product
            product.amount_in_stock, product.measure = calculate_product_amount(
                product, collection.amount, collection.measure, False)
            print(product.amount_in_stock, product.measure)
            product.save()
            collection.is_exists = False
            collection.save()