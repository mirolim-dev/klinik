from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from warehouse.models import ProductUsage, ProductsCollection, Product
