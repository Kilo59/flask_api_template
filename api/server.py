from flask import Flask, jsonify

APP = Flask(__name__)


@APP.route("/")
def home():
    return "Hello World!"


@APP.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    APP.run(debug=True)
