from django.core.exceptions import ValidationError

class InsuranceFieldsValidator:
    def __call__(self, value):
        insurance_provider = value.insurance_provider
        insurance_policy_number = value.insurance_policy_number

        if bool(insurance_provider) != bool(insurance_policy_number):
            raise ValidationError("Either both 'insurance_provider' and 'insurance_policy_number' must be provided or both should be empty.")


def validate_insurance_fields(value):
    print(value)
    """
        checking_fields:
            insurance_provider,
            insurance_policy_number
        explaination:
            this function checks both fields are exist together or not.
            if both fields exist together or don't exist together function works good
            if one of fields exists and another one doesn't exist it raises ValidationError
    """
    if bool(value.insurance_provider) != bool(value.insurance_policy_number):
        raise ValidationError("Either both 'insurance_provider' and 'insurance_policy_number' \
            must be provided or both should be empty.")
    