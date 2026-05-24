from django.urls import path
from .views import alumni_form

urlpatterns = [
    path('', alumni_form),
]