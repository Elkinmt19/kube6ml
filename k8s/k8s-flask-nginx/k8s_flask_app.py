import os
import requests
from flask import Flask, jsonify

app = Flask("k8s-flask-nginx")
@app.route('/', )
def get_k8s_pod():
    pod_info = os.uname()

    return jsonify(pod_info)

@app.route("/nginx")
def call_nginx():
    url = 'http://nginx'
    response = requests.get(url)

    result = {
        "status_code": response.status_code,
        "response": response.text
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)