from django.db import models
from django.db.models import F, Sum
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
import random
import string

# from local
from hr_management.models import Staff
from hr_management.utils import generate_barcode, generate_barcode_data
from hr_management.validators import validate_staff_is_working

from departments.models import DepartmentStorage
from .validators import (
    validate_amount_of_product_collection, 
    validate_product_collection,
    validate_barcode_data)
from .utils import calculate_product_amount
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

    def get_measure_name(self)->str:
        return MeasureChoices.CHOICES[self.measure][1]


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
    barcode_data = models.CharField(max_length=13, editable=False, unique=True)
    barcode_file = models.ImageField(upload_to='products_collection/barcodes/', editable=False)
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} | {self.barcode_data}"

    def clean(self) -> None:
        validate_measure_type(self.product, self.measure)
        validate_amount_of_product_collection(self.product, self.amount, self.measure)
        super().clean()

    def save(self, *args, **kwargs):
        """Method is being handled because of barcode_data and 
            barcode_file_path should be created automatically""" 
        if not self.pk:#checking is object creating or updating
            self.barcode_data = generate_barcode_data("123")
            # 123 is for making different ProductCollections' barcode data from Staff's barcode data
            while True:
                try:
                    break
                except ValidationError:
                    pass
            self.barcode_file_path = f"media/products_collection/barcodes/"
            generate_barcode(self.barcode_data, self.barcode_file_path)
        super().save(*args, **kwargs)


class ProductUsage(models.Model):
    for_storage = models.ForeignKey(DepartmentStorage, on_delete=models.CASCADE, null=True)
    collections = models.ManyToManyField(ProductsCollection)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.get_full_name()}"

    def clean(self) -> None:
        validate_staff_is_working(self.staff)
        return super().clean()
    # class Meta:
    #     unique_together = 


class ProductInStorage(models.Model):
    storage = models.ForeignKey(DepartmentStorage, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    measure = models.IntegerField(choices=MeasureChoices.CHOICES, default=2)
    
    def __str__(self):
        return f"{self.product.name} | {self.amount} {self.meas}"