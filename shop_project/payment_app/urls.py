from django.urls import path
from .views import *

urlpatterns = [
    path('checkout',CheckoutView.as_view(), name='checkout'),
    path('sslc/status', sslc_status, name='status'),
    path('sslc/complete/<val_id>/<tran_id>/', sslc_complete, name='sslc-complete'),
]