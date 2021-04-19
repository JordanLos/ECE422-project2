#!/usr/bin/env python
import asyncio
import websockets
import docker
import json
import numpy as np
import math
import requests

from redis import Redis

########## CONSTANTS ##########
swarm_master_ip = '10.2.9.255'
alpha = 0.7
upper_response_time_threshold = 4
lower_response_time_threshold = 2
#client = docker.from_env()

#redis = Redis(host='localhost', port=6379)
redis = Redis(host='redis', port=6379)

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

def get_container_number(rps, alpha):
    new_val = math.ceil(rps / alpha)
    if (new_val == 0):
        new_val = 1
    return new_val
    


async def time(websocket, path):
    # Init data
    x = np.arange(-120, 0, 0.5).tolist() # TODO remove and make it rolling
    y1 = np.zeros(len(x), dtype=int).tolist()
    y2 = np.zeros(len(x), dtype=int).tolist()
    y3 = np.zeros(len(x), dtype=int).tolist()

    rolling_response = [0, 0, 0, 0, 0]
    rolling_workload = [0, 0, 0, 0, 0]
    hits_prev = int(redis.get('hits').decode())

    replicas = 1

    while True:
        # Get Metrics
        hits_before = int(redis.get('hits').decode())
        response = requests.get('http://' + swarm_master_ip + ':8000' )
        response_time = response.elapsed.total_seconds()
        hits_after = int(redis.get('hits').decode())
        workload = hits_after - hits_before
        
        # Check threshold & Scale
        if ((response_time > upper_response_time_threshold) or (response_time < lower_response_time_threshold)):
            req_ps = workload/response_time
            new_replica_count = get_container_number(req_ps, alpha)
            #bottle_neck = next((x for x in client.services.list() if x.name == 'app_web'), None)
            #if bottle_neck != None:
            if False:
                did_it_scale = bottle_neck.scale(replicas)
                replicas = new_replica_count


        # Update Graph
        rolling_response = update_array(rolling_response, response_time)
        avg_response = avg_arr(rolling_response)
        y1 = update_array(y1, avg_response)

        hits_current = int(redis.get('hits').decode())
        workload = hits_current - hits_prev
        hits_prev = hits_current

        rolling_workload = update_array(rolling_workload, workload)
        avg_workload = avg_arr(rolling_workload)
        y2 = update_array(y2, avg_workload)

        y3 = update_array(y3, replicas)
    
        # Calculate X each time and normalize
        graph_to_send = json.dumps({'x1': x, 'y1': y1,
                                    'x2': x, 'y2': y2,
                                    'x3': x, 'y3': y3})

        await websocket.send(graph_to_send)
        # await asyncio.sleep(random.random() * 3)


start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
