I created my signals in a new signals.py file and I iported it in my apps.py file But my signal is not working.
Could anybody help me.?
my signals.py file's location is like this
[![image](https://private-user-images.githubusercontent.com/109344886/282394828-e7415764-8f81-4b81-b74c-c72857d2934a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk4NjI4NTQsIm5iZiI6MTY5OTg2MjU1NCwicGF0aCI6Ii8xMDkzNDQ4ODYvMjgyMzk0ODI4LWU3NDE1NzY0LThmODEtNGI4MS1iNzRjLWM3Mjg1N2QyOTM0YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTExM1QwODAyMzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMjVmZDcxNjQ3NjFlOTgzOWM5ZGU3MzEzNzIyNTA3YTAxZjBhYWU2ZGJhNjZiY2FkN2FmNTUwZDliYTIzMzYxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.I90IpF9pysHDZQuNYjejrB1jPRZye2HBO0ygVX-M4Y4)](https://private-user-images.githubusercontent.com/109344886/282394828-e7415764-8f81-4b81-b74c-c72857d2934a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTk4NjI4NTQsIm5iZiI6MTY5OTg2MjU1NCwicGF0aCI6Ii8xMDkzNDQ4ODYvMjgyMzk0ODI4LWU3NDE1NzY0LThmODEtNGI4MS1iNzRjLWM3Mjg1N2QyOTM0YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTExM1QwODAyMzRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kMjVmZDcxNjQ3NjFlOTgzOWM5ZGU3MzEzNzIyNTA3YTAxZjBhYWU2ZGJhNjZiY2FkN2FmNTUwZDliYTIzMzYxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.I90IpF9pysHDZQuNYjejrB1jPRZye2HBO0ygVX-M4Y4)

my [signals](https://github.com/mrdjangodev/klinik/blob/main/warehouse/signals.py)

```python
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
```

my [apps.py ](https://github.com/mrdjangodev/klinik/blob/main/warehouse/apps.py)file:

```python
from django.apps import AppConfig


class WarehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'warehouse'

    def ready(self) -> None:
        import warehouse.signals
```

my [models.py ](https://github.com/mrdjangodev/klinik/blob/main/warehouse/models.py)file:

```python
from django.db import models
from django.db.models import F, Sum
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# from local
from hr_management.models import Staff
# from .validators import validate_measure_type
# from .utils import calculate_product_amount
# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=17)
    contact_person = models.CharField(max_length=150, help_text="Person's Full name in here")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_all_orders(self):
        """Returns all orders belonging to Supplier"""
        return self.order_set.select_related('product')


class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

 
class ItemCategory(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
  

class MeasureChoices:
    MILLIGRAMM = 0
    GRAMM = 1
    KILOGRAMM = 2
    TON = 3
    MILLILITER = 4
    LITER = 5
    PEACE = 6

    measure_types = {
        'weight': [MILLIGRAMM, GRAMM, KILOGRAMM, TON],
        'volume': [MILLILITER, LITER],
        'peace': [PEACE],
    }

    CHOICES = (
        (MILLIGRAMM, 'MilliGramm'),
        (GRAMM, 'Gramm'),
        (KILOGRAMM, 'KiloGramm'),
        (TON, 'Ton'),
        (MILLILITER, 'MilliLiter'),
        (LITER, 'Liter'),
        (PEACE, 'Peace'),
    )

def validate_measure_type(product:object, measure:int):
    measures = MeasureChoices.measure_types[product.get_measure_type()]
    if measure not in measures:
        raise ValidationError(f"measure should be one of these {measures}")

class Product(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    unit_price = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    amount_in_stock = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    measure = models.IntegerField(choices=MeasureChoices.CHOICES, default=2)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
  
    def __str__(self)->str:
        return self.name

    def get_measure_type(self):
        for measure_type, measures in MeasureChoices.measure_types.items():
            if self.measure in measures:
                return measure_type
        return None


class Order(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Shipping'),
        (3, 'Delivered'),
        (4, 'Cancelled'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.supplier.name

    def get_all_items(self):
        return self.orderitem_set.select_related('order', 'product')
  
    def get_total_price(self):
        total_price = self.orderitem_set.aggregate(
            total=Sum(F('amount') * F('product__unit_price'))
        )['total']
  
        return total_price or 0
  

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    measure = models.IntegerField(choices=MeasureChoices.CHOICES, default=2)
    usable_till = models.DateField(null=True)

    def __str__(self):
        return f"{self.product.name} | {self.amount} {self.measure}"
  
    def clean(self) -> None:
        super().clean()
        validate_measure_type(self.product, self.measure)

  
class ProductsCollection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    measure = models.IntegerField(choices=MeasureChoices.CHOICES, default=1)
    usable_till = models.DateField()
    barcode_data = models.CharField(max_length=11)
    barcode_file = models.ImageField(upload_to='products_collection/barcodes/')
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} | {self.barcode_data}"

    def clean(self) -> None:
        super().clean()
        validate_measure_type(self.product, self.measure)


class ProductUsage(models.Model):
    product_collections = models.ManyToManyField(ProductsCollection)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_collections.count()} | {self.staff.get_full_name()}"
```
