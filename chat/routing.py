from django.urls import re_path
from django.urls import path
from . import consumers

websocket_urlpatterns = [

    path('ws/ledger-socket-server/<str:user_id>/', consumers.LedgerConsumer.as_asgi()),
    
    # ------------------------New Url------------------------------

    path('ws/voucher-socket-server/<str:user_id>/', consumers.BankVoucherConsumer.as_asgi()),
    path('ws/invoice-socket-server/<str:user_id>/', consumers.InvoiceVoucherConsumer.as_asgi()),
]