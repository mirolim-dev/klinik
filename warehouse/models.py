from django.db import models
from django.db.models import F, Sum
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# from local
from hr_management.models import Staff
# from .validators import validate_measure_type
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
        return f"{self.product.name} | {self.amoun} {self.measure}"
    
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

