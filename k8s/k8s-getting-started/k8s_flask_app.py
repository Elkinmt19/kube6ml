import os
from flask import Flask, jsonify

app = Flask("k8s-flask")
@app.route('/')
def get_k8s_pod():
    pod_info = os.uname()

    return jsonify(pod_info)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)