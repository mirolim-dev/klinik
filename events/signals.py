from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .consulting_models import ConsultingPatientUsage, DiagnozPatientUsage

@receiver(post_save, sender=ConsultingPatientUsage)
def create_diagnoz_patient_usage_by_consulting(sender, instance, **kwargs):
    print('Signal working from events', instance.status)
    if instance.status in [1, 2, 3]:
        required_diagnoses = instance.required_diagnoses.all()
        print(f"reuqired Digonses", required_diagnoses)
        diagnoz_patient_usage_list = [
            DiagnozPatientUsage(
                patient=instance.patient,
                diagnoz=diagnose,
                consulting_patient_usage=instance,
                status=1,
            )
            for diagnose in required_diagnoses
        ]
        print(diagnoz_patient_usage_list)
        DiagnozPatientUsage.objects.bulk_create(diagnoz_patient_usage_list)