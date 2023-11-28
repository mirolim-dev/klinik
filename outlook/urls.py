from django.urls import path

from .views import (
    home_view, dash_home1,
    )


urlpatterns = [
    path('', home_view, name='home'),
    path('dash/', dash_home1, name='dash1'),
]