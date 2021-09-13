#!/usr/bin/python3

import json
import datetime


def marginesy(l, margines):
    k = "\n" + margines
    l = k.join(l.split("\n"))
    return (l)


for i in range(37, 0, -1):
    file = 'message_' + str(i) + '.json'

    with open(file) as json_file:
        data = json.load(json_file)

        sender_time_old = 'dupa'
        for p in reversed(data['messages']):

            sender_name = p["sender_name"].encode("latin").decode("utf")
            if sender_name == 'Cezary Grądys':
                margines = ''
            else:
                margines = '\t'

            time = datetime.datetime.fromtimestamp(p["timestamp_ms"] / 1000.0).strftime("%Y-%m-%d %H:%M")
            sender_time = sender_name + '  ' + time

            if sender_time_old != sender_time:
                print("\n" + margines + sender_time)
                sender_time_old = sender_time

            if 'content' in p:
                print(margines + marginesy(p['content'].encode("latin").decode("utf"), margines))

            if 'gifs' in p:
                print(margines, end='')
                print(p['gifs'])

            if 'photos' in p:
                print(margines, end='')
                print(p['photos'])

            if 'sticker' in p:
                print(margines, end='')
                print(p['sticker'])

            if 'videos' in p:
                print(margines, end='')
                print(p['videos'])

            if 'share' in p:
                print(margines, end='')
                print(p['share'])

            if 'reactions' in p:
                print(margines, end='')
                print(p['reactions'])

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
