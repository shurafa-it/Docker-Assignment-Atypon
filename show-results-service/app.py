from flask import Flask, jsonify, request
import requests
import pymongo

app = Flask(__name__)

AUTH_SERVICE_URL = "http://authentication-service:5001/auth"
mongo_client = pymongo.MongoClient("mongodb://mongo-db:27017/")
mongo_db = mongo_client["analytics_db"]
mongo_collection = mongo_db["results"]

@app.route("/results", methods=["GET"])
def results():
    username = request.args.get("username")
    password = request.args.get("password")

    auth_response = requests.post(AUTH_SERVICE_URL, json={"username": username, "password": password})
    if auth_response.status_code != 200:
        return jsonify({"message": "Authentication failed"}), 401

    results = list(mongo_collection.find({}, {"_id": 0}))
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
