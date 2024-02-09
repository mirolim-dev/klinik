from django.urls import path

from .views import (
    patient_profile,
)

urlpatterns = [
    path('patient/<int:patient_id>/', patient_profile, name='patient-profile'),
]