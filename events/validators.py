from django.core.exceptions import ValidationError

def validate_consultant(value):
    # (1, "Senior"),
    # (2, "Consultant"),
    if value.position not in [1, 2]:
        raise ValidationError(
            f"Postion of your consultant doctor is {value.position}\
                It should be one of Consultant or Senior"
        )
    if not value.staff.working:
        raise ValidationError(
            f"Consultant is not working\
            Consultan should be working(It means consultant shoul be active)"
        )

def validate_consulting(value):
    # (0, "Inactive"),
    # (1, 'Active'),
    if value.status == 0:
        raise ValidationError(f"Consulting should be active to choose")

def validate_diagnoz(value):
    # (0, "Inactive"),
    # (1, "Active"),
    if value.status == 0:
        raise ValidationError("Diagnoz status should be active to choose")

def validate_consulting_patient_usage_dpu(value):
    """
        This function validates consulting patient usage for Diagnoz patient usage. 
        If it's status is waiting_daignoses it works good otherwise it raises Validation error 
    """
    # (3, "Waiting diagnoses"),
    if value.status != 3:
        raise ValidationError("Consulting Patient usage status should be Waiting diagnoses")