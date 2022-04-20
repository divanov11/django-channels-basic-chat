import json
from channels.generic.websocket import AsyncWebsocketConsumer
from uvicorn import main
from .models import *

class LedgerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        uuid=self.scope['url_route']['kwargs']['user_id']
        # print(uuid)
        self.room_group_name = f'{uuid}'
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name)
        await self.accept()
        await self.send('connected to the server')

    async def receive(self, text_data):
        print(text_data,'--------------------------')
        text_data_json = json.loads(text_data)
        # print(text_data_json,'1111111111111111111111')
        # main=text_data_json['res']['config']['data']
        # main1=json.loads(text_data_json)
        main1=text_data_json
        message = main1
        await self.channel_layer.group_send(
        self.room_group_name,
        {   'type':'send_message',
            'message': message,
        })

    async def send_message(self, event):    
        await self.send(text_data=json.dumps({
            'message':event['message']
        }))

    # async def disconnect(self, event):
    #     await self.disconnect("LedgerConsumer has been disconnected")


class BankVoucherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        uuid=self.scope['url_route']['kwargs']['user_id']
        print(uuid)
        self.room_group_name = f'{uuid}'
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name)
        await self.accept()
        await self.send('connected to the server')

    async def receive(self, text_data):
        print(text_data,'+++++++++++++++++++++++')
        text_data_json = json.loads(text_data)
        print(text_data_json,'2222222222222222222222')
        # main=text_data_json['res']['config']['data']
        main1=text_data_json
        message = main1
        await self.channel_layer.group_send(
        self.room_group_name,
        {   'type':'send_message',
            'message': message,
        })

    async def send_message(self, event):    
        await self.send(text_data=json.dumps({
            'message':event['message']
        }))

    # async def disconnect(self):
    #     await self.disconnect("BankVoucherConsumer has been disconnected")


class InvoiceVoucherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        uuid=self.scope['url_route']['kwargs']['user_id']
        print(uuid)
        self.room_group_name = f'{uuid}'
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name)
        await self.accept()
        await self.send('connected to the server')

    async def receive(self, text_data):
        print(text_data,'************************')
        text_data_json = json.loads(text_data)
        print(text_data_json,'33333333333333333333333')
        # main=text_data_json['res']['config']['data']
        main1=text_data_json
        message = main1
        await self.channel_layer.group_send(
        self.room_group_name,
        {   'type':'send_message',
            'message': message,
        })

    async def send_message(self, event):    
        await self.send(text_data=json.dumps({
            'message':event['message']
        }))

    # async def disconnect(self):
    #     await self.disconnect("InvoiceVoucherConsumer has been disconnected")

        