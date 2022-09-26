import os
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Main: " + "Hello from main!"


@app.route("/helloDocker")
def hello_world_docker():
    docker_message = ""
    try:
        docker_message = os.environ("DOCKER_ENV")
    except Exception:
        docker_message = "docker env not found"
    return "Docker: " + docker_message


# Return max value between 2 values
def max(a, b):
    if a > b:
        # for i in 10:
        #     print(i)
        return a
    else:
        return b
