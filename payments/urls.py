from django.urls import path

from .views import (
    single_invoice_view,
)
urlpatterns = [
    path('invoice/<int:invoice_id>/', single_invoice_view, name='single-invoice'),
    
]