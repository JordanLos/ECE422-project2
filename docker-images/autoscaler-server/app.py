#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

import json
import numpy as np

import requests
import time

# grab all data and send at the same time
# update all graphs at once


swarm_master_ip = '10.2.9.255'

def update_array(old_roll, new_resp):
    # drop the oldest response
    new_roll = old_roll[1:]
    # add new response
    new_roll.append(new_resp)
    return new_roll

def avg_arr(array):
    return sum(array)/len(array)

def get_new_response():
    response = requests.get('http://' + swarm_master_ip + ':8000')
    return response.elapsed.total_seconds()


async def time(websocket, path):
    # Init data
    rolling_response = [0,0,0,0,0]
    x = np.arange(-120, 0, 0.5).tolist()
    y1 = np.zeros(len(x), dtype=int).tolist()
    y2 = np.zeros(len(x), dtype=int).tolist()
    y3 = np.zeros(len(x), dtype=int).tolist()

    while True:
        response_time = get_new_response()
        rolling_response = update_array(rolling_response, response_time)
        avg_response = avg_arr(rolling_response)

        y1 = update_array(y1, avg_response)
        # Test data
        graph_to_send = json.dumps({'x1':x,'y1':y1,
                                    'x2':x,'y2':y2,
                                    'x3':x,'y3':y3})

        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(graph_to_send)
        #await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
