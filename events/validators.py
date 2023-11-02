from django.core.exceptions import ValidationError

def validate_consultant(value):
    # (1, "Senior"),
    # (2, "Consultant"),
    if value.position not in [1, 2]:
        raise ValidationError(
            f"Postion of your consultant doctor is {value.position}\
                It should be one of Consultant or Senior"
        )
    if not value.consultant.staff.working:
        raise ValidationError(
            f"Consultant is not working\
            Consultan should be working(It means consultant shoul be active)"
        )
