import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        service="lab-02-docker-service",
        environment=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
    )


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)