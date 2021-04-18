
from flask import Flask
import docker

app = Flask(__name__)

@app.route('/')
def hello_world():
    client = docker.from_env()

    # TODO: Maybe get some env var to make sure the name of the app is the same
    bottle_neck = next((x for x in client.services.list() if x.name == 'app_web'), None)
    did_it_scale = bottle_neck.scale(1)


    return  'Web Service: ' + str(did_it_scale)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
