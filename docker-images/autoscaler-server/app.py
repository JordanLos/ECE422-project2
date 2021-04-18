#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

import json
import numpy as np

async def time(websocket, path):
    while True:

        # Test data
        x = np.arange(-120, 0, 0.5).tolist()
        y1 = np.zeros(len(x), dtype=int).tolist()
        y2 = np.zeros(len(x), dtype=int).tolist()
        y3 = np.zeros(len(x), dtype=int).tolist()

        graph_to_send = json.dumps({'x1':x,'y1':y1,
                                    'x2':x,'y2':y2,
                                    'x3':x,'y3':y3})

        # now = datetime.datetime.utcnow().isoformat() + "Z"
        print("going to sleep")
        await websocket.send(graph_to_send)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
