from django.core.exceptions import ValidationError

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
    

            
    