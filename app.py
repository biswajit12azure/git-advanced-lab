from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Succesfully deployed Python App using Github Actions and Docker into EC2 Instance and Image stored inside DockerHub"})


@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    result = data.get('a', 0) + data.get('b', 0)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
