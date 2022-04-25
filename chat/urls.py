from django.urls import path 
from . import views 

urlpatterns = [
    path('lobby/', views.lobby),
    path('l/', views.ledgerData),
    path('v/', views.voucherData),
    path('i/', views.invoiceData),
]