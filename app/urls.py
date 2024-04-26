# urls.py
from django.urls import path
from .views import upload_invoice, validate_invoice, extract_data

urlpatterns = [
    path('upload/', upload_invoice, name='upload_invoice'),
    path('validate/<int:invoice_id>/', validate_invoice, name='validate_invoice'),
    path('extract/<int:invoice_id>/', extract_data, name='extract_data'),
]
