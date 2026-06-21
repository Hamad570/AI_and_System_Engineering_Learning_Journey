# checker/urls.py
from django.urls import path
from .views import CheckWhatsAppNumber, index_page

urlpatterns = [
    path('', index_page, name='index'),  # One-page frontend html render kre ga
    path('api/check-number/', CheckWhatsAppNumber.as_view(), name='check_number'), # API Endpoint
]