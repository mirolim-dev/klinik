from django.urls import path

from .views import (
    main_index,
)

urlpatterns = [
    path('main/', main_index, name='main_index'),
]