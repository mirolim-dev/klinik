from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

def validate_insurance_fields(insurance_provider, insurance_policy_number):
    # print(value)
    """
        checking_fields:
            insurance_provider,
            insurance_policy_number
        explaination:
            this function checks both fields are exist together or not.
            if both fields exist together or don't exist together function works good
            if one of fields exists and another one doesn't exist it raises ValidationError
    """
    if bool(insurance_provider) != bool(insurance_policy_number):
        raise ValidationError("Either both 'insurance_provider' and 'insurance_policy_number' \
            must be provided or both should be empty.")
    

def validate_available_time(from_time, to):
    """Checks available times. If 'from_time' 
        field lower then 'to' field works good 
        else raises Validation error"""
    if timedelta(2) <= (to-from_time):
        raise ValidationError("Available time should be more then 2 hours")


def validate_staff_is_vorking(value):
    if not value.working:
        ValidationError("This stuff is not working. Choose another stuff or change working status to True")


def validate_file_type(value):
    valid_extentions = ['jpg', 'jpeg', 'png', 'web', 'pdf', 'doc', 'docx']
    extention = str(value).split('.')[-1].lower()
    if not extention in valid_extentions:
        ValidationError(f"Invalid file extention. Your file's extention should \
                        be one of these valid extentions ({', '.join(valid_extentions)})")

def validate_file_size(value):
    if value.size > 3 * 1024 * 1024:
        return ValidationError(f"Your file size({value.size}) higher. But maximum size shoul be 3MB")