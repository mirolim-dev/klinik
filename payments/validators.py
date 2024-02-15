from django.core.exceptions import ValidationError
from .models import Invoice

def validate_invoice_to_create(patient):
    """
    Checks has patient got previouse active(status=pending or partly paid) invoice
    If patient has this kind of Invoice already. function raises error

    So if Patient has active Invoice he/she should fully pay for it
    before creating new Invoice
    """
    #statuses ((1, 'Pending'), (2, 'Partly paid'))
    invoices = patient.get_all_invoices().filter(status__in=[1, 2])
    if invoices.exists():
        message = f"Patient has active Invoice. He/She should fully pay for it to create \
            new Invoice"
        raise ValidationError(message)
    

def validate_invoice_to_update(object_pk:int, new_status:int):
    """
    This validation:
    1) Doesn't allow to change back Invoices status to Pending
    2) Doesn't allow to complete(changing status to Done) before residual_amount = 0
    """
    invoice = Invoice.objects.get(pk=object_pk)
    old_status = invoice.status
    if old_status != new_status:
        if new_status == 1:
            raise ValidationError(f"Changing invoice's status to Pending is not allowed.")
        elif new_status == 3 and invoice.residual_amount > 0:
            raise ValidationError(f"This invoice has {invoice.residual_amount}. Patient should pay this amount first to complete Invoice")
            
    