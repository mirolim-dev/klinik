from django.urls import path

from .views import (
    main_index, department_detail,
    main_index2, show_all_patients_by_department,
    search_patients,
)

urlpatterns = [
    path('main/', main_index, name='main_index'),
    path('main/2', main_index2, name='main_index2'),
    path('detail/<int:pk>/', department_detail, name='detail-department'),
    path('<int:department_id>/show_patients/', show_all_patients_by_department, name='show-patients-by-department'),
    path('departent/<int:department_id>/search_patients/', search_patients, name="search_patients_in_department"),
]