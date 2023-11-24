from django.contrib import admin

# from local
from .models import (
    Product, ProductsCollection, 
    ProductUsage, Order, OrderItem, 
    Supplier, Section, ItemCategory
    )
# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_number', 
            'contact_person', 'address', 'created_at']
admin.site.register(Supplier, SupplierAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Section, SectionAdmin)


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'section', 'name']
admin.site.register(ItemCategory, ItemCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 
        'unit_price', 'amount_in_stock', 'measure',
        'location']
admin.site.register(Product, ProductAdmin)


class ProductUsageAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'taken_at']
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     form.save_m2m()  # This will save the many-to-many fields
    #     obj.clean_collections()  # Now you can use many-to-many fields
admin.site.register(ProductUsage, ProductUsageAdmin)


class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'measure', 
        'usable_till', 'is_exists']
admin.site.register(ProductsCollection, ProductCollectionAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'status', 'created_at']
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 
        'amount', 'measure', 'usable_till']
admin.site.register(OrderItem, OrderItemAdmin)