import json
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from matplotlib.font_manager import json_dump
from .models import *
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print(self.scope)
        user_id=self.scope['url_route']['kwargs']['user_id']
        username=self.scope['url_route']['kwargs']['username']
        
        self.room_group_name = f'{username}'
        await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name)

        if user_id[-1]=='c':
            self.username =  self.save_keys(user_id,self.scope['headers'][1][1])
            print(self.scope['headers'][1][1])
        else:
            self.username =  self.save_keys(user_id,self.scope['headers'][3][1])
            print(self.scope['headers'][3][1])
        d=await self.username
        print(d)
       
        await self.accept()
        await self.send('connected to the server')
        # self.room_group_name = 'test'
        # await (self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

    @database_sync_to_async
    def save_keys(self,userid,key):
        userid1=userid.rstrip(userid[-1])
        obj=userDetail.objects.get(userid=userid1)
        key=key.decode()
        mykey=userid[-1]
        if mykey=='c':
            obj.key1=key
        else:
            obj.key2=key
        obj.save()
        return None

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        data=self.get_data(1)
        data= await data
        message={}
        message['name']=data.name,
        message['id']=data.userid

        original_data = await text_data
        self.save_database(original_data)

        # self.save_data(message)
    # Send message to room group
        await self.channel_layer.group_send(
        self.room_group_name,
        {   'type':'send_message',
            'message': message,
        } )

    async def send_message(self, event):
        message = event['message']
        print(message)
        await self.send(text_data=json.dumps({
            'message':message
        }))

    @database_sync_to_async
    def get_data(self,id):
        obj=userDetail.objects.get(id=id)
        return obj

    @database_sync_to_async
    def save_database(self,original_data):
        original_data = json.loads(original_data)
        print(original_data, "This is the original_data")


        