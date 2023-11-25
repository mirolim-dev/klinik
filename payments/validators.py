from django.core.exceptions import ValidationError

# def validate_payment_invoice(value):
#     print(f"Value: {value}")
#     not_valid_invoice_statuses = {
#         3: 'Done',
#         4: 'Cancelled',
#         5: 'Expired'
#     }
#     if value in not_valid_invoice_statuses.keys():
#         raise ValidationError(f"The invoice status({not_valid_invoice_statuses[value]}) is not valid")