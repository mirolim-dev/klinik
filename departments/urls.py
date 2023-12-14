from django.urls import path

from .views import (
    main_index, department_detail,
    main_index2,
)

urlpatterns = [
    path('main/', main_index, name='main_index'),
    path('main/2', main_index2, name='main_index2'),
    path('detail/<int:pk>/', department_detail, name='detail-department'),
]