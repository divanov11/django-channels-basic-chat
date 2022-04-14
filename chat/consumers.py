import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Details

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        a = self.scope
        print(a)

        user_id = self.scope['url_route']['kwargs']['user_id']
        if user_id[-1]=='c':
            websocketKey = a['headers'][1][1]
        else:
            websocketKey = a['headers'][3][1]

        # windowServiceKey = 

        self.username = self.saveData(user_id, websocketKey)

        # print(websocketKey, " is the key of the websocket")
        # print(user_id, "This is the user ID")

        # removed bcz channel_layer is removed from settings.py
        # self.room_group_name = 'test'
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        self.accept()

        # socket id here
        # socket id store on user table

    def saveData(self, user_id, websocketKey):
        # print(user_id[-1], "This is the user ID")
        # print(websocketKey, "This is the websocket key")
        if user_id[-1]=='c': 
            Details.objects.filter(userid=user_id[:-1]).update(clientWebsocketKey = websocketKey)
        else: 
            Details.objects.filter(userid=user_id[:-1]).update(windowServiceKey = websocketKey)    
            print("socketKey updated Successfully")            

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
        # we'll get data from this method
        # socket id from windows service and store it on any table 
        # uuid match with socket id



        # we have to initialize websocket on url through which data will fatch

    # def chat_message(self, event):
    #     message = event['message']
    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message':message
    #     }))