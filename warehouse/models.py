from django.db import models

# Create your models here.
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

    CHOICES = (
        (MILLIGRAMM, 'MilliGramm'),
        (GRAMM, 'Gramm'),
        (KILOGRAMM, 'KiloGramm'),
        (TON, 'Ton'),
        (MILLILITER, 'MilliLiter'),
        (LITER, 'Liter'),
        (PEACE, 'Peace'),
    )

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

