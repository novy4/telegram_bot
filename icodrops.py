#!/usr/bin/python3

from telethon import TelegramClient
from telethon import utils
import time
import os, sys
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, from telegram bot")

application = tornado.web.Application([
    (r"/", MainHandler),
])


#My API values
api_id = 181055
api_hash ='8c267b7f0bcbdc604fe27b12142a9687'

phone_number = '+37368351333'

client = TelegramClient('me', api_id, api_hash)
client.start()

#print(client.get_me().stringify())
#client.send_message('self', 'Hello World from Telethon!')
#dialogs, entities = client.get_dialogs(dialog_count)


for message in client.get_message_history('icodrops', limit=1):
    last = message.id
    print(message.id)
    # print(message.media)
    # print(message.media.caption)

while True:

    for message in client.get_message_history('icodrops', min_id=last):
        # print(utils.get_display_name(message.sender), message.id, message.message) 
        cryptomessage = message.message
        if message.id > last:
            last = message.id
            # print(last)
        if cryptomessage != '':
            mesg1 = cryptomessage.encode('utf-8') 
            # print(mesg1)
            client.send_message('cryptoanalizatorfeed', mesg1)
            time.sleep(1)
        else:
            print(message.media.caption)
    time.sleep(30)

if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()
