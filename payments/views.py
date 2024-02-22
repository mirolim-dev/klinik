from django.shortcuts import render, get_object_or_404


from .models import Invoice, InvoiceService
# Create your views here.

def single_invoice_view(request, invoice_id:int):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    context = {
        'invoice': invoice,
    }
    return render(request, 'payments/single_invoice.html', context)