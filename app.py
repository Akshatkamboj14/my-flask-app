# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.getenv('HOSTNAME', 'Unknown')
    return f"Hello from Docker and Kubernetes! Running on Pod: {pod_name}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

