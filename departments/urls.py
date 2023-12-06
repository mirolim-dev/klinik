from django.urls import path

from .views import (
    main_index, department_detail,
)

urlpatterns = [
    path('main/', main_index, name='main_index'),
    path('detail/<int:pk>/', department_detail, name='detail-department'),
]