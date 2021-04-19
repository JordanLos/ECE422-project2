#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import websockets
import random
import json
import numpy as np

import requests

from redis import Redis

##### CONSTANT ##########
swarm_master_ip = '10.2.9.255'
# redis = Redis(host='redis', port=6379)
redis = Redis(host='localhost', port=6379)

#### HELPER FUNCTIONS ####
def update_array(old_roll, new_resp):
    # drop the oldest response
    new_roll = old_roll[1:]
    # add new response
    new_roll.append(new_resp)
    return new_roll


def avg_arr(array):
    return sum(array) / len(array)


def get_new_response():
    response = requests.get('http://' + swarm_master_ip + ':8000')
    return response.elapsed.total_seconds()


def get_workload(old_workload):
    current_workload = int(redis.get('hits').decode())
    print("old: " + str(old_workload) + ", new: ," + str(current_workload))
    return current_workload - old_workload


async def time(websocket, path):
    # Init data
    x = np.arange(-120, 0, 0.5).tolist()
    y1 = np.zeros(len(x), dtype=int).tolist()
    y2 = np.zeros(len(x), dtype=int).tolist()
    y3 = np.zeros(len(x), dtype=int).tolist()

    rolling_response = [0, 0, 0, 0, 0]
    rolling_workload = [0, 0, 0, 0, 0]
    hits_prev = int(redis.get('hits').decode())

    replicas = 1

    graph_to_send = {'x1': x, 'y1': y1,
                     'x2': x, 'y2': y2,
                     'x3': x, 'y3': y3}
    graph_to_send = json.dumps({'message': 'INIT', 'data': graph_to_send})

    await websocket.send(graph_to_send)
    while True:
        # response_time = get_new_response()
        # rolling_response = update_array(rolling_response, response_time)
        # avg_response = avg_arr(rolling_response)
        # y1 = update_array(y1, avg_response)
        #
        # hits_current = int(redis.get('hits').decode())
        # workload = hits_current - hits_prev
        # hits_prev = hits_current
        #
        # rolling_workload = update_array(rolling_workload, workload)
        # avg_workload = avg_arr(rolling_workload)
        # y2 = update_array(y2, avg_workload)
        #
        # y3 = update_array(y3, replicas)
        # # Test data
        # graph_to_send = {'x1': x, 'y1': y1,
        #                  'x2': x, 'y2': y2,
        #                  'x3': x, 'y3': y3}
        graph_to_send = json.dumps({'message': 'UPDATE', 'data': "hey"})

        await websocket.send(graph_to_send)
        await asyncio.sleep(random.random() * 3)


start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
