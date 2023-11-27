from django.db.models.signals import pre_save, post_save, m2m_changed
#from django.db.models.signals import 
from django.dispatch import receiver
# from local
from .models import Order, OrderItem, Product, ProductUsage, ProductsCollection
from .utils import calculate_product_amount
from .validators import validate_product_collection
from .models import ProductInStorage
from departments.utils import calculate_product_amount_in_storage

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
        # update_product_amount_in_stock(instance)
        for collection in instance.collections.all():
            validate_product_collection(collection)
            update_product_in_storage_amount(instance, collection)
            product = collection.product
            product.amount_in_stock, product.measure = calculate_product_amount(
                product, collection.amount, collection.measure, False)
            print(product.amount_in_stock, product.measure)
            product.save()
            collection.is_exists = False
            collection.save()


# @receiver(post_save, sender=ProductUsage)
def update_product_in_storage_amount(instance, collection):
    # if created:
    if ProductInStorage.objects.filter(product=collection.product).exists():
        product_in_storage = ProductInStorage.objects.get(product=collection.product)
        product_in_storage.amount, product_in_storage.measure = \
            calculate_product_amount_in_storage(
                product_in_storage.amount, product_in_storage.measure,
                collection.amount, collection.measure)
        product_in_storage.save()
    else:
        ProductInStorage.objects.create(
            storage = instance.for_storage,
            product=collection.product,
            amount = collection.amount,
            measure = collection.measure,
        )