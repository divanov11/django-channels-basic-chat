import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from matplotlib.font_manager import json_dump
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        uuid=self.scope['url_route']['kwargs']['user_id']
        print(uuid)

        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name)

        await self.accept()
        await self.send('connected to the server')
 
    async def receive(self, text_data):        
            print(text_data, "----------------")

            text_data_json = json.loads(text_data)
            print(text_data_json, "****************")

            main = text_data_json['res']['config']['data']
            main1 = json.loads(main)
            message={}

            message['ledeger_name']=main1['ledeger_name']
            message['ledeger_state']=main1['ledeger_state']
            message['ledeger_website']=main1['ledeger_website']

            await self.channel_layer.group_send(
            self.room_group_name,
            {   'type':'send_message',
                'message': message,
            })

    async def send_message(self, event):
        print(event['message'])

        await self.send(text_data=json.dumps({
            'ledeger_name':event['message']['ledeger_name'],
            'ledeger_state':event['message']['ledeger_state'],
            'ledeger_website':event['message']['ledeger_website']
            
        }))