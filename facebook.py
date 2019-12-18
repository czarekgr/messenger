#!/usr/bin/python3.7

import json
import datetime

with open('message_1.json' ) as json_file:
    data = json.load(json_file)
    for p in data['messages']:


        print(p["sender_name"].encode("latin").decode("utf"))
        czas = datetime.datetime.fromtimestamp(p["timestamp_ms"]/1000.0)
        print(czas.date(), "", czas.time())
        if 'content' in p:
            print(p['content'].encode("latin").decode("utf")) # podzielić \n i odwrócić! dla tac!

        if 'gifs' in p:
            print(p['gifs'])

        if 'photos' in p:
            print(p['photos'])

        if 'sticker' in p:
            print(p['sticker'])

        if 'videos' in p:
            print(p['videos'])

        if 'share' in p:
            print(p['share'])

        if 'reactions' in p:
            print(p['reactions'])


        if 'share' in p:
            print(p['share'])


        if 'type' in p:
            print(p['type'])



''' sender_name timestamp_ms content photos type
sender_name timestamp_ms content reactions type
sender_name timestamp_ms content share type
sender_name timestamp_ms content type
sender_name timestamp_ms gifs reactions type
sender_name timestamp_ms photos reactions type
sender_name timestamp_ms photos type
sender_name timestamp_ms sticker type
sender_name timestamp_ms type
sender_name timestamp_ms videos type */ '''
