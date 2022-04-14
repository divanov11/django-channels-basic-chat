# from django.urls import re_path 
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/socket-server/<str:user_id>/', consumers.ChatConsumer.as_asgi())
    path(r'ws/socket-server/<str:user_id>/', consumers.ChatConsumer.as_asgi())
]